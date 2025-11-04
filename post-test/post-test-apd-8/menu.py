from tampilan_ui import *
from autentikasi import *
from pesawat import *
from data_data import user_session

def menu_admin():
    while True:
        try:
            clear_screen()
            tampilkan_header(f"MENU ADMIN - {user_session['username']}")
            print("\n┌─────────────────────────────────────────────────────────────────────────────┐")
            print("│  1. Tambah Pesawat    2. Lihat Pesawat    3. Cari Pesawat                  │")
            print("│  4. Update Pesawat    5. Hapus Pesawat    6. Logout                        │")
            print("└─────────────────────────────────────────────────────────────────────────────┘")
            
            pil = input("\n» Pilih menu: ").strip()
            
            if pil == "1":
                clear_screen()
                tampilkan_header("➕ TAMBAH PESAWAT")
                print()
                nama = input("📝 Nama Pesawat  : ").strip()
                tipe = input("🏷️  Tipe Pesawat  : ").strip()
                harga = input("💰 Harga (Rp)    : ").strip()
                
                sukses, pesan = tambah_pesawat(nama, tipe, harga)
                print(f"\n{'✅' if sukses else '❌'} {pesan}")
                pause()
                
            elif pil == "2":
                clear_screen()
                tampilkan_header("📋 DAFTAR PESAWAT")
                print()
                tampilkan_daftar_pesawat()
                pause()
                
            elif pil == "3":
                clear_screen()
                tampilkan_header("🔍 CARI PESAWAT")
                print()
                keyword = input("🔎 Kata kunci (nama/tipe): ").strip()
                hasil = cari_pesawat(keyword) if keyword else {}
                print()
                tampilkan_hasil_pencarian(hasil)
                pause()
                
            elif pil == "4":
                clear_screen()
                tampilkan_header("✏️ UPDATE PESAWAT")
                print()
                tampilkan_daftar_pesawat()
                id_up = input("\n🆔 Masukkan ID pesawat: ").strip()
                
                if id_up.isdigit():
                    id_up = int(id_up)
                    p = get_pesawat(id_up)
                    
                    if p:
                        print("\n💡 Tekan Enter untuk skip (tidak mengubah)")
                        nama = input(f"📝 Nama [{p['nama']}]: ").strip()
                        tipe = input(f"🏷️  Tipe [{p['tipe']}]: ").strip()
                        harga = input(f"💰 Harga [{p['harga']}]: ").strip()
                        status = input(f"📊 Status [{p['status']}]: ").strip()
                        
                        sukses, pesan = update_pesawat(id_up, nama, tipe, harga, status)
                        print(f"\n{'✅' if sukses else '❌'} {pesan}")
                    else:
                        print("\n❌ ID tidak valid!")
                else:
                    print("\n❌ ID harus berupa angka!")
                pause()
                
            elif pil == "5":
                clear_screen()
                tampilkan_header("🗑️ HAPUS PESAWAT")
                print()
                tampilkan_daftar_pesawat()
                id_del = input("\n🆔 Masukkan ID pesawat: ").strip()
                
                if id_del.isdigit():
                    id_del = int(id_del)
                    p = get_pesawat(id_del)
                    
                    if p:
                        konfirmasi = input(f"\n⚠️  Hapus '{p['nama']}'? (y/n): ").lower()
                        if konfirmasi == 'y':
                            sukses, pesan = hapus_pesawat(id_del)
                            print(f"\n{'✅' if sukses else '❌'} {pesan}")
                        else:
                            print("\n❌ Penghapusan dibatalkan")
                    else:
                        print("\n❌ ID tidak valid!")
                else:
                    print("\n❌ ID harus berupa angka!")
                pause()
                
            elif pil == "6":
                logout_user()
                print("\n👋 Logout berhasil!")
                pause()
                break
                
        except Exception as e:
            print(f"Error: {e}")
            pause()

def menu_user():
    while True:
        try:
            clear_screen()
            tampilkan_header(f"MENU PENGGUNA - {user_session['username']}")
            print("\n┌─────────────────────────────────────────────────────────────────────────────┐")
            print("│  1. Lihat Pesawat    2. Cari Pesawat    3. Logout                          │")
            print("└─────────────────────────────────────────────────────────────────────────────┘")
            
            pil = input("\n» Pilih menu: ").strip()
            
            if pil == "1":
                clear_screen()
                tampilkan_header("📋 DAFTAR PESAWAT")
                print()
                tampilkan_daftar_pesawat()
                pause()
                
            elif pil == "2":
                clear_screen()
                tampilkan_header("🔍 CARI PESAWAT")
                print()
                keyword = input("🔎 Kata kunci (nama/tipe): ").strip()
                hasil = cari_pesawat(keyword) if keyword else {}
                print()
                tampilkan_hasil_pencarian_user(hasil)
                pause()
                
            elif pil == "3":
                logout_user()
                print("\n👋 Logout berhasil!")
                pause()
                break
                
        except Exception as e:
            print(f"Error: {e}")
            pause()

def menu_utama():
    while True:
        try:
            clear_screen()
            tampilkan_header("✈️ SISTEM MANAJEMEN DATA PESAWAT ✈️")
            print("\n┌─────────────────────────────────────────────────────────────────────────────┐")
            print("│  1. Login    2. Register    3. Keluar                                      │")
            print("└─────────────────────────────────────────────────────────────────────────────┘")
            
            pil = input("\n» Pilih menu: ").strip()
            
            if pil == "1":
                clear_screen()
                tampilkan_header("🔐 LOGIN")
                print()
                user = input("👤 Username: ").strip()
                pwd = input("🔑 Password: ").strip()
                
                valid, data = validasi_login(user, pwd)
                if valid:
                    login_user(user, data["role"])
                    print(f"\n✅ Login berhasil! Selamat datang, {user}!")
                    pause()
                    
                    if data["role"] == "admin":
                        menu_admin()
                    else:
                        menu_user()
                else:
                    print("\n❌ Login gagal! Username atau password salah.")
                    pause()
                    
            elif pil == "2":
                clear_screen()
                tampilkan_header("📝 REGISTER")
                print()
                user = input("👤 Username baru    : ").strip()
                pwd = input("🔑 Password         : ").strip()
                conf = input("🔑 Konfirmasi Pass  : ").strip()
                
                sukses, pesan = register_user(user, pwd, conf)
                print(f"\n{'✅' if sukses else '❌'} {pesan}")
                pause()
                
            elif pil == "3":
                clear_screen()
                print("\n" + "="*80)
                print("✈️  Terima kasih telah menggunakan Sistem Manajemen Data Pesawat! ✈️".center(80))
                print("="*80 + "\n")
                break
                
        except Exception as e:
            print(f"Error: {e}")
            pause()