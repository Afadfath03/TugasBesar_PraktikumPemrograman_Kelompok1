def View():
    #TODO Lihat Data Mahasiswa
    return

def Tambah():
    # TODO Tambah Data Mahasiswa
    return

def Edit():
    #TODO Edit Data Mahasiswa
    #Ini diedit oleh Afad
    return

def Hapus():
    #TODO Hapus Data Mahasiswa
    return

def Cari():
    #TODO Cari Data Mahasiswa
    return

def Urutkan():
    #TODO Urutkan Data Mahasiswa
    return

"""
-Menu - Afad
-Edit (Nama) -Afad

-sorting (berdasarkan nim) -Kevin

-Buat(Nim, Nama) -Noor Alam

-Hapus(berdasarkan Nim) -Althafia

-searching (berdasarkan nim/nama) -Rezky
"""

Mahasiswa_Nama = []
Mahasiswa_Nim = []

while True:
    print("=" * 30)
    print("==== Pilihan ====")
    print("1. Lihat Data Mahasiswa")
    print("2. Tambah Data Mahasiswa")
    print("3. Edit Data Mahasiswa")
    print("4. Hapus Data Mahasiswa")
    print("5. Cari Data Mahasiswa")
    print("6. Urutkan Data Mahasiswa")
    print("7. Keluar")

    pilihan = input("Pilihan Anda: ")
    if pilihan == "1":
        Lihat()
    elif pilihan == "2":
        Tambah()
    elif pilihan == "3":
        Edit()
    elif pilihan == "4":
        Hapus()
    elif pilihan == "5":
        Cari()
    elif pilihan == "6":
        Urutkan()
    elif pilihan == "7":
        print("Program berhenti")
        break
