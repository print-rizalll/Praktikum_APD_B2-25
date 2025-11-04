import os
from prettytable import PrettyTable
from data_data import pesawat_db
from pesawat import hitung_total_pesawat

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_header(judul):
    print("=" * 80)
    print(judul.center(80))
    print("=" * 80)

def tampilkan_daftar_pesawat():
    try:
        if not pesawat_db:
            print("Tidak ada data pesawat.")
            return
        
        table = PrettyTable()
        table.field_names = ["ID", "Nama Pesawat", "Tipe", "Harga (Rp)", "Status"]
        
        table.align["ID"] = "c"
        table.align["Nama Pesawat"] = "l"
        table.align["Tipe"] = "l"
        table.align["Harga (Rp)"] = "r"
        table.align["Status"] = "c"
        
        for id_p, p in pesawat_db.items():
            table.add_row([
                id_p,
                p['nama'],
                p['tipe'],
                f"{p['harga']:,}",
                p['status']
            ])
        
        print(table)
        
        total, nilai = hitung_total_pesawat()
        print(f"\n{'='*80}")
        print(f"Total Pesawat: {total} unit | Total Nilai: Rp {nilai:,}")
        print(f"{'='*80}")
        
    except Exception as e:
        print(f"Error: {e}")

def tampilkan_hasil_pencarian(hasil):
    if hasil:
        table = PrettyTable()
        table.field_names = ["ID", "Nama Pesawat", "Tipe", "Harga (Rp)"]
        
        table.align["ID"] = "c"
        table.align["Nama Pesawat"] = "l"
        table.align["Tipe"] = "l"
        table.align["Harga (Rp)"] = "r"
        
        for id_p, p in hasil.items():
            table.add_row([
                id_p,
                p['nama'],
                p['tipe'],
                f"{p['harga']:,}"
            ])
        
        print(table)
        print(f"\nDitemukan {len(hasil)} pesawat")
    else:
        print("❌ Tidak ditemukan.")

def tampilkan_hasil_pencarian_user(hasil):
    if hasil:
        table = PrettyTable()
        table.field_names = ["ID", "Nama Pesawat", "Tipe"]
        
        table.align["ID"] = "c"
        table.align["Nama Pesawat"] = "l"
        table.align["Tipe"] = "l"
        
        for id_p, p in hasil.items():
            table.add_row([
                id_p,
                p['nama'],
                p['tipe']
            ])
        
        print(table)
        print(f"\nDitemukan {len(hasil)} pesawat")
    else:
        print("❌ Tidak ditemukan.")

def pause():
    input("\nTekan Enter untuk melanjutkan...")