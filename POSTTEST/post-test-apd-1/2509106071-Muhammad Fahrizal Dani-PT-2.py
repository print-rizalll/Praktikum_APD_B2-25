nama = input("Masukan Nama Lengkap Anda: ")
nim = input("Masukan Nim Anda: ")

harga = int(input("Masukan harga makanan(Rp. ): "))

menu = ["Pecel Lele", "Mie Ayam", "Nasi Padang"]
persen_pajak = [5, 8, 10]

print("=" * 60)
print(f"{nama} Dengan Nim {nim} ingin membeli makanan seharga Rp{harga:,}")
print("=" * 60)

print("{:<15} {:<10} {:<15}".format("Menu", "Pajak", "Total Harga"))
print("-" * 60)

for i in range(len(menu)):
    pajak = harga * (persen_pajak[i] / 100)
    total = harga + pajak
    print("{:<15} {:<10} Rp{:<15,.0f}".format(menu[i], f"{persen_pajak[i]}%", total)) 
print("=" * 60)