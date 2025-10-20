import os

# ==========================
# DATABASE
# ==========================
users_db = {
    "admin": {"password": "admin123", "role": "admin"},
    "user1": {"password": "user123", "role": "pengguna"}
}

pesawat_db = {
    1: {"nama": "Boeing 737 MAX 8", "tipe": "Komersial", "harga": 1250000000, "status": "Tersedia"},
    2: {"nama": "Airbus A320neo", "tipe": "Komersial", "harga": 1180000000, "status": "Tersedia"},
    3: {"nama": "Cessna Citation X", "tipe": "Jet Pribadi", "harga": 230000000, "status": "Tersedia"},
    4: {"nama": "Gulfstream G700", "tipe": "Jet Pribadi", "harga": 760000000, "status": "Tersedia"},
    5: {"nama": "ATR 72-600", "tipe": "Regional", "harga": 250000000, "status": "Tersedia"},
    6: {"nama": "LM F-35 Lightning II", "tipe": "Militer", "harga": 1850000000, "status": "Tersedia"},
    7: {"nama": "Boeing 777-300ER", "tipe": "Komersial", "harga": 1800000000, "status": "Tersedia"},
    8: {"nama": "Airbus A350-1000", "tipe": "Komersial", "harga": 1750000000, "status": "Tersedia"},
    9: {"nama": "Dassault Falcon 8X", "tipe": "Jet Pribadi", "harga": 580000000, "status": "Tersedia"},
    10: {"nama": "Pilatus PC-24", "tipe": "Jet Pribadi", "harga": 110000000, "status": "Tersedia"},
    11: {"nama": "Embraer E195-E2", "tipe": "Regional", "harga": 300000000, "status": "Tersedia"},
    12: {"nama": "Sukhoi Superjet 100", "tipe": "Regional", "harga": 270000000, "status": "Tersedia"},
    13: {"nama": "Antonov An-225 Mriya", "tipe": "Kargo", "harga": 2500000000, "status": "Tersedia"},
    14: {"nama": "Boeing 747-8F", "tipe": "Kargo", "harga": 1500000000, "status": "Tersedia"},
    15: {"nama": "Airbus BelugaXL", "tipe": "Kargo", "harga": 1200000000, "status": "Tersedia"}
}

user_login = None
user_role = None

# ==========================
# PROGRAM UTAMA
# ==========================
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

    # ==========================
    # LOGIN
    # ==========================
    if pilihan_utama == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 60)
        print("LOGIN")
        print("=" * 60)

        username_input = input("Masukkan username: ").strip()
        password_input = input("Masukkan password: ").strip()

        if username_input in users_db and users_db[username_input]["password"] == password_input:
            user_login = username_input
            user_role = users_db[username_input]["role"]
            print(f"\nLogin berhasil! Selamat datang, {username_input}.")
            input("Tekan Enter untuk melanjutkan...")

            # ==========================
            # MENU ADMIN
            # ==========================
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

                    # Tambah
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
                        id_baru = max(pesawat_db.keys()) + 1 if pesawat_db else 1
                        pesawat_db[id_baru] = {"nama": nama, "tipe": tipe, "harga": harga, "status": "Tersedia"}
                        print(f"Pesawat '{nama}' berhasil ditambahkan!")
                        input("Tekan Enter untuk kembali...")

                    # Lihat
                    elif pilihan_admin == "2":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=== DAFTAR PESAWAT ===")
                        if not pesawat_db:
                            print("Belum ada data pesawat.")
                        else:
                            print(f"{'ID':<4} {'Nama':<25} {'Tipe':<15} {'Harga':<15} {'Status':<10}")
                            print("-" * 75)
                            for id_p, p in pesawat_db.items():
                                print(f"{id_p:<4} {p['nama']:<25} {p['tipe']:<15} Rp{p['harga']:>12,} {p['status']:<10}")
                        input("\nTekan Enter untuk kembali...")

                    # Update
                    elif pilihan_admin == "3":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=== UPDATE DATA PESAWAT ===")
                        if not pesawat_db:
                            print("Belum ada data.")
                            input("Tekan Enter...")
                            continue
                        id_update = input("Masukkan ID pesawat yang akan diubah: ").strip()
                        if not id_update.isdigit():
                            print("Masukan harus berupa angka!")
                            input("Tekan Enter...")
                            continue
                        id_update = int(id_update)
                        if id_update in pesawat_db:
                            p = pesawat_db[id_update]
                            nama_baru = input("Nama baru (Enter untuk skip): ").strip()
                            tipe_baru = input("Tipe baru (Enter untuk skip): ").strip()
                            harga_baru = input("Harga baru (Enter untuk skip): ").strip()
                            status_baru = input("Status baru (Enter untuk skip): ").strip()
                            if nama_baru: p["nama"] = nama_baru
                            if tipe_baru: p["tipe"] = tipe_baru
                            if harga_baru.isdigit(): p["harga"] = int(harga_baru)
                            if status_baru: p["status"] = status_baru
                            print("Data pesawat berhasil diubah!")
                        else:
                            print("ID tidak ditemukan!")
                        input("Tekan Enter untuk kembali...")

                    # Hapus
                    elif pilihan_admin == "4":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=== HAPUS DATA PESAWAT ===")
                        id_hapus = input("Masukkan ID pesawat yang akan dihapus: ").strip()
                        if not id_hapus.isdigit():
                            print("Masukan harus berupa angka!")
                            input("Tekan Enter...")
                            continue
                        id_hapus = int(id_hapus)
                        if id_hapus in pesawat_db:
                            nama = pesawat_db[id_hapus]["nama"]
                            del pesawat_db[id_hapus]
                            print(f"Pesawat '{nama}' berhasil dihapus!")
                        else:
                            print("ID tidak ditemukan.")
                        input("Tekan Enter untuk kembali...")

                    # Logout
                    elif pilihan_admin == "5":
                        user_login = None
                        user_role = None
                        menu_admin = False
                        print("Logout berhasil.")
                        input("Tekan Enter...")

                    else:
                        print("Pilihan tidak valid!")
                        input("Tekan Enter...")

            # ==========================
            # MENU PENGGUNA
            # ==========================
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
                        if not pesawat_db:
                            print("Tidak ada data pesawat.")
                        else:
                            print(f"{'ID':<4} {'Nama':<25} {'Tipe':<15} {'Harga':<15} {'Status':<10}")
                            print("-" * 75)
                            for id_p, p in pesawat_db.items():
                                print(f"{id_p:<4} {p['nama']:<25} {p['tipe']:<15} Rp{p['harga']:>12,} {p['status']:<10}")
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

    # ==========================
    # REGISTER
    # ==========================
    elif pilihan_utama == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== REGISTER PENGGUNA BARU ===")
        username = input("Masukkan username: ").strip()
        password = input("Masukkan password: ").strip()
        confirm = input("Konfirmasi password: ").strip()
        if password != confirm:
            print("Password tidak cocok!")
        elif username in users_db:
            print("Username sudah terdaftar!")
        else:
            users_db[username] = {"password": password, "role": "pengguna"}
            print("Registrasi berhasil!")
        input("Tekan Enter untuk kembali...")

    # ==========================
    # KELUAR
    # ==========================
    elif pilihan_utama == "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Terima kasih telah menggunakan program ini!")
        menu_login = False

    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter...")
