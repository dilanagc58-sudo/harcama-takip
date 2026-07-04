import json
import matplotlib.pyplot as plt
import pandas as pd
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

def kategori_toplamlari():          
    toplamlar = {}
    for harcama in harcamalar:
        kategori = harcama["kategori"]
        tutar = harcama["tutar"]
        if kategori in toplamlar:
            toplamlar[kategori] = toplamlar[kategori] + tutar
        else:
            toplamlar[kategori] = tutar
    return toplamlar


def pandas_analiz():
    df = pd.DataFrame(harcamalar)
    
    print("\n--- Kategoriye Göre Toplam ---")
    print(df.groupby("kategori")["tutar"].sum())
    
    print("\n--- En Yüksek Harcama ---")
    print(df.loc[df["tutar"].idxmax()])
    
    print("\n--- Ortalama Harcama ---")
    print(df["tutar"].mean())

def grafik_ciz():
    toplamlar = kategori_toplamlari()
    kategoriler = list(toplamlar.keys())
    tutarlar = list(toplamlar.values())
    
    plt.pie(tutarlar, labels=kategoriler, autopct="%1.1f%%")
    plt.title("Kategoriye Göre Harcama Dağılımı")
    plt.show()

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
verileri_yukle()
print(kategori_toplamlari())  

while True:
    print("\n1. Harcama Ekle")
    print("2. Harcamaları Göster")
    print("3. Toplamı Göster")
    print("4. Grafik Göster")
    print("5. Pandas Analiz")
    print("6. Çıkış")
    
    secim = input("Seçiminiz: ")
    
    if secim == "1":
        harcama_ekle()
    elif secim == "2":
        harcamalari_goster()
    elif secim == "3":
        toplam_hesapla()
    elif secim == "4":
        grafik_ciz()
    elif secim == "5":
        pandas_analiz()
    elif secim == "6":
        verileri_kaydet()
        print("Görüşürüz!")
        break
    else:
        print("Geçersiz seçim, tekrar dene.")