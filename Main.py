def Lihat(Nim, Nama):
    for i in range(len(Nim) == len(Nama)):
        print(f"{Nim[i]}, {Nama[i]}")
    return -1

def Tambah():
    # TODO Tambah Data Mahasiswa
    return

def Edit(Nim, Nama):
    Cari(Nim)
    if Cari(Nim) != -1:
        Nama[Cari(Nim)] = input("Nama baru: ")
    return -1

def Hapus():
    #TODO Hapus Data Mahasiswa
    return

def Cari():
def bubble_sort(Nama, Nim):
    for i in range(len(Nim)):
        for j in range(len(Nim) - i - 1):
            if str(Nim[j]).lower() > str(Nim[j+1]).lower():
                Nim[j], Nim[j+1] = Nim[j+1], Nim[j]
    return binary_search(Nama, Nim)

def binary_search(Nama, Nim):
    left = 0
    right = len(Nim) - 1

    while left <= right:
        mid = (left + right) // 2
        if str(Nim[mid]).lower() > Nama.lower():
            right = mid - 1
        elif str(Nim[mid]).lower() < Nama.lower():
            left = mid + 1
        else:
            print(Nim)
            print(f"Nim {Nama} berada pada baris {mid}")
            return mid

    print(f"Nim {Nama} tidak ditemukan")
    return -1

Nim = []
Nama = input("Masukkan nim: ")
bubble_sort(Nama, Nim)
    return

def Urutkan():
    #TODO Urutkan Data Mahasiswa
    return

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
