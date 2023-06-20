def selection_sort(mahasiswa):
    n = len(mahasiswa)
    
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if mahasiswa[j]["NIM"] < mahasiswa[min_index]["NIM"]:
                min_index = j
        mahasiswa[i], mahasiswa[min_index] = mahasiswa[min_index], mahasiswa[i]
    return mahasiswa

data = [[2211104001, 2211104002, 2211104003, 2211104004, 2211104005, 2211104006, 
         2211104007, 2211104008, 2211104009, 2211104010, 2211104011, 2211104012, 
         2211104013, 2211104014, 2211104015, 2211104016, 2211104017, 2211104018, 
         2211104019, 2211104020, 2211104021, 2211104022, 2211104023, 2211104024, 
         2211104025, 2211104026, 2211104027, 2211104028, 2211104029, 2211104030, 
         2211104031, 2211104032, 2211104033, 2211104034, 2211104035]]
print(f"Before: {data}")
selection_sort(data)
print(f"After: {data}")
