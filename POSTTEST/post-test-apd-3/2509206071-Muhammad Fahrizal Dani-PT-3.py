data_nama = "Muhammad Fahrizal Dani"
data_nim = "2509106071"
data_ukt = 6000000

print("===================== LOGIN UKT =====================")
nama = input("Masukan Nama Lengkap Anda: ")
nim = input("Masukan Nim Anda: ")
print("=======================================================")

if nama == data_nama and nim == data_nim:
    print("================== DETAIL PEMBAYARAN ==================")
    print("data_ukt yang harus dibayar berjumlah : Rp. 6.000.000")
    print("=======================================================")
    print("Pilih metode pembayaran :")
    print("1. Lunas (Sekali Bayar): Biaya administrasi 1%.")
    print("2. Cicilan 2x per Semester: Biaya administrasi 5%.")
    print("3. Cicilan 4x per Semester: Biaya administrasi 8%.")
    print("4. Cicilan 6x per Semester: Biaya administrasi 12%.")
    metode_pembayaran = input("Metode pembayaran yang dipilih 1/2/3/4/ :")
    print("=======================================================")

    if metode_pembayaran == "1":
        fee = 0.01
        harga_total = (data_ukt + (data_ukt*fee))
        print("================== DETAIL PEMBAYARAN ==================")
        print(f"Jumlah yang harus dibayarkan : Rp {harga_total:,.0f}")
        print("=======================================================")

    elif metode_pembayaran == "2":
        fee = 0.05
        harga_total = (data_ukt + (data_ukt*fee))
        harga_cicilan = harga_total/2
        print("================== DETAIL PEMBAYARAN ==================")
        print(f"Jumlah yang harus dibayarkan : Rp {harga_total:,.0f}")
        print(f"Jumlah Cicilan 2x per Semester :Rp {harga_cicilan:,.0f}")
        print("=======================================================")

    elif metode_pembayaran == "3":
        fee = 0.08
        harga_total = (data_ukt + (data_ukt*fee))
        harga_cicilan = harga_total/4
        print("================== DETAIL PEMBAYARAN ==================")
        print(f"Jumlah yang harus dibayarkan : Rp {harga_total:,.0f}")
        print(f"Jumlah Cicilan 4x per Semester :Rp {harga_cicilan:,.0f}")
        print("=======================================================")
    
    elif metode_pembayaran == "4":
        fee = 0.12
        harga_total = (data_ukt + (data_ukt*fee))
        harga_cicilan = harga_total/6
        print("================== DETAIL PEMBAYARAN ==================")
        print(f"Jumlah yang harus dibayarkan : Rp {harga_total:,.0f}")
        print(f"Jumlah Cicilan 6x per Semester :Rp {harga_cicilan:,.0f}")
        print("=======================================================")

    else:
        print("Pilihan tidak valid!")

else:
    print("Nama/Nim Salah!")