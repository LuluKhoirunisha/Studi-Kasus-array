# Deklarasi array untuk menyimpan angka
angka = []

# Meminta input Pengguna
for i in range(5):
    elemen = int(input(f"Masukan angka ke-{i+1}: "))
    angka.append(elemen)
    
# Menghitung frekuensi kemunculan
frekuensi = {}
for elemen in frekuensi:
    if elemen in frekuensi:
        frekuensi[elemen] += 1
    else:
        frekuensi[elemen] = 1
        
# Menampilkan hasil
for elemen, jumlah in frekuensi.item():
    print(f"Angka{elemen} muncul sebanyak {jumlah} kali.")