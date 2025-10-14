import os

# Database pengguna: [username, password, role]
users_db = [
    ["admin", "admin123", "admin"],
    ["user1", "user123", "pengguna"]
]

# Database pesawat: [[id, nama_pesawat, tipe, harga, status, pembeli, tanggal_penjualan]]
pesawat_db = [
    [1, "Boeing 737 MAX 8", "Komersial", 1250000000, "Tersedia", "", ""],
    [2, "Airbus A320neo", "Komersial", 1180000000, "Tersedia", "", ""],
    [3, "Cessna Citation X", "Jet Pribadi", 230000000, "Tersedia", "", ""],
    [4, "Gulfstream G700", "Jet Pribadi", 760000000, "Tersedia", "", ""],
    [5, "ATR 72-600", "Regional", 250000000, "Tersedia", "", ""],
    [6, "LM F-35 Lightning II", "Militer", 1850000000, "Tersedia", "", ""],
    [7, "Boeing 777-300ER", "Komersial", 1800000000, "Tersedia", "", ""],
    [8, "Airbus A350-1000", "Komersial", 1750000000, "Tersedia", "", ""],
    [9, "Dassault Falcon 8X", "Jet Pribadi", 580000000, "Tersedia", "", ""],
    [10, "Pilatus PC-24", "Jet Pribadi", 110000000, "Tersedia", "", ""],
    [11, "Embraer E195-E2", "Regional", 300000000, "Tersedia", "", ""],
    [12, "Sukhoi Superjet 100", "Regional", 270000000, "Tersedia", "", ""],
    [13, "Antonov An-225 Mriya", "Kargo", 2500000000, "Tersedia", "", ""],
    [14, "Boeing 747-8F", "Kargo", 1500000000, "Tersedia", "", ""],
    [15, "Airbus BelugaXL", "Kargo", 1200000000, "Tersedia", "", ""]
]
user_login = None
user_role = None

# MAIN PROGRAM
menu_login = True
while menu_login:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 60)
    print("SISTEM MANAJEMEN PENJUALAN PESAWAT")
    print("=" * 60)
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    
    pilihan_utama = input("\nPilih menu (1-3): ").strip()
    
    if pilihan_utama == "1":
        # LOGIN
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 60)
        print("LOGIN")
        print("=" * 60)
        
        username_input = input("Masukkan username: ").strip()
        password_input = input("Masukkan password: ").strip()
        
        login_berhasil = False
        for i in range(len(users_db)):
            if users_db[i][0] == username_input and users_db[i][1] == password_input:
                user_login = username_input
                user_role = users_db[i][2]
                login_berhasil = True
                break
        
        if login_berhasil:
            print(f"Login berhasil! Selamat datang, {username_input}")
            input("Tekan Enter untuk melanjutkan...")
            
            # MENU SESUAI ROLE
            if user_role == "admin":
                menu_admin_aktif = True
                while menu_admin_aktif:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=" * 60)
                    print(f"MENU ADMIN - {user_login}")
                    print("=" * 60)
                    print("1. Tambah Pesawat Baru")
                    print("2. Lihat Semua Pesawat")
                    print("3. Update Data Pesawat")
                    print("4. Hapus Data Pesawat")
                    print("5. Laporan Penjualan")
                    print("6. Logout")
                    
                    pilihan_admin = input("\nPilih menu (1-6): ").strip()
                    
                    if pilihan_admin == "1":
                        # TAMBAH PESAWAT
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=" * 60)
                        print("TAMBAH PESAWAT BARU")
                        print("=" * 60)
                        
                        nama = input("Nama pesawat: ").strip()
                        if len(nama) == 0:
                            print("Masukan tidak boleh kosong!")
                            input("Tekan Enter untuk kembali...")
                            continue
                        
                        tipe = input("Tipe pesawat: ").strip()
                        if len(tipe) == 0:
                            print("Masukan tidak boleh kosong!")
                            input("Tekan Enter untuk kembali...")
                            continue
                        
                        harga_str = input("Harga pesawat: ").strip()
                        if len(harga_str) == 0:
                            print("Masukan tidak boleh kosong!")
                            input("Tekan Enter untuk kembali...")
                            continue
                        
                        if not harga_str.isdigit():
                            print("Hanya angka yang diperbolehkan!")
                            input("Tekan Enter untuk kembali...")
                            continue
                        
                        harga = int(harga_str)
                        
                        if harga < 0:
                            print("Harga tidak boleh negatif!")
                            input("Tekan Enter untuk kembali...")
                            continue
                        
                        if len(pesawat_db) == 0:
                            id_baru = 1
                        else:
                            max_id = max(p[0] for p in pesawat_db)
                            id_baru = max_id + 1
                        
                        pesawat_db.append([id_baru, nama, tipe, harga, "Tersedia", "-", "-"])
                        print(f"Pesawat berhasil ditambahkan dengan ID: {id_baru}")
                        input("Tekan Enter untuk kembali...")
                    
                    elif pilihan_admin == "2":
                        # LIHAT SEMUA PESAWAT
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=" * 60)
                        print("DAFTAR PESAWAT")
                        print("=" * 60)
                        
                        if len(pesawat_db) == 0:
                            print("Tidak ada data pesawat.")
                        else:
                            print(f"{'ID':<4} {'Nama':<25} {'Tipe':<15} {'Harga':<15} {'Status':<12} {'Pembeli':<20} {'Tanggal':<12}")
                            print("-" * 110)
                            for pesawat in pesawat_db:
                                print(f"{pesawat[0]:<4} {pesawat[1]:<25} {pesawat[2]:<15} Rp{pesawat[3]:>12,} {pesawat[4]:<12} {pesawat[5]:<20} {pesawat[6]:<12}")
                        
                        input("\nTekan Enter untuk kembali...")
                    
                    elif pilihan_admin == "3":
                        # UPDATE DATA PESAWAT
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=" * 60)
                        print("UPDATE DATA PESAWAT")
                        print("=" * 60)
                        
                        if len(pesawat_db) == 0:
                            print("Tidak ada data pesawat untuk diupdate.")
                            input("Tekan Enter untuk kembali...")
                            continue
                        
                        print(f"{'ID':<4} {'Nama':<25} {'Tipe':<15} {'Harga':<15} {'Status':<12}")
                        print("-" * 75)
                        for pesawat in pesawat_db:
                            print(f"{pesawat[0]:<4} {pesawat[1]:<25} {pesawat[2]:<15} Rp{pesawat[3]:>12,} {pesawat[4]:<12}")
                        
                        id_update_str = input("\nMasukkan ID pesawat yang akan diupdate: ").strip()
                        if not id_update_str.isdigit():
                            print("Masukan tidak valid!")
                            input("Tekan Enter untuk kembali...")
                            continue
                        
                        id_update = int(id_update_str)
                        pesawat_found = False
                        
                        for pesawat in pesawat_db:
                            if pesawat[0] == id_update:
                                pesawat_found = True
                                print(f"\nData saat ini: {pesawat[1]} | {pesawat[2]} | Rp{pesawat[3]:,} | {pesawat[4]}")
                                
                                nama_baru = input("Nama pesawat baru (Enter untuk skip): ").strip()
                                if len(nama_baru) > 0:
                                    pesawat[1] = nama_baru
                                
                                tipe_baru = input("Tipe pesawat baru (Enter untuk skip): ").strip()
                                if len(tipe_baru) > 0:
                                    pesawat[2] = tipe_baru
                                
                                harga_str_baru = input("Harga pesawat baru (Enter untuk skip): ").strip()
                                if len(harga_str_baru) > 0:
                                    if not harga_str_baru.isdigit():
                                        print("Harga harus berupa angka!")
                                        input("Tekan Enter untuk kembali...")
                                        break
                                    harga_baru = int(harga_str_baru)
                                    pesawat[3] = harga_baru
                                
                                print("Data pesawat berhasil diupdate!")
                                break
                        
                        if not pesawat_found:
                            print("ID pesawat tidak ditemukan!")
                        
                        input("Tekan Enter untuk kembali...")
                    
                    elif pilihan_admin == "4":
                        # HAPUS DATA PESAWAT
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=" * 60)
                        print("HAPUS DATA PESAWAT")
                        print("=" * 60)
                        
                        if len(pesawat_db) == 0:
                            print("Tidak ada data pesawat untuk dihapus.")
                            input("Tekan Enter untuk kembali...")
                            continue
                        
                        print(f"{'ID':<4} {'Nama':<25} {'Tipe':<15} {'Harga':<15}")
                        print("-" * 75)
                        for pesawat in pesawat_db:
                            print(f"{pesawat[0]:<4} {pesawat[1]:<25} {pesawat[2]:<15} Rp{pesawat[3]:>12,}")
                        
                        id_hapus_str = input("\nMasukkan ID pesawat yang akan dihapus: ").strip()
                        if not id_hapus_str.isdigit():
                            print("Masukan tidak valid!")
                            input("Tekan Enter untuk kembali...")
                            continue
                        
                        id_hapus = int(id_hapus_str)
                        index_hapus = next((i for i, p in enumerate(pesawat_db) if p[0] == id_hapus), -1)
                        
                        if index_hapus >= 0:
                            nama_pesawat = pesawat_db[index_hapus][1]
                            pesawat_db.pop(index_hapus)
                            print(f"Pesawat '{nama_pesawat}' berhasil dihapus!")
                        else:
                            print("ID pesawat tidak ditemukan!")
                        
                        input("Tekan Enter untuk kembali...")
                    
                    elif pilihan_admin == "5":
                        # LAPORAN PENJUALAN
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=" * 60)
                        print("LAPORAN PENJUALAN")
                        print("=" * 60)
                        
                        pesawat_terjual = [p for p in pesawat_db if p[4] == "Terjual"]
                        total_harga = sum(p[3] for p in pesawat_terjual)
                        
                        if len(pesawat_terjual) == 0:
                            print("Belum ada pesawat yang terjual.")
                        else:
                            print(f"\n{'ID':<4} {'Nama':<25} {'Pembeli':<20} {'Harga':<15} {'Tanggal':<12}")
                            print("-" * 78)
                            for pesawat in pesawat_terjual:
                                print(f"{pesawat[0]:<4} {pesawat[1]:<25} {pesawat[5]:<20} Rp{pesawat[3]:>12,} {pesawat[6]:<12}")
                            print("-" * 78)
                            print(f"Total penjualan: Rp{total_harga:,}")
                            print(f"Jumlah pesawat terjual: {len(pesawat_terjual)}")
                        
                        input("\nTekan Enter untuk kembali...")
                    
                    elif pilihan_admin == "6":
                        user_login = None
                        user_role = None
                        print("Logout berhasil!")
                        input("Tekan Enter untuk kembali...")
                        menu_admin_aktif = False
            
            else:
                # MENU PENGGUNA
                menu_pengguna_aktif = True
                while menu_pengguna_aktif:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=" * 60)
                    print(f"MENU PENGGUNA - {user_login}")
                    print("=" * 60)
                    print("1. Lihat Semua Pesawat")
                    print("2. Proses Penjualan Pesawat")
                    print("3. Logout")
                    
                    pilihan_pengguna = input("\nPilih menu (1-3): ").strip()
                    
                    if pilihan_pengguna == "1":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=" * 60)
                        print("DAFTAR PESAWAT")
                        print("=" * 60)
                        
                        if len(pesawat_db) == 0:
                            print("Tidak ada data pesawat.")
                        else:
                            print(f"{'ID':<4} {'Nama':<25} {'Tipe':<15} {'Harga':<15} {'Status':<12} {'Pembeli':<20} {'Tanggal':<12}")
                            print("-" * 110)
                            for pesawat in pesawat_db:
                                print(f"{pesawat[0]:<4} {pesawat[1]:<25} {pesawat[2]:<15} Rp{pesawat[3]:>12,} {pesawat[4]:<12} {pesawat[5]:<20} {pesawat[6]:<12}")
                        
                        input("\nTekan Enter untuk kembali...")
                    
                    elif pilihan_pengguna == "2":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=" * 60)
                        print("PROSES PENJUALAN PESAWAT")
                        print("=" * 60)
                        
                        if len(pesawat_db) == 0:
                            print("Tidak ada data pesawat.")
                            input("Tekan Enter untuk kembali...")
                            continue
                        
                        print(f"{'ID':<4} {'Nama':<25} {'Tipe':<15} {'Harga':<15} {'Status':<12}")
                        print("-" * 75)
                        for pesawat in pesawat_db:
                            print(f"{pesawat[0]:<4} {pesawat[1]:<25} {pesawat[2]:<15} Rp{pesawat[3]:>12,} {pesawat[4]:<12}")
                        
                        id_jual_str = input("\nMasukkan ID pesawat yang akan dijual: ").strip()
                        if not id_jual_str.isdigit():
                            print("Masukan tidak valid!")
                            input("Tekan Enter untuk kembali...")
                            continue
                        
                        id_jual = int(id_jual_str)
                        pesawat_found = False
                        
                        for pesawat in pesawat_db:
                            if pesawat[0] == id_jual:
                                pesawat_found = True
                                if pesawat[4] == "Terjual":
                                    print("Pesawat ini sudah terjual!")
                                    input("Tekan Enter untuk kembali...")
                                    break
                                
                                pembeli = input("Nama pembeli: ").strip()
                                tanggal = input("Tanggal penjualan (YYYY-MM-DD): ").strip()
                                if len(pembeli) == 0 or len(tanggal) == 0:
                                    print("Masukan tidak boleh kosong!")
                                    input("Tekan Enter untuk kembali...")
                                    break
                                
                                pesawat[4] = "Terjual"
                                pesawat[5] = pembeli
                                pesawat[6] = tanggal
                                
                                print(f"Pesawat '{pesawat[1]}' berhasil dijual kepada {pembeli}!")
                                break
                        
                        if not pesawat_found:
                            print("ID pesawat tidak ditemukan!")
                        
                        input("Tekan Enter untuk kembali...")
                    
                    elif pilihan_pengguna == "3":
                        user_login = None
                        user_role = None
                        print("Logout berhasil!")
                        input("Tekan Enter untuk kembali...")
                        menu_pengguna_aktif = False
        
        else:
            print("Username atau password salah!")
            input("Tekan Enter untuk kembali...")
    
    elif pilihan_utama == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 60)
        print("REGISTER PENGGUNA BARU")
        print("=" * 60)
        
        username_reg = input("Masukkan username: ").strip()
        if len(username_reg) == 0:
            print("Masukan tidak boleh kosong!")
            input("Tekan Enter untuk kembali...")
            continue
        
        if any(u[0] == username_reg for u in users_db):
            print("Username sudah terdaftar!")
            input("Tekan Enter untuk kembali...")
            continue
        
        password_reg = input("Masukkan password: ").strip()
        if len(password_reg) < 6:
            print("Password minimal 6 karakter!")
            input("Tekan Enter untuk kembali...")
            continue
        
        confirm_password_reg = input("Konfirmasi password: ").strip()
        if password_reg != confirm_password_reg:
            print("Password tidak cocok!")
            input("Tekan Enter untuk kembali...")
            continue
        
        users_db.append([username_reg, password_reg, "pengguna"])
        print("Register berhasil! Silakan login.")
        input("Tekan Enter untuk kembali...")
    
    elif pilihan_utama == "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 60)
        print("TERIMA KASIH")
        print("=" * 60)
        print("Program berakhir. Sampai jumpa!")
        menu_login = False
    
    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter untuk kembali...")
