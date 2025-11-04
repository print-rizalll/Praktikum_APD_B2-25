from data_data import pesawat_db

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

def tambah_pesawat(nama, tipe, harga):
    try:
        if not nama or not tipe:
            return False, "Nama dan tipe tidak boleh kosong!"
        
        if not harga.isdigit() or int(harga) <= 0:
            return False, "Harga harus berupa angka positif!"
        
        pesawat_db[get_next_id()] = {
            "nama": nama, 
            "tipe": tipe, 
            "harga": int(harga), 
            "status": "Tersedia"
        }
        return True, "Pesawat berhasil ditambahkan!"
    except Exception as e:
        return False, f"Error: {e}"

def update_pesawat(id_pesawat, nama=None, tipe=None, harga=None, status=None):
    try:
        if id_pesawat not in pesawat_db:
            return False, "ID pesawat tidak ditemukan!"
        
        p = pesawat_db[id_pesawat]
        
        if nama: p["nama"] = nama
        if tipe: p["tipe"] = tipe
        if harga and harga.isdigit(): p["harga"] = int(harga)
        if status: p["status"] = status
        
        return True, "Pesawat berhasil diupdate!"
    except Exception as e:
        return False, f"Error: {e}"

def hapus_pesawat(id_pesawat):
    try:
        if id_pesawat not in pesawat_db:
            return False, "ID pesawat tidak ditemukan!"
        
        nama = pesawat_db[id_pesawat]["nama"]
        del pesawat_db[id_pesawat]
        return True, f"Pesawat '{nama}' berhasil dihapus!"
    except Exception as e:
        return False, f"Error: {e}"

def get_pesawat(id_pesawat):
    return pesawat_db.get(id_pesawat, None)