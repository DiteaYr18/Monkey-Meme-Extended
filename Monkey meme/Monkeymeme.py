import pandas as pd
from sklearn.neighbors import KNeighborsClassifier # Perhatikan: Sekarang pakai "Classifier"
from sklearn.preprocessing import LabelEncoder

# 1. PERSIAPAN DATA
df = pd.read_csv('laptopPrice.csv')

# Bersihkan RAM dan SSD (Hapus 'GB')
df['ram_gb'] = df['ram_gb'].str.replace(' GB', '').astype(int)
df['ssd'] = df['ssd'].str.replace(' GB', '').astype(int)

# Ubah Processor jadi Angka (Encoding)
encoder = LabelEncoder()
df['processor_code'] = encoder.fit_transform(df['processor_name'])

# Ubah Rating jadi Angka Sederhana (Mapping)
# Kita buat kamus bahasa: "5 stars" artinya 5, dst.
kamus_rating = {
    '1 star': 1, '2 stars': 2, '3 stars': 3, 
    '4 stars': 4, '5 stars': 5
}
df['rating_angka'] = df['rating'].map(kamus_rating)

# 2. LATIH MODEL (Training)
# Kita pakai data: RAM, SSD, Processor, dan Harga untuk menebak Rating
X = df[['ram_gb', 'ssd', 'processor_code', 'Price']]
y = df['rating_angka']

# Panggil KNN Klasifikasi (Cari 5 tetangga)
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X, y)

# 3. PREDIKSI (Menebak Rating Laptop Baru)
# Misal: Laptop Core i7 (kode 3), RAM 16GB, SSD 512GB, Harganya 126.000 (sesuai prediksi sebelumnya)
kode_i7 = encoder.transform(['Core i7'])[0] 
laptop_baru = [[16, 512, kode_i7, 126000]]

prediksi_rating = model.predict(laptop_baru)

print(f"Spesifikasi Laptop: RAM 16GB, SSD 512GB, Core i7, Harga ~126k")
print(f"Prediksi Rating: {prediksi_rating[0]} Bintang")import cv2
import numpy as np
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '-1' # Paksa pakai CPU
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Hilangkan log warning yang berisik

# --- KONFIGURASI ---
# Menggunakan tf_keras agar kompatibel dengan model Teachable Machine lama
os.environ["TF_USE_LEGACY_KERAS"] = "1"

try:
    from tf_keras.models import load_model
except ImportError:
    print("Error: Library 'tf_keras' belum terinstall.")
    print("Silakan jalankan di terminal: pip install tf_keras")
    exit()

MODEL_PATH = "tensorflow.h5"
LABELS_PATH = "labels.txt"

image_map = {
    0: "Manyun.jpeg",
    1: "Monyet1.jpeg",
    2: "Monyet2.jpeg",
    3: "Ragebait.jpeg",
    4: "Kaget.jpeg"
}

np.set_printoptions(suppress=True)

# 1. Load Model
print("Sedang memuat model (Menggunakan tf_keras)...")

try:
    # Compile=False penting agar tidak perlu load optimizer yang berat
    model = load_model(MODEL_PATH, compile=False)
    
    # Load Label
    class_names = open(LABELS_PATH, "r").readlines()
    print("✅ Model BERHASIL dimuat!")

except Exception as e:
    print("\nTERJADI ERROR SAAT LOAD MODEL:")
    print(e)
    print("\nPastikan file 'tensorflow.h5' ada di folder yang sama.")
    exit()

# 2. Siapkan Kamera
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# Gambar default (hitam)
current_reaction_img = np.zeros((400, 400, 3), dtype=np.uint8)
last_prediction_index = -1

print("Kamera akan menyala dalam 3 detik...")

while True:
    ret, image = cap.read()
    if not ret:
        break

    # --- PREPROCESSING ---
    # Resize ke 224x224 sesuai standar Teachable Machine
    image_resized = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
    
    # Ubah ke array dan bentuk (1, 224, 224, 3)
    image_input = np.asarray(image_resized, dtype=np.float32).reshape(1, 224, 224, 3)
    
    # Normalisasi (Range -1 sampai 1)
    image_input = (image_input / 127.5) - 1

    # --- PREDIKSI ---
    prediction = model.predict(image_input, verbose=0)
    index = np.argmax(prediction)
    class_name = class_names[index].strip()
    confidence_score = prediction[0][index]

    # --- LOGIKA TAMPILAN GAMBAR ---
    if index != last_prediction_index:
        filename = image_map.get(index)
        if filename:
            try:
                loaded_img = cv2.imread(filename)
                if loaded_img is not None:
                    current_reaction_img = cv2.resize(loaded_img, (400, 400))
                else:
                    # Jika gambar tidak ketemu, buat layar merah
                    current_reaction_img[:] = (0, 0, 255) 
            except:
                pass
        last_prediction_index = index

    # --- TAMPILKAN HASIL ---
    # Persentase
    confidence_percent = int(confidence_score * 100)
    text = f"{class_name}: {confidence_percent}%"
    
    # Warna text: Hijau jika yakin (>80%), Merah jika ragu
    text_color = (0, 255, 0) if confidence_percent > 80 else (0, 0, 255)

    # Kotak background text
    cv2.rectangle(image, (5, 5), (400, 40), (0, 0, 0), -1) 
    cv2.putText(image, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, text_color, 2)

    cv2.imshow("Webcam Input", image)
    cv2.imshow("Reaksi Mesin", current_reaction_img)

    if cv2.waitKey(1) == 27: # Tekan ESC untuk keluar
        break

cap.release()
cv2.destroyAllWindows()
