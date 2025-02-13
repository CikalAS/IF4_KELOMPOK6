

📊 Dashboard Analisis Polusi Udara

📌 Deskripsi Proyek

Dashboard ini dibuat untuk menganalisis data polusi udara di Guanyuan dari tahun 2013 hingga 2017. Data yang digunakan mencakup berbagai polutan udara (PM2.5, PM10, SO2, NO2, CO, O3) serta faktor cuaca (TEMP, PRES, DEWP, RAIN, WSPM). Visualisasi interaktif ditampilkan menggunakan Streamlit, yang memungkinkan pengguna untuk mengeksplorasi tren polusi secara dinamis.

🔧 Fitur Utama

Filter Interaktif → Memilih tahun dan bulan untuk analisis

Tren Polusi Udara → Grafik perubahan polusi berdasarkan waktu

Heatmap Korelasi → Menunjukkan hubungan antara polusi dan faktor cuaca

Peta Interaktif → Distribusi polutan dalam area penelitian

Kesimpulan & Dokumentasi → Ringkasan temuan utama dari analisis data

📂 Struktur File

DashBoard_Polusi.py → Kode utama dashboard menggunakan Streamlit

PRSA_Data_Guanyuan_20130301-20170228.csv → Dataset polusi udara

requirements.txt → Daftar pustaka Python yang diperlukan

README.md → Dokumentasi proyek ini

🚀 Cara Menjalankan Dashboard

1️⃣ Pastikan Python Terinstal

Jika belum memiliki Python, unduh dan instal dari python.org.

2️⃣ Install Dependensi

Pastikan semua pustaka yang dibutuhkan sudah terinstal dengan menjalankan:

pip install -r requirements.txt

3️⃣ Jalankan Streamlit

streamlit run DashBoard_Polusi.py

4️⃣ Akses Dashboard

Setelah dijalankan, buka salah satu dari link berikut di browser:

Localhost: http://localhost:8501

Online (Streamlit Cloud): https://if4kelompok6-dashboardpolusiudara.streamlit.app/

❗ Troubleshooting

Jika terjadi error, coba langkah-langkah berikut:

⚠️ Modul Tidak Ditemukan (ModuleNotFoundError)

Jika error seperti ini muncul:

ModuleNotFoundError: No module named 'folium'

Jalankan perintah berikut untuk menginstal pustaka yang hilang:

pip install folium streamlit-folium

⚠️ File Tidak Ditemukan (File does not exist)

Jika muncul error:

Error: Invalid value: File does not exist: DashBoard_Polusi.py

Pastikan Anda berada di folder proyek sebelum menjalankan Streamlit:

cd C:\Users\acer_\OneDrive\Desktop\UAS_PDSD_IF4_KELOMPOK6

⚠️ Localhost Tidak Bisa Dibuka

Jika http://localhost:8501 tidak bisa diakses:

Pastikan Streamlit berjalan dengan benar.

Coba jalankan di port lain:

streamlit run DashBoard_Polusi.py --server.port 8502

Matikan firewall atau antivirus sementara karena bisa memblokir localhost.

🌍 Menjalankan Dashboard Secara Online

🔹 Membuka Dashboard di Streamlit Cloud

Setelah berhasil di-deploy, dashboard dapat diakses melalui:

Streamlit Cloud: https://if4kelompok6-dashboardpolusiudara.streamlit.app/

🔹 Langkah-langkah Deploy ke Streamlit Cloud

Upload proyek ke GitHub (pastikan file utama dan dataset sudah tersedia).

Buka Streamlit Cloud dan buat aplikasi baru.

Pilih repository GitHub yang berisi proyek ini.

Tentukan file utama → DashBoard_Polusi.py.

Pastikan file requirements.txt ada untuk menginstal pustaka yang diperlukan.

Klik 'Deploy' dan tunggu hingga aplikasi siap digunakan.

✨ Anggota Kelompok

Nama 1

Nama 2

Nama 3

Nama 4

Nama 5

© 2025 Dashboard Analisis Polusi Udara

