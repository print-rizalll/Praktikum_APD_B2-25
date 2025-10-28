import os

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

user_session = {"username": None, "role": None}

def validasi_login(username, password):
    try:
        valid = username in users_db and users_db[username]["password"] == password
        data = users_db[username] if valid else None
        return valid, data
    except:
        return False, None

def cari_pesawat(keyword):
    try:
        hasil = {id: data for id, data in pesawat_db.items() 
                if keyword.lower() in data["nama"].lower() or keyword.lower() in data["tipe"].lower()}
        return hasil
    except:
        return {}

def hitung_total_pesawat():
    try:
        total = len(pesawat_db)
        nilai = sum(p["harga"] for p in pesawat_db.values())
        return total, nilai
    except:
        return 0, 0

def get_next_id():
    try:
        return max(pesawat_db.keys()) + 1 if pesawat_db else 1
    except:
        return 1

def hitung_total_harga_rekursif(data_list, index=0):
    try:
        if index >= len(data_list):
            return 0
        return data_list[index]["harga"] + hitung_total_harga_rekursif(data_list, index + 1)
    except:
        return 0

def tampilkan_pesawat_rekursif(data_items, index=0):
    try:
        if index >= len(data_items):
            return
        id_p, p = data_items[index]
        print(f"{id_p:<4} {p['nama']:<25} {p['tipe']:<15} Rp{p['harga']:>12,} {p['status']:<10}")
        tampilkan_pesawat_rekursif(data_items, index + 1)
    except:
        pass

def tampilkan_header(judul):
    print("=" * 60)
    print(judul.center(60))
    print("=" * 60)

def tampilkan_daftar_pesawat():
    try:
        if not pesawat_db:
            print("Tidak ada data pesawat.")
            return
        print(f"{'ID':<4} {'Nama':<25} {'Tipe':<15} {'Harga':<15} {'Status':<10}")
        print("-" * 75)
        data_items = list(pesawat_db.items())
        tampilkan_pesawat_rekursif(data_items)
        total = len(pesawat_db)
        data_list = list(pesawat_db.values())
        nilai = hitung_total_harga_rekursif(data_list)
        print(f"Total: {total} unit | Nilai: Rp{nilai:,}")
    except Exception as e:
        print(f"Error: {e}")

def menu_admin():
    while True:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            tampilkan_header(f"MENU ADMIN - {user_session['username']}")
            print("1. Tambah  2. Lihat  3. Cari  4. Update  5. Hapus  6. Logout")

            pil = input("\nPilih: ").strip()

            if pil == "1":
                os.system('cls' if os.name == 'nt' else 'clear')
                tampilkan_header("TAMBAH PESAWAT")
                nama = input("Nama: ").strip()
                tipe = input("Tipe: ").strip()
                harga = input("Harga: ").strip()
                
                if nama and tipe and harga.isdigit() and int(harga) > 0:
                    pesawat_db[get_next_id()] = {"nama": nama, "tipe": tipe, "harga": int(harga), "status": "Tersedia"}
                    print(f"Berhasil ditambahkan!")
                else:
                    print("Input tidak valid!")
                input("Enter...")
                
            elif pil == "2":
                os.system('cls' if os.name == 'nt' else 'clear')
                tampilkan_header("DAFTAR PESAWAT")
                tampilkan_daftar_pesawat()
                input("\nEnter...")
                
            elif pil == "3":
                os.system('cls' if os.name == 'nt' else 'clear')
                tampilkan_header("CARI PESAWAT")
                keyword = input("Kata kunci: ").strip()
                hasil = cari_pesawat(keyword) if keyword else {}
                
                if hasil:
                    print(f"{'ID':<4} {'Nama':<25} {'Tipe':<15} {'Harga':<15}")
                    print("-" * 60)
                    hasil_items = list(hasil.items())
                    tampilkan_pesawat_rekursif(hasil_items)
                else:
                    print("Tidak ditemukan.")
                input("\nEnter...")
                
            elif pil == "4":
                os.system('cls' if os.name == 'nt' else 'clear')
                tampilkan_header("UPDATE PESAWAT")
                tampilkan_daftar_pesawat()
                id_up = input("\nID: ").strip()
                
                if id_up.isdigit() and int(id_up) in pesawat_db:
                    p = pesawat_db[int(id_up)]
                    nama = input(f"Nama [{p['nama']}]: ").strip()
                    tipe = input(f"Tipe [{p['tipe']}]: ").strip()
                    harga = input(f"Harga [{p['harga']}]: ").strip()
                    status = input(f"Status [{p['status']}]: ").strip()
                    
                    if nama: p["nama"] = nama
                    if tipe: p["tipe"] = tipe
                    if harga.isdigit(): p["harga"] = int(harga)
                    if status: p["status"] = status
                    print("Berhasil diupdate!")
                else:
                    print("ID tidak valid!")
                input("Enter...")
                
            elif pil == "5":
                os.system('cls' if os.name == 'nt' else 'clear')
                tampilkan_header("HAPUS PESAWAT")
                tampilkan_daftar_pesawat()
                id_del = input("\nID: ").strip()
                
                if id_del.isdigit() and int(id_del) in pesawat_db:
                    nama = pesawat_db[int(id_del)]["nama"]
                    if input(f"Hapus '{nama}'? (y/n): ").lower() == 'y':
                        del pesawat_db[int(id_del)]
                        print("Berhasil dihapus!")
                else:
                    print("ID tidak valid!")
                input("Enter...")
                
            elif pil == "6":
                user_session["username"] = None
                user_session["role"] = None
                break
        except Exception as e:
            print(f"Error: {e}")
            input("Enter...")

def menu_pengguna():
    while True:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            tampilkan_header(f"MENU PENGGUNA - {user_session['username']}")
            print("1. Lihat  2. Cari  3. Logout")
            
            pil = input("\nPilih: ").strip()
            
            if pil == "1":
                os.system('cls' if os.name == 'nt' else 'clear')
                tampilkan_header("DAFTAR PESAWAT")
                tampilkan_daftar_pesawat()
                input("\nEnter...")
            elif pil == "2":
                os.system('cls' if os.name == 'nt' else 'clear')
                tampilkan_header("CARI PESAWAT")
                keyword = input("Kata kunci: ").strip()
                hasil = cari_pesawat(keyword) if keyword else {}
                
                if hasil:
                    print(f"{'ID':<4} {'Nama':<25} {'Tipe':<15}")
                    hasil_items = list(hasil.items())
                    tampilkan_pesawat_rekursif(hasil_items)
                else:
                    print("Tidak ditemukan.")
                input("\nEnter...")
            elif pil == "3":
                user_session["username"] = None
                user_session["role"] = None
                break
        except Exception as e:
            print(f"Error: {e}")
            input("Enter...")

def menu_utama():
    while True:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            tampilkan_header("SISTEM MANAJEMEN DATA PESAWAT")
            print("1. Login  2. Register  3. Keluar")
            
            pil = input("\nPilih: ").strip()
            
            if pil == "1":
                os.system('cls' if os.name == 'nt' else 'clear')
                tampilkan_header("LOGIN")
                user = input("Username: ").strip()
                pwd = input("Password: ").strip()
                
                valid, data = validasi_login(user, pwd)
                if valid:
                    user_session["username"] = user
                    user_session["role"] = data["role"]
                    print(f"Login berhasil!")
                    input("Enter...")
                    menu_admin() if data["role"] == "admin" else menu_pengguna()
                else:
                    print("Login gagal!")
                    input("Enter...")
                    
            elif pil == "2":
                os.system('cls' if os.name == 'nt' else 'clear')
                tampilkan_header("REGISTER")
                user = input("Username: ").strip()
                pwd = input("Password: ").strip()
                conf = input("Konfirmasi: ").strip()
                
                if user and pwd and pwd == conf and user not in users_db and len(pwd) >= 5:
                    users_db[user] = {"password": pwd, "role": "pengguna"}
                    print("Registrasi berhasil!")
                else:
                    print("Registrasi gagal! Cek input Anda.")
                input("Enter...")
                
            elif pil == "3":
                print("Terima kasih!")
                break
        except Exception as e:
            print(f"Error: {e}")
            input("Enter...")

if __name__ == "__main__":
    try:
        menu_utama()
    except KeyboardInterrupt:
        print("\n\nProgram dihentikan.")
    except Exception as e:
        print(f"\nError: {e}")