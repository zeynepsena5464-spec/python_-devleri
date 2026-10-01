toplam = 0
notlar = []

ogrenci_adi = input("Öğrenci adı:")
ders_adi = input("Ders adı: ")  
ders_sayisi = int(input("Kaç sınav notu girilecek?"))

for i in range(ders_sayisi):
    not_degeri = float(input(f"{i + 1}. not: "))

    if not_degeri < 0 or not_degeri > 100:
        print("Geçersiz not! Not 0 kabul edildi.")
        not_degeri = 0

    notlar.append(not_degeri)
    toplam += not_degeri

ortalama = toplam / ders_sayisi

if ortalama >= 90:
    harf_notu = "AA"
elif ortalama >= 80:
    harf_notu = "BA"
elif ortalama >= 70:
    harf_notu = "BB"
elif ortalama >= 60:
    harf_notu = "CC"
elif ortalama >= 50:
    harf_notu = "DD"
else:
    harf_notu = "FF"

if ortalama >= 50:
    durum = "GEÇTİ"
else:
    durum = "KALDI"

print("\n--- SONUÇ ---")
print("Öğrenci:", ogrenci_adi.upper())
print("Ders:", ders_adi.upper())
print(f"Ortalama: {ortalama:.2f}")
print("Harf Notu:", harf_notu)
print("Durum:", durum)