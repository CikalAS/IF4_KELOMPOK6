📊 Dashboard Analisis Polusi Udara
📌 Deskripsi Proyek
Dashboard ini dirancang untuk menganalisis data polusi udara di Guanyuan dari tahun 2013 hingga 2017. Data yang digunakan mencakup:
✅ Polutan udara: PM2.5, PM10, SO2, NO2, CO, O3
✅ Faktor cuaca: Suhu (TEMP), Tekanan Udara (PRES), Titik Embun (DEWP), Curah Hujan (RAIN), Kecepatan Angin (WSPM)

📊 Visualisasi interaktif dibuat menggunakan Streamlit, memungkinkan pengguna mengeksplorasi tren polusi dengan lebih mudah.

🔧 Fitur Utama
🔹 Filter Interaktif → Pilih tahun & bulan untuk analisis spesifik
🔹 Tren Polusi Udara → Grafik perubahan polusi berdasarkan waktu
🔹 Heatmap Korelasi → Menunjukkan hubungan polusi dengan faktor cuaca
🔹 Peta Interaktif → Distribusi polutan dalam area penelitian
🔹 Kesimpulan & Dokumentasi → Ringkasan hasil analisis

📂 Struktur File
📜 DashBoard_Polusi.py → Kode utama dashboard (Streamlit)
📊 PRSA_Data_Guanyuan_20130301-20170228.csv → Dataset polusi udara
⚙️ requirements.txt → Daftar pustaka Python yang dibutuhkan
📖 README.md → Dokumentasi proyek ini

🚀 Cara Menjalankan Dashboard
1️⃣ Pastikan Python Terinstal
Jika belum memiliki Python, unduh dari python.org.

2️⃣ Install Dependensi
Jalankan perintah berikut untuk menginstal pustaka yang diperlukan:

bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Jalankan Streamlit
Gunakan perintah berikut untuk menjalankan dashboard:

bash
Copy
Edit
streamlit run DashBoard_Polusi.py
4️⃣ Akses Dashboard
Setelah berjalan, buka salah satu link berikut di browser:
🌍 Localhost → http://localhost:8501
☁️ Online (Streamlit Cloud) → https://dashboard-polusi-guanyuan.streamlit.app/

❗ Troubleshooting (Mengatasi Error)
⚠️ Modul Tidak Ditemukan (ModuleNotFoundError)
Jika error seperti ini muncul:

bash
Copy
Edit
ModuleNotFoundError: No module named 'folium'
Solusi:

bash
Copy
Edit
pip install folium streamlit-folium
⚠️ File Tidak Ditemukan (File does not exist)
Jika muncul error seperti ini:

bash
Copy
Edit
Error: Invalid value: File does not exist: DashBoard_Polusi.py
Solusi: Pastikan berada di folder proyek sebelum menjalankan Streamlit:

bash
Copy
Edit
cd C:\Users\acer_\OneDrive\Desktop\UAS_PDSD_IF4_KELOMPOK6
⚠️ Localhost Tidak Bisa Dibuka
Jika http://localhost:8501 tidak bisa diakses:
✅ Pastikan Streamlit berjalan dengan benar
✅ Coba jalankan di port lain:

bash
Copy
Edit
streamlit run DashBoard_Polusi.py --server.port 8502
✅ Matikan firewall atau antivirus sementara

🌍 Menjalankan Dashboard Secara Online
🔹 Akses Dashboard di Streamlit Cloud
Setelah berhasil dideploy, dashboard dapat diakses di:
➡️ Streamlit Cloud

🔹 Langkah-langkah Deploy ke Streamlit Cloud
1️⃣ Upload proyek ke GitHub (pastikan file utama dan dataset sudah tersedia).
2️⃣ Buka Streamlit Cloud dan buat aplikasi baru.
3️⃣ Pilih repository GitHub yang berisi proyek ini.
4️⃣ Tentukan file utama → DashBoard_Polusi.py.
5️⃣ Pastikan requirements.txt ada untuk menginstal pustaka yang diperlukan.
6️⃣ Klik "Deploy", tunggu hingga aplikasi siap digunakan.

✨ Anggota Kelompok
👤 Cikal Agustian S (10123153)
👤 M. Abduh (10123148)
👤 Delia Aksani (10123156)
👤 Rainhard Frealdo S (10123169)

© 2025 Dashboard Analisis Polusi Udara 🌎📊
