"""
Ehliyet Kursuna kayıt olma Proje

Öğretim en az lise
Kişinin yaşı en az 18 
 

teaching = Öğretim
driver_class = sürücü sınıf

"""


print("Hoşgeldiniz")

name = input("İsminiz:")
surname = input("Soyadınız:")
age = int(input("Yaşınız:"))
teaching = input("Öğretim Durumunuz nedir ?")
driver_class = input("Sürücü Sınıf:")

if driver_class == "b" or "B":
    tutar = 12500
elif driver_class == "e" or "E":
    tutar = 7600


if (age >= 18 ) and (teaching == "Lise" or "lise" or "Üniversite" or "üniversite"  ):
    print(f"İsim:{name} Soyad: {surname} Yaş: {age} Öğretim durumu: {teaching} Sürücü sınıfı {driver_class} ve ücret: {tutar} Başarılıyla kayıt oldunuz.")
else:
    print("Maalesef kayıt şartları yetersiz.")
