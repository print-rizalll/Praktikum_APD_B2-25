# Daftar_buku = {
# "Buku1" : "Bumi Manusia",
# "Buku2" : "Laut Bercerita"
# }

# for key in Daftar_buku:
#     print(key)

# Biodata = {
#     "Nama" : "Ananda Daffa Harahap",
#     "NIM" : 2409106050,
#     "KRS" : ["Pemrograman Web", "Struktur Data", "Basis Data", "Algoritma"],
#     "Mahasiswa_Aktif" : True,
#     "Social Media" : {"Instagram" : "daffahrhap"}
# }

# print(Biodata.get("KRS")[0:1:3])

# Nilai = {
#     "Matematika": 80,
#     "B. Indonesia": 90,
#     "B. Inggris": 81,
#     "Kimia": 78,
#     "Fisika": 80
# }
# # Tanpa menggunakan items()
# for i in Nilai:
#     print(i)
# print("") # pemisah

# for i, j in Nilai.items():
#     print(f"Nilai {i} anda adalah {j}")

# Film = {
# "Avenger Endgame" : "Action",
# "Sherlock Holmes" : "Mystery",
# "The Conjuring" : "Horror"
# }
# print(Film)

# Film["Godzila"] = "Action"
# print(Film)

# data = {
# "Nama" : "Daffa",
# "Umur" : 19,
# "Jurusan" : "Informatika"
# }
#Sebelum Dihapus
# print(data)
# del data["Nama"]
# #Setelah diubah


# print(data)

# print(data.get("Nama"))

# cache = data.pop("Nama")
# #Setelah dihapus
# print(data)
# #memanggil data yang telah dihapus pada dictionary
# print(data.get("Nama"))
# #memanggil data yang telah dihapus pada variabel cache
# print(cache)

# data.clear()
# #Setelah dihapus
# print(data)

# buku = {
# "Buku1" : "Bumi Manusia",
# "Buku2" : "Laut Bercerita"
# }
# pinjam = buku.copy()

# print("Dictionary yang telah disalin : ", pinjam)
# print("Dictionary asli : ", buku)

# key = "apel", "jeruk", "mangga"
# value = 1

# buah = dict.fromkeys(key, value)

# print(buah)


Nilai = {
"Matematika" : 80,
"B. Indonesia" : 90,
"B. Inggris" : 81,
"Kimia" : 78,
"Fisika" : 80
}
#menggunakan keys
for i in Nilai.keys():
    print(i)
print("")

for i in Nilai.values():
    print(i)







