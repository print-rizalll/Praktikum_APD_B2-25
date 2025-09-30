harga = int(input("Masukan Harga : "))

if harga >= 100000:
    diskon = 0.20
elif harga >= 50000:
    diskon = 0.10
else:
    diskon = 0

total = harga - (harga * diskon)
print (total)