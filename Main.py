students = []

def ReturnMenu():
    input("\ntekan enter untuk kembali ke menu utama")
    return

def view_mahasiswa():
    if students:
        print("Daftar mahasiswa:")
        for i in students:
            print(f"NIM: {i['nim']}, Nama: {i['nama']}, Jenis Kelamin: {i['gender']}")
    else:
        print("Belum ada mahasiswa yang terdaftar")
    ReturnMenu()

def add_mahasiswa(jumlah):
    for i in range(jumlah):
        nim = int(input("Masukkan NIM: "))
        mahasiswa = input("Masukkan Nama Mahasiswa: ")
        gender = input("Masukkan Jenis Kelamin: ")
        student = {
            "nim": nim,
            "nama": mahasiswa,
            "gender": gender
        }
        students.append(student)
        print(f"Mahasiswa dengan NIM {nim} telah ditambahkan\n")
    ReturnMenu()

def update_mahasiswa(nim):
    nama = input("Masukkan Nama Mahasiswa baru: ")
    for i in students:
        if i['nim'] == nim:
            i['nama'] = nama
            print(f"Mahasiswa dengan NIM {nim} telah diperbarui.")
            return
    print(f"Mahasiswa dengan NIM {nim} tidak ditemukan.")
    ReturnMenu()

def delete_mahasiswa(nim):
    #TODO: hapus data mahasiswa berdasarkan NIM
    ReturnMenu()

def searching_mahasiswa(nim):
    for i in students:
        if i['nim'] == nim:
            print(f"Mahasiswa dengan NIM {nim} ditemukan pada urutan ke {i+1}:")
            print(f"NIM: {i['nim']}, Nama: {i['nama']}, Jenis Kelamin: {i['gender']}")
            ReturnMenu()
            return
    print(f"Mahasiswa dengan NIM {nim} tidak ditemukan.")
    ReturnMenu()

def sorting_mahasiswa():
    n = len(students)
    for i in range(n):
        index = i
        for j in range(i+1, n):
            if students[j]['nim'] < students[index]['nim']:
                index = j
        students[i], students[index] = students[index], students[i]
    print("Mahasiswa diurutkan berdasarkan NIM.")
    view_mahasiswa()
    ReturnMenu()

while True:
    print("\n================== MENU UTAMA ==================")
    print("1. Tambah mahasiswa")
    print("2. Lihat daftar mahasiswa")
    print("3. Perbarui data mahasiswa")
    print("4. Hapus data mahasiswa")
    print("5. Cari mahasiswa")
    print("6. Urutkan mahasiswa berdasarkan NIM (Ascending)")
    print("7. Keluar")

    pilihan = input("Masukkan pilihan Anda (1-7): ")

    if pilihan == '1':
        jumlah = int(input("Masukkan jumlah mahasiswa yang akan ditambahkan: "))
        add_mahasiswa(jumlah)

    elif pilihan == '2':
        view_mahasiswa()

    elif pilihan == '3':
        nim = int(input("Masukkan NIM mahasiswa yang akan diperbarui: "))
        update_mahasiswa(nim)

    elif pilihan == '4':
        nim = int(input("Masukkan NIM mahasiswa yang akan dihapus: "))
        delete_mahasiswa(nim)

    elif pilihan == '5':
        nim = int(input("Masukkan NIM mahasiswa yang akan dicari: "))
        searching_mahasiswa(nim)

    elif pilihan == '6':
        sorting_mahasiswa()

    elif pilihan == '7':
        print("Program keluar.")
        break

    else:
        print("Pilihan tidak valid.")