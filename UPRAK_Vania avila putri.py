print("program bangun datar")

print("1.balok")

panjang = int(input("masukan nilai panjang: "))
lebar = int(input("masukan nilai lebar: "))
tinggi =int(input("masukan nilai tinggi: "))


luas_balok = panjang * lebar * tinggi 

print("luas balok adalah: ", luas_balok)

print("2.tabung")

luas_alas_lingkaran = int(input("masukan nilai alas lingkaran: "))
tinggi = int(input("masukan nilai tinggi: "))

volume_ling = luas_alas_lingkaran * tinggi 

print("nilai volume tabung adalah:", volume_ling)

print("3.limas")

alas =int(input("masukan nilai alas: "))
tinggi = int(input("masukan nilai tinggi: "))
volume_1 = alas * tinggi 
print("volume limas adalah:", volume_1)

kursDolar = 14000
rupiah = float(input("masukan uang rupiah: "))
rupToDol = rupiah/ kursDolar 
dolDecimal = round(rupToDol, 2)
print("RP.",rupiah, "==> US$", dolDecimal)