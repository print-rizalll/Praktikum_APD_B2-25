data_nama = "Muhammad Fahrizal Dani"
data_nim = "2509106071"
kondisi_login = False

print("===== LOGIN INFORDEH =====")
for i in range(3):
    nama = input("Masukan Nama Lengkap : ")
    password = input("Masukan NIM : ")
    if nama == data_nama and password == data_nim:
        print("===== LOGIN BERHASIL =====")
        kondisi_login = True
        break
    else:
        print("Login Gagal Percobaan ke-", i+1)

if kondisi_login == False:
    print("===== Gagal login 3 kali, Program berhenti ===== ")

else:
    total_harga = 0
    ulang = True

    while ulang == True:
        print(" ")
        print("===== MENU FURNITUR =====")
        print("1. Sofa -  Rp 500.000/Per unit")
        print("2. Meja Belajar - Rp 250.000/Per unit")
        print("3. Rak Lemari - Rp 150.000/Per unit")
        print("4. Keluar")
        pilihan = input("Pilih menu [1-4]: ")

        if pilihan == "1":
            nama_barang = "Sofa"
            harga = 500000
            if total_harga >= 700000:
                diskon = 0.2
                diskontext = "Diskon 20%"
            elif total_harga >= 500000:
                diskon = 0.08
                diskontext = "Diskon 8%%"
            elif total_harga >= 150000:
                diskontext = "Bonus Kitchen Set Gratis!"
            else:
                diskontext = "Tidak Ada"
        elif pilihan == "2":
            nama_barang = "Meja Belajar"
            harga = 250000
            if total_harga >= 700000:
                diskon = 0.2
                diskontext = "Diskon 20%"
            elif total_harga >= 500000:
                diskon = 0.08
                diskontext = "Diskon 8%%"
            elif total_harga >= 150000:
                diskontext = "Bonus Kitchen Set Gratis!"
            else:
                diskontext = "Tidak Ada"
        elif pilihan == "3":
            nama_barang = "Rak Lemari"
            harga = 150000
            if total_harga >= 700000:
                diskon = 0.2
                diskontext = "Diskon 20%"
            elif total_harga >= 500000:
                diskon = 0.08
                diskontext = "Diskon 8%%"
            elif total_harga >= 150000:
                diskontext = "Bonus Kitchen Set Gratis!"
            else:
                diskontext = "Tidak Ada"
        elif pilihan == "4":
            ulang = False
            continue
        else:
            print("Pilihan tidak ada!\n")
            continue

        jumlah_barang = int(input("Masukan Jumlah Barang : "))

        subtotal_harga = 0

        for i in range(jumlah_barang):
            subtotal_harga = subtotal_harga + harga
            subtotal_diskon = subtotal_harga - (subtotal_harga * diskon)

        total_harga = total_harga + subtotal_harga

        print(" ")
        print("===== STRUK PEMBELIAN =====")
        print(f"Jenis Furnitur : {nama_barang}")
        print(f"Jumlah Unit : {jumlah_barang}")
        print(f"Total Harga : {total_harga:,.0f}")
        print(f"Bonus Diskon : {diskontext}")
