#Fungsi
def ReturnMenu():
    input("\ntekan enter untuk ke menu utama")
    return

def view_mahasiswa():
    if mahasiswa:
        print("Daftar mahasiswa:")
        for data in mahasiswa:
            print(f"NIM: {data['nim']}, Nama: {data['nama']}, Jenis Kelamin: {data['gender']}")
    else:
        print("Belum ada mahasiswa yang terdaftar")
    ReturnMenu()

def tambah_mahasiswa(jumlah):
    for i in range(jumlah):
        nim = int(input("\nMasukkan NIM: "))
        nama = input("Masukkan Nama Mahasiswa: ")
        gender = input("Masukkan Jenis Kelamin: ")
        student = {
            "nim": nim,
            "nama": nama,
            "gender": gender
        }
        mahasiswa.append(student)
        print(f"Mahasiswa dengan NIM {nim} telah ditambahkan")
    ReturnMenu()

def update_mahasiswa(nim):
    nama = input("Masukkan Nama Mahasiswa baru: ")
    for data in mahasiswa:
        if data['nim'] == nim:
            data['nama'] = nama
            print(f"Mahasiswa dengan NIM {nim} telah diperbarui.")
            ReturnMenu()
            return
    print(f"Mahasiswa dengan NIM {nim} tidak ditemukan.")
    ReturnMenu()

def hapus_mahasiswa(nim):
    for i in range(len(mahasiswa)):
        if mahasiswa[i]['nim'] == nim:
            mahasiswa.pop(i)
            print(f"Mahasiswa dengan NIM {nim} telah dihapus.")
            ReturnMenu()
            return
    print(f"Mahasiswa dengan NIM {nim} tidak ditemukan.")
    ReturnMenu()

def cari_mahasiswa(nim):
    for data in mahasiswa:
        if data['nim'] == nim:
            print(f"Mahasiswa dengan NIM {nim}:")
            print(f"NIM: {data['nim']}, Nama: {data['nama']}, Jenis Kelamin: {data['gender']}")
            ReturnMenu()
            return
    print(f"Mahasiswa dengan NIM {nim} tidak ditemukan.")
    ReturnMenu()

def urutkan_mahasiswa():
    n = len(mahasiswa)
    for i in range(n):
        index = i
        for j in range(i+1, n):
            if mahasiswa[j]['nim'] < mahasiswa[index]['nim']:
                index = j
        mahasiswa[i], mahasiswa[index] = mahasiswa[index], mahasiswa[i]
    print("Mahasiswa telah diurutkan berdasarkan NIM.")
    view_mahasiswa()

#Array
mahasiswa = []

jumlah = int(input("Masukkan jumlah mahasiswa awal: "))
tambah_mahasiswa(jumlah)

# Menu Utama
while True:
    print("\n================== MENU UTAMA =====================")
    print("1. Tambah mahasiswa")
    print("2. Lihat daftar mahasiswa")
    print("3. Perbarui data mahasiswa")
    print("4. Hapus data mahasiswa")
    print("5. Cari mahasiswa")
    print("6. Urutkan mahasiswa berdasarkan NIM (Ascending)")
    print("7. Keluar")

    pilihan = input("Masukkan pilihan Anda (1-7): ")

    if pilihan == '1':
        jmh = int(input("Masukkan jumlah mahasiswa yang akan ditambahkan: "))
        tambah_mahasiswa(jmh)
    elif pilihan == '2':
        view_mahasiswa()

    elif pilihan == '3':
        nim = int(input("Masukkan NIM mahasiswa yang akan diperbarui: "))
        update_mahasiswa(nim)

    elif pilihan == '4':
        nim = int(input("Masukkan NIM mahasiswa yang akan dihapus: "))
        hapus_mahasiswa(nim)

    elif pilihan == '5':
        nim = int(input("Masukkan NIM mahasiswa yang akan dicari: "))
        cari_mahasiswa(nim)

    elif pilihan == '6':
        urutkan_mahasiswa()

    elif pilihan == '7':
        print("Program keluar.")
        break

    else:
        print("Pilihan tidak valid.")
        ReturnMenu()