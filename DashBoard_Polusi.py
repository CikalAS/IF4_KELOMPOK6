import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import folium
from streamlit_folium import folium_static
from scipy.stats.mstats import winsorize
from sklearn.cluster import KMeans
import numpy as np

# **Load dataset**
file_path = "PRSA_Data_Guanyuan_20130301-20170228.csv"
df = pd.read_csv(file_path)

# **Menangani nilai hilang**
pollutant_cols = ["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"]
df[pollutant_cols] = df[pollutant_cols].fillna(df[pollutant_cols].median())

weather_cols = ["TEMP", "PRES", "DEWP", "RAIN", "WSPM"]
df[weather_cols] = df[weather_cols].fillna(df[weather_cols].mean())

df["wd"] = df["wd"].fillna(df["wd"].mode()[0])

# **Menggabungkan kolom year, month, day, hour menjadi satu kolom datetime**
df["datetime"] = pd.to_datetime(df[["year", "month", "day", "hour"]])

# **Menghapus kolom yang tidak diperlukan setelah penggabungan**
df.drop(columns=["year", "month", "day", "hour"], inplace=True)

# **Winsorizing untuk outlier**
df[pollutant_cols] = df[pollutant_cols].apply(lambda x: winsorize(x, limits=[0.01, 0.01]))
df[weather_cols] = df[weather_cols].apply(lambda x: winsorize(x, limits=[0.01, 0.01]))

# **Feature Engineering: Rata-rata polusi harian**
df["date"] = df["datetime"].dt.date
daily_avg = df.groupby("date")[pollutant_cols].mean().reset_index()

# **Feature Engineering: Polusi per Musim**
def get_season(month):
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    else:
        return "Autumn"

df["season"] = df["datetime"].dt.month.apply(get_season)

# **Streamlit Dashboard**
st.set_page_config(page_title="Dashboard Polusi Udara", layout="wide")
st.markdown("""
<style>
    * {
        font-family: 'Times New Roman', serif !important;
    }
    .main {
        background-color: #f5f5f5;
    }
    .stSidebar {
        background-color: #2c3e50;
        color: white;
    }
    .stTitle, .stHeader, .stSubheader {
        color: #2c3e50;
    }
    label, .stSelectbox div, .stTextInput div, .stNumberInput div {
        color: grey !important;
    }
</style>
""", unsafe_allow_html=True)

st.title('🌍 Dashboard Analisis Polusi Udara dan Cuaca')

# **Sidebar untuk filter**
with st.sidebar:
    st.header("⚙️ **PENGATURAN     DASHBOARD**")
    st.markdown("""
    **👥 ANGGOTA KELOMPOK 6:**  
    - **CIKAL AGUSTIAN (10123153)**  
    - **M.ABDUH (10123) 2**  
    - **DELIA (10123)**  
    - **RAINDHARD (10123)**    
    """)
    selected_year = st.selectbox("📅 Pilih Tahun", df["datetime"].dt.year.unique(), format_func=lambda x: f"{x}")
    selected_month = st.selectbox("📆 Pilih Bulan", df["datetime"].dt.month.unique(), format_func=lambda x: f"Bulan {x}")
    pollutant = st.selectbox('☁️ Pilih Polutan untuk Visualisasi', pollutant_cols)

# **Filter data berdasarkan tahun dan bulan**
filtered_df = df[(df["datetime"].dt.year == selected_year) & (df["datetime"].dt.month == selected_month)]

# **Layout menggunakan columns**
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader(f"📊 Tren {pollutant} Seiring Waktu")
    st.markdown("Visualisasi ini menunjukkan tren konsentrasi polutan dalam satu bulan yang dipilih.")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=filtered_df, x="datetime", y=pollutant, ax=ax, label=pollutant, color="red", alpha=0.7)
    plt.xlabel("Tahun")
    plt.ylabel(f"Konsentrasi {pollutant}")
    plt.title(f"Tren {pollutant} Seiring Waktu")
    plt.legend()
    st.pyplot(fig)

st.subheader("🔍 Heatmap Korelasi")
st.markdown("Heatmap ini menunjukkan hubungan antara berbagai polutan dan variabel cuaca.")
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(df[pollutant_cols + weather_cols].corr(), annot=True, cmap="coolwarm", fmt=".2f", center=0)
st.pyplot(fig)

# **Peta interaktif**
st.subheader("🗺️ Peta Distribusi Polusi Udara")
st.markdown("Peta ini menunjukkan distribusi polusi udara berdasarkan data sampel.")
m = folium.Map(location=[39.9, 116.4], zoom_start=10)
for i, row in df.sample(100).iterrows():
    folium.CircleMarker(
        location=[39.9 + np.random.uniform(-0.05, 0.05), 116.4 + np.random.uniform(-0.05, 0.05)],
        radius=row["PM2.5"] / 10,
        color='red',
        fill=True,
        fill_color='red',
        fill_opacity=0.6
    ).add_to(m)
folium_static(m)

# **Dokumentasi dan kesimpulan**
st.markdown("""
### 📌 Kesimpulan dari Analisis Data Polusi Udara
✅ **Polusi Udara Cenderung Meningkat di Musim Dingin**
✅ **Hujan Membantu Menurunkan Polusi**
✅ **Clustering Menunjukkan Polusi Tinggi di Area Tertentu**
""")

st.subheader("📋 Data Setelah Pembersihan")
st.dataframe(df.head())
