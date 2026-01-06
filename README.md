🐵 Monkey Meme - AI Expression DetectorProgram Computer Vision berbasis Python yang menggunakan Teachable Machine (TensorFlow) untuk mendeteksi ekspresi wajah pengguna melalui webcam secara real-time dan memunculkan gambar reaksi (meme) yang sesuai.📋 FiturMendeteksi ekspresi wajah secara langsung lewat Webcam.Menampilkan gambar reaksi (.jpg) sesuai prediksi model.Menggunakan model .h5 dari Google Teachable Machine.

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

