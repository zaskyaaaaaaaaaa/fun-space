def luas_segitiga():
    a = int(input("Masukkan alas segitiga: "))
    t = int(input("Masukkan tinggi segitiga: "))
    luas = a * t / 2
    print("Luas segitiga adalah: ", luas)

luas_segitiga()

def luas_persegi_panjang():
    p = int(input("Masukkan panjang persegi: "))
    l = int(input("Masukkan lebar persegi: "))
    luas = p * l 
    print("Luas persegi adalah: ", luas)

luas_persegi_panjang()

def luas_linkaran():
    r = int(input("Masukkan jari-jari linkaran: "))
    luas = 3.14 * r * r
    print("Luas lingkaran adalah: " , luas)

luas_linkaran()