🐵 Monkey Meme - AI Expression DetectorProgram Computer Vision berbasis Python yang menggunakan Teachable Machine (TensorFlow) untuk mendeteksi ekspresi wajah pengguna melalui webcam secara real-time dan memunculkan gambar reaksi (meme) yang sesuai.📋 FiturMendeteksi ekspresi wajah secara langsung lewat Webcam.Menampilkan gambar reaksi (.jpg) sesuai prediksi model.Menggunakan model .h5 dari Google Teachable Machine.📂 Struktur FilePastikan semua file ini berada dalam satu folder yang sama (disarankan di C:\cv_project untuk pengguna Windows):PlaintextC:\cv_project\
│
├── main.py                # Script utama Python (atau Monkey Meme.py)
├── keras_model.h5         # Model AI hasil training
├── labels.txt             # (Opsional) Daftar label
│
├── Manyun.jpg             # Gambar Reaksi Class 0
├── Monyet1.jpg            # Gambar Reaksi Class 1
├── Monyet2.jpg            # Gambar Reaksi Class 2
├── Ragebait.jpg           # Gambar Reaksi Class 3
└── Kaget.jpg              # Gambar Reaksi Class 4
🛠️ Persyaratan SistemPython 3.9 - 3.12Webcam yang berfungsi
🚀 Cara Instalasi (Windows)Karena TensorFlow memiliki struktur file yang dalam, sangat disarankan menggunakan Virtual Environment di folder dengan alamat pendek (seperti di Drive C) untuk menghindari error "Long Path".Buat Folder Proyek:Buka Terminal / PowerShell dan jalankan:PowerShellcd C:\
mkdir cv_project
cd cv_project
Buat Virtual Environment:PowerShellpython -m venv venv
Aktifkan Environment:PowerShell.\venv\Scripts\Activate
(Pastikan muncul tulisan (venv) di awal baris terminal).
Install Library:PowerShellpip install opencv-python tensorflow numpy
Pindahkan File:Copy file script Python Anda, keras_model.h5, dan semua gambar
jpg ke dalam folder C:\cv_projec.
▶️ Cara MenjalankanPastikan terminal masih berada di folder proyek dan virtual environment aktif (venv).Jalankan perintah:PowerShellpython main.py
(Ganti main.py dengan nama file Anda, misal Monkey Meme.py jika belum diganti).
🎮 KontrolESC: Tekan tombol Esc pada keyboard untuk menutup program dan mematikan kamera.
🤖 Daftar Kelas (Prediksi)Program ini dikonfigurasi untuk mendeteksi 5 gerakan:IndexEkspresiFile Gambar Muncul
0 ManyunManyun.jpg
1 Monyet 1Monyet1.jpg
2 Monyet 2Monyet2.jpg
3 RagebaitRagebait.jpg
4 KagetKaget.jpg
⚠️ TroubleshootingJika muncul error "ModuleNotFoundError" atau "Errno 2 No such file":Pastikan Anda sudah mengaktifkan venv sebelum menjalankan program.Pastikan folder proyek tidak terlalu dalam (jangan taruh di dalam folder Downloads yang panjang, pindahkan ke C:\cv_project).
