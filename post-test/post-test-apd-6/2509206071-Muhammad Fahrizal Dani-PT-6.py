import os
users_db = [
    ["admin", "admin123", "admin"],
    ["user1", "user123", "pengguna"]

]
pesawat_db = [
    [1, "Boeing 737 MAX 8", "Komersial", 1250000000, "Tersedia"],
    [2, "Airbus A320neo", "Komersial", 1180000000, "Tersedia"],
    [3, "Cessna Citation X", "Jet Pribadi", 230000000, "Tersedia"],
    [4, "Gulfstream G700", "Jet Pribadi", 760000000, "Tersedia"],
    [5, "ATR 72-600", "Regional", 250000000, "Tersedia"],
    [6, "LM F-35 Lightning II", "Militer", 1850000000, "Tersedia"],
    [7, "Boeing 777-300ER", "Komersial", 1800000000, "Tersedia"],
    [8, "Airbus A350-1000", "Komersial", 1750000000, "Tersedia"],
    [9, "Dassault Falcon 8X", "Jet Pribadi", 580000000, "Tersedia"],
    [10, "Pilatus PC-24", "Jet Pribadi", 110000000, "Tersedia"],
    [11, "Embraer E195-E2", "Regional", 300000000, "Tersedia"],
    [12, "Sukhoi Superjet 100", "Regional", 270000000, "Tersedia"],
    [13, "Antonov An-225 Mriya", "Kargo", 2500000000, "Tersedia"],
    [14, "Boeing 747-8F", "Kargo", 1500000000, "Tersedia"],
    [15, "Airbus BelugaXL", "Kargo", 1200000000, "Tersedia"]
]

user_login = None
user_role = None

menu_login = True
while menu_login:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 60)
    print("SISTEM MANAJEMEN DATA PESAWAT")
    print("=" * 60)
    print("1. Login")
    print("2. Register")
    print("3. Keluar")

    pilihan_utama = input("\nPilih menu (1-3): ").strip()

    if pilihan_utama == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 60)
        print("LOGIN")
        print("=" * 60)

        username_input = input("Masukkan username: ").strip()
        password_input = input("Masukkan password: ").strip()

        login_berhasil = False
        for u in users_db:
            if u[0] == username_input and u[1] == password_input:
                user_login = u[0]
                user_role = u[2]
                login_berhasil = True
                break

        if login_berhasil:
            print(f"\nLogin berhasil! Selamat datang, {username_input}.")
            input("Tekan Enter untuk melanjutkan..")

            if user_role == "admin":
                menu_admin = True
                while menu_admin:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=" * 60)
                    print(f"MENU ADMIN - {user_login}")
                    print("=" * 60)
                    print("1. Tambah Pesawat")
                    print("2. Lihat Data Pesawat")
                    print("3. Update Data Pesawat")
                    print("4. Hapus Data Pesawat")
                    print("5. Logout")

                    pilihan_admin = input("\nPilih menu (1-5): ").strip()

                    if pilihan_admin == "1":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=== TAMBAH PESAWAT ===")
                        nama = input("Nama pesawat: ").strip()
                        tipe = input("Tipe pesawat: ").strip()
                        harga_str = input("Harga pesawat: ").strip()

                        if not harga_str.isdigit():
                            print("Harga harus berupa angka!")
                            input("Tekan Enter...")
                            continue

                        harga = int(harga_str)
                        id_baru = max([p[0] for p in pesawat_db]) + 1 if pesawat_db else 1
                        pesawat_db.append([id_baru, nama, tipe, harga, "Tersedia"])
                        print(f"Pesawat '{nama}' berhasil ditambahkan!")
                        input("Tekan Enter untuk kembali...")

                    elif pilihan_admin == "2":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=== DAFTAR PESAWAT ===")
                        if len(pesawat_db) == 0:
                            print("Belum ada data pesawat.")
                        else:
                            print(f"{'ID':<4} {'Nama':<25} {'Tipe':<15} {'Harga':<15} {'Status':<10}")
                            print("-" * 75)
                            for p in pesawat_db:
                                print(f"{p[0]:<4} {p[1]:<25} {p[2]:<15} Rp{p[3]:>12,} {p[4]:<10}")
                        input("\nTekan Enter untuk kembali...")

                    elif pilihan_admin == "3":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=== DAFTAR PESAWAT ===")
                        if len(pesawat_db) == 0:
                            print("Tidak ada data pesawat.")
                        else:
                            print(f"{'ID':<4} {'Nama':<25} {'Tipe':<15} {'Harga':<15} {'Status':<10}")
                            print("-" * 75)
                            for p in pesawat_db:
                                print(f"{p[0]:<4} {p[1]:<25} {p[2]:<15} Rp{p[3]:>12,} {p[4]:<10}")
                        print("=== UPDATE DATA PESAWAT ===")
                        if len(pesawat_db) == 0:
                            print("Belum ada data.")
                            input("Tekan Enter...")
                            continue
                        id_update = input("Masukkan ID pesawat yang akan diubah: ").strip()
                        if not id_update.isdigit():
                            print("Masukan harus berupa angka!")
                            input("Tekan Enter...")
                            continue
                        id_update = int(id_update)
                        found = False
                        for p in pesawat_db:
                            if p[0] == id_update:
                                found = True
                                nama_baru = input("Nama baru (Enter untuk skip): ").strip()
                                tipe_baru = input("Tipe baru (Enter untuk skip): ").strip()
                                harga_baru = input("Harga baru (Enter untuk skip): ").strip()
                                status_baru = input("Status baru (Enter untuk skip): ").strip()
                                if nama_baru: p[1] = nama_baru
                                if tipe_baru: p[2] = tipe_baru
                                if harga_baru.isdigit(): p[3] = int(harga_baru)
                                if status_baru: p[4] = status_baru
                                print("Data pesawat berhasil diubah!")
                                break
                        if not found:
                            print("ID tidak ditemukan!")
                        input("Tekan Enter untuk kembali...")

                    elif pilihan_admin == "4":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=== DAFTAR PESAWAT ===")
                        if len(pesawat_db) == 0:
                            print("Tidak ada data pesawat.")
                        else:
                            print(f"{'ID':<4} {'Nama':<25} {'Tipe':<15} {'Harga':<15} {'Status':<10}")
                            print("-" * 75)
                            for p in pesawat_db:
                                print(f"{p[0]:<4} {p[1]:<25} {p[2]:<15} Rp{p[3]:>12,} {p[4]:<10}")
                        print("=== HAPUS DATA PESAWAT ===")
                        id_hapus = input("Masukkan ID pesawat yang akan dihapus: ").strip()
                        if not id_hapus.isdigit():
                            print("Masukan harus berupa angka!")
                            input("Tekan Enter...")
                            continue
                        id_hapus = int(id_hapus)
                        found = False
                        for p in pesawat_db:
                            if p[0] == id_hapus:
                                nama = p[1]
                                found = True
                                break

                        if found:
                            pesawat_db = [p for p in pesawat_db if p[0] != id_hapus]
                            print(f"Pesawat '{nama}' berhasil dihapus!")
                        else:
                            print("ID tidak ditemukan.")  
                        input("Tekan Enter untuk kembali...")

                    elif pilihan_admin == "5":
                        user_login = None
                        user_role = None
                        menu_admin = False
                        print("Logout berhasil.")
                        input("Tekan Enter...")

                    else:
                        print("Pilihan tidak valid!")
                        input("Tekan Enter...")

            else:
                menu_user = True
                while menu_user:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=" * 60)
                    print(f"MENU PENGGUNA - {user_login}")
                    print("=" * 60)
                    print("1. Lihat Data Pesawat")
                    print("2. Logout")

                    pilihan_user = input("\nPilih menu (1-2): ").strip()

                    if pilihan_user == "1":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=== DAFTAR PESAWAT ===")
                        if len(pesawat_db) == 0:
                            print("Tidak ada data pesawat.")
                        else:
                            print(f"{'ID':<4} {'Nama':<25} {'Tipe':<15} {'Harga':<15} {'Status':<10}")
                            print("-" * 75)
                            for p in pesawat_db:
                                print(f"{p[0]:<4} {p[1]:<25} {p[2]:<15} Rp{p[3]:>12,} {p[4]:<10}")
                        input("\nTekan Enter untuk kembali...")

                    elif pilihan_user == "2":
                        user_login = None
                        user_role = None
                        menu_user = False
                        print("Logout berhasil.")
                        input("Tekan Enter...")

                    else:
                        print("Pilihan tidak valid!")
                        input("Tekan Enter...")

        else:
            print("Username atau password salah!")
            input("Tekan Enter untuk kembali...")

    elif pilihan_utama == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== REGISTER PENGGUNA BARU ===")
        username = input("Masukkan username: ").strip()
        password = input("Masukkan password: ").strip()
        confirm = input("Konfirmasi password: ").strip()
        if password != confirm:
            print("Password tidak cocok!")
        duplikat = False
        for u in users_db:
            if u[0] == username:
                duplikat = True
                break

        if duplikat:
            print("Username sudah terdaftar!")
        else:
            users_db.append([username, password, "pengguna"])
            print("Registrasi berhasil!")
        input("Tekan Enter untuk kembali...")

    elif pilihan_utama == "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Terima kasih telah menggunakan program ini!")
        menu_login = False

    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter...")

