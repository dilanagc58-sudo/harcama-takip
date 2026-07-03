import json

harcamalar = []

def harcama_ekle():
    kategori = input("Kategori (örn: market, ulaşım, eğlence): ")
    tutar = float(input("Tutar (TL): "))
    harcamalar.append({"kategori": kategori, "tutar": tutar})
    print("Harcama eklendi!")

def harcamalari_goster():
    for harcama in harcamalar:
        print(harcama["kategori"], "-", harcama["tutar"], "TL")

def toplam_hesapla():
    toplam = 0
    for harcama in harcamalar:
        toplam = toplam + harcama["tutar"]
    print("Toplam harcama:", toplam, "TL")

def verileri_kaydet():
    with open("harcamalar.json", "w") as dosya:
        json.dump(harcamalar, dosya)

def verileri_yukle():
    global harcamalar
    try:
        with open("harcamalar.json", "r") as dosya:
            harcamalar = json.load(dosya)
    except FileNotFoundError:
        harcamalar = []

verileri_yukle()
while True:
    print("\n1. Harcama Ekle")
    print("2. Harcamaları Göster")
    print("3. Toplamı Göster")
    print("4. Çıkış")
    
    secim = input("Seçiminiz: ")
    
    if secim == "1":
        harcama_ekle()
    elif secim == "2":
        harcamalari_goster()
    elif secim == "3":
        toplam_hesapla()
    elif secim == "4":
        verileri_kaydet()
        print("Görüşürüz!")
        break
    else:
        print("Geçersiz seçim, tekrar dene.")