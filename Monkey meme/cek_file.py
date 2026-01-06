import os

# Daftar file yang WAJIB ada
files_to_check = [
    "Manyun.jpg",
    "Monyet1.jpg",
    "Monyet2.jpg",
    "Ragebait.jpg",
    "Kaget.jpg",
    "tensorflow.h5",
    "labels.txt"
]

print("--- MULAI PENGECEKAN FILE ---")
print(f"Lokasi folder saat ini: {os.getcwd()}")
print("-----------------------------")

all_good = True

for filename in files_to_check:
    if os.path.exists(filename):
        print(f"✅ DITEMUKAN: {filename}")
    else:
        print(f"❌ HILANG   : {filename}")
        all_good = False
        
        # Cek apakah ada file dengan nama mirip (misal salah ekstensi)
        files_in_dir = os.listdir()
        for f in files_in_dir:
            if filename.split('.')[0].lower() in f.lower():
                print(f"   >>> APAKAH MAKSUD KAMU: '{f}' ?")

print("-----------------------------")
if all_good:
    print("KESIMPULAN: Semua file lengkap! Masalah ada di kode utama.")
else:
    print("KESIMPULAN: Ada file yang namanya salah atau tidak ada.")
    print("Solusi: Ubah nama file di folder agar SAMA PERSIS dengan yang HILANG.")