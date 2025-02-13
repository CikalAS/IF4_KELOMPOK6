📊 Dashboard Analisis Polusi Udara dan Cuaca di Guanyuan
🚀 Deskripsi Singkat
Dashboard ini dibuat untuk menganalisis tren polusi udara dan faktor cuaca di Guanyuan dari tahun 2013 hingga 2017. Dengan menggunakan dataset PRSA Data Guanyuan, kita dapat melihat pola perubahan kualitas udara berdasarkan polutan tertentu (seperti PM2.5) serta faktor cuaca yang memengaruhinya.

🔍 Fitur Utama
✅ Filter Tahun & Bulan – Pengguna dapat memilih tahun dan bulan untuk melihat tren polusi udara.
✅ Visualisasi Interaktif – Grafik dan plot yang memperlihatkan tren PM2.5 secara historis.
✅ Analisis Data – Penerapan teknik statistik dan machine learning untuk memahami pola data.

⚙️ Cara Menjalankan Proyek
1️⃣ Clone Repository
bash
Copy
Edit
git clone https://github.com/CikalAS/IF4_KELOMPOK6.git
cd IF4_KELOMPOK6
2️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Jalankan Dashboard
bash
Copy
Edit
streamlit run DashBoard_Polusi.py
4️⃣ Buka di Browser
🔗 http://localhost:8501/

🌍 Deployment
🔗 Akses Dashboard Online (Tambahkan link setelah dideploy!)

📂 Struktur Repository
bash
Copy
Edit
IF4_KELOMPOK6/
│── DashBoard_Polusi.py        # Script utama untuk menjalankan dashboard
│── PRSA_Data_Guanyuan_2013... # Dataset yang digunakan
│── requirements.txt           # Daftar library yang diperlukan
│── README.md                  # Dokumentasi proyek ini
│── notebook/                  
│   ├── Analisis_Polusi.ipynb  # Jupyter Notebook untuk eksplorasi data
📚 Library yang Digunakan
streamlit
pandas
matplotlib
seaborn
scikit-learn (untuk teknik analisis lanjutan seperti clustering)
(Tambahkan jika ada library lain!)
🎥 Video Demo
📺 YouTube Link (Tambahkan link setelah video dibuat!)


🚀 Cara Deploy ke Streamlit Cloud
Pastikan repository GitHub sudah lengkap dengan file .py, dataset, dan requirements.txt.
Login ke Streamlit Cloud.
Klik "New App", lalu pilih repository GitHub kalian.
Pilih branch (main) dan file utama (DashBoard_Polusi.py).
Klik "Deploy", dan tunggu hingga proses selesai.
Setelah berhasil, kalian akan mendapatkan link dashboard online.
