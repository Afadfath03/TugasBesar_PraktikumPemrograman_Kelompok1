jml = int(input("Masukkan jumlah mahasiswa: "))
print()

# inisiasi array
array_of_mhs = []

# perulangan sesuai input jumlah
for i in range(jml): 
    print(f"Mahasiswa ke-{i+1}")
    # Masukkan nama dan nim
    nama = input("Masukkan nama: ")
    nim = input("Masukkan nim: ")
    print()
    # nama dan nim dimasukkan ke dalam dictionary
    mhs = {"nama": nama, "nim":nim}

    # dictonary dimasukkan ke dalam array
    array_of_mhs.append(mhs)

print("============ DATA MAHASISWA ===========")
# perulangan sesuai jumlah array
for i in range(len(array_of_mhs)):
    # masukkan value dictionary dari dalam array ke variabel nama dan nim
    nama = array_of_mhs[i]["nama"]
    nim = array_of_mhs[i]["nim"]
    # print nama dan nim
    print(f"Mahasiswa ke-{i+1}")
    print(f"Nama\t: {nama}")
    print(f"NIM\t: {nim}\n")
