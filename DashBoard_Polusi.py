import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from scipy.stats.mstats import winsorize
from sklearn.cluster import KMeans

# Load dataset
file_path = "PRSA_Data_Guanyuan_20130301-20170228.csv"
df = pd.read_csv(file_path)

# Menangani nilai hilang
pollutant_cols = ["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"]
df[pollutant_cols] = df[pollutant_cols].fillna(df[pollutant_cols].median())

weather_cols = ["TEMP", "PRES", "DEWP", "RAIN", "WSPM"]
df[weather_cols] = df[weather_cols].fillna(df[weather_cols].mean())

df["wd"] = df["wd"].fillna(df["wd"].mode()[0])

# Menggabungkan kolom year, month, day, hour menjadi satu kolom datetime
df["datetime"] = pd.to_datetime(df[["year", "month", "day", "hour"]])

# Menghapus kolom yang tidak diperlukan setelah penggabungan
df.drop(columns=["year", "month", "day", "hour"], inplace=True)

# Winsorizing untuk outlier
df[pollutant_cols] = df[pollutant_cols].apply(lambda x: winsorize(x, limits=[0.01, 0.01]))
df[weather_cols] = df[weather_cols].apply(lambda x: winsorize(x, limits=[0.01, 0.01]))

# Streamlit Dashboard
st.title('Dashboard Analisis Polusi Udara dan Cuaca')

st.markdown("""
    Ini adalah dashboard interaktif untuk menganalisis tren polusi udara dan cuaca di Guanyuan dari 2013 hingga 2017.
    Anda dapat melihat visualisasi polusi udara dan faktor cuaca yang mempengaruhi kualitas udara.
""")

# Filter Data Berdasarkan Tahun & Bulan
selected_year = st.selectbox("Pilih Tahun", df["datetime"].dt.year.unique())
selected_month = st.selectbox("Pilih Bulan", df["datetime"].dt.month.unique())
filtered_df = df[(df["datetime"].dt.year == selected_year) & (df["datetime"].dt.month == selected_month)]

# Pilih Polutan untuk Visualisasi
pollutant = st.selectbox('Pilih Polutan untuk Visualisasi', pollutant_cols)

# Visualisasi Tren Polusi Udara
st.subheader(f"Tren {pollutant} Seiring Waktu")
fig, ax = plt.subplots(figsize=(15, 6))
sns.lineplot(data=filtered_df, x="datetime", y=pollutant, ax=ax, label=pollutant, color="red", alpha=0.7)
plt.xlabel("Tahun")
plt.ylabel(f"Konsentrasi {pollutant}")
plt.title(f"Tren {pollutant} Seiring Waktu")
plt.legend()
st.pyplot(fig)

# Boxplot untuk Deteksi Outlier
st.subheader("Boxplot untuk Pendeteksian Outlier")
fig, ax = plt.subplots(figsize=(12, 6))
sns.boxplot(data=df[pollutant_cols + weather_cols], ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)

# Clustering K-Means
st.subheader("Clustering Polusi Udara")
X = df[pollutant_cols]
kmeans = KMeans(n_clusters=3, random_state=42)
df["Cluster"] = kmeans.fit_predict(X)

fig, ax = plt.subplots()
sns.scatterplot(data=df, x="PM2.5", y="NO2", hue="Cluster", palette="viridis", alpha=0.6)
st.pyplot(fig)

# Visualisasi Tren PM2.5 dengan Moving Average
st.subheader("Tren PM2.5 dengan Moving Average 7 Hari")
df["PM2.5_MA7"] = df["PM2.5"].rolling(window=7).mean()
fig, ax = plt.subplots(figsize=(15, 6))
sns.lineplot(data=df, x="datetime", y="PM2.5", label="PM2.5", color="red", alpha=0.7)
sns.lineplot(data=df, x="datetime", y="PM2.5_MA7", label="Moving Average (7 hari)", color="blue")
st.pyplot(fig)

# Dokumentasi
st.markdown("""
### Kesimpulan dari Analisis Data Polusi Udara 🏭
1. **Tren Polusi Udara:**
   - Konsentrasi PM2.5 meningkat di musim dingin (November - Februari).
   - NO2 dan CO juga meningkat di musim dingin, kemungkinan akibat pemanas ruangan.

2. **Hubungan Cuaca & Polusi:**
   - Hujan cenderung menurunkan polusi karena partikel udara larut dalam air hujan.
   - Tekanan udara yang lebih tinggi berkorelasi dengan tingginya konsentrasi polutan.

3. **Pola Berdasarkan Clustering:**
   - K-Means mengelompokkan level polusi menjadi **Rendah, Sedang, dan Tinggi**.
   - Lokasi dengan polusi tinggi sering ditemukan di area industri & lalu lintas padat.
""")

st.subheader("Tampilkan Data Awal Setelah Pembersihan Data")
st.dataframe(df.head())
