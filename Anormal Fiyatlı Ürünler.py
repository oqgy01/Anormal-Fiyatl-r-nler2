#Doğrulama Kodu
import requests
from bs4 import BeautifulSoup
url = "https://docs.google.com/spreadsheets/d/1AP9EFAOthh5gsHjBCDHoUMhpef4MSxYg6wBN0ndTcnA/edit#gid=0"
response = requests.get(url)
html_content = response.content
soup = BeautifulSoup(html_content, "html.parser")
first_cell = soup.find("td", {"class": "s2"}).text.strip()
if first_cell != "Aktif":
    exit()
first_cell = soup.find("td", {"class": "s1"}).text.strip()
print(first_cell)



import pandas as pd
import requests
from io import BytesIO
import re

# İndirilecek linkler
links = [
    "https://task.haydigiy.com/FaprikaXls/E11V3T/1/",
    "https://task.haydigiy.com/FaprikaXls/E11V3T/2/",
    "https://task.haydigiy.com/FaprikaXls/E11V3T/3/"
]

# Boş bir DataFrame oluştur
merged_df = pd.DataFrame()

# Her bir link için işlem yap
for link in links:
    # İstek gönder ve içeriği al
    response = requests.get(link)
    
    # BytesIO kullanarak içeriği oku
    data = BytesIO(response.content)
    
    # Excel dosyasını DataFrame'e dönüştür
    df = pd.read_excel(data)
    
    # DataFrame'leri birleştir
    merged_df = pd.concat([merged_df, df], ignore_index=True)

# "UrunAdi", "AlisFiyati", "SatisFiyati" sütunları hariç diğer tüm sütunları sil
merged_df = merged_df[["UrunAdi", "AlisFiyati", "SatisFiyati", "Kategori"]]

# Benzersiz hale getir
unique_df = merged_df.drop_duplicates()

# Benzersiz hale getirilmiş DataFrame'i Excel dosyasına kaydet
unique_df.to_excel("Zararına Satılan Ürünler.xlsx", index=False)





print(" ")
print("Oturum Açma Başarılı Oldu")
print(" /﹋\ ")
print("(҂`_´)")
print("<,︻╦╤─ ҉ - -")
print("/﹋\\")
print("Mustafa ARI")
print(" ")










# Veriyi Okuma
df = pd.read_excel('Zararına Satılan Ürünler.xlsx')

# Alış Fiyatına Göre İşlemler ve Kategori Kontrolü
def calculate_list_price(row):
    alis_fiyati = row['AlisFiyati']
    kategori = row['Kategori']

    if 0 <= alis_fiyati <= 24.99:
        result = alis_fiyati + 10
    elif 25 <= alis_fiyati <= 39.99:
        result = alis_fiyati + 13
    elif 40 <= alis_fiyati <= 59.99:
        result = alis_fiyati + 17
    elif 60 <= alis_fiyati <= 199.99:
        result = alis_fiyati * 1.30
    elif alis_fiyati >= 200:
        result = alis_fiyati * 1.25
    else:
        result = alis_fiyati  # Eğer belirtilen aralıklarda değilse aynı değeri koru

    # Kategori Kontrolü (NaN kontrolü eklenmiştir)
    if isinstance(kategori, str) and any(category in kategori for category in ["Parfüm", "Gözlük", "Saat"]):
        result *= 1.20
    else:
        result *= 1.10

    return result

# Yeni Sütun Oluşturma
df['ListeFiyati'] = df.apply(calculate_list_price, axis=1)

# Sonucu Mevcut Excel Dosyasının Üzerine Kaydetme
df.to_excel('Zararına Satılan Ürünler.xlsx', index=False)









# "Zararına Satılan Ürünler" excel dosyasını oku
zararli_urunler_df = pd.read_excel("Zararına Satılan Ürünler.xlsx")

# "Kategori" sütununu sil
zararli_urunler_df = zararli_urunler_df.drop("Kategori", axis=1, errors="ignore")

# "ListeFiyati" sütunundaki verileri tam sayıya çevir
zararli_urunler_df["ListeFiyati"] = zararli_urunler_df["ListeFiyati"].astype(int)

# "0,99" ile toplamayı gerçekleştir
zararli_urunler_df["ListeFiyati"] = zararli_urunler_df["ListeFiyati"] + 0.99


# "SatisFiyati" sütunundaki verileri "ListeFiyati" sütunundaki verilerden çıkar
zararli_urunler_df["Liste Fiyatından Uzaklık"] = zararli_urunler_df["SatisFiyati"] - zararli_urunler_df["ListeFiyati"]


# Güncellenmiş DataFrame'i yazdır veya kaydet
zararli_urunler_df.to_excel("Zararına Satılan Ürünler.xlsx", index=False)






# "Zararına Satılan Ürünler" excel dosyasını oku
zararli_urunler_df = pd.read_excel("Zararına Satılan Ürünler.xlsx")

# "Liste Fiyatından Uzaklık" sütununda değeri 3'ten küçük olan satırları filtrele
zararli_urunler_df = zararli_urunler_df[(zararli_urunler_df["Liste Fiyatından Uzaklık"] > 3) | (zararli_urunler_df["Liste Fiyatından Uzaklık"] < -3)]


# "Liste Fiyatından Uzaklık" sütununa göre büyükten küçüğe sırala
zararli_urunler_df = zararli_urunler_df.sort_values(by="Liste Fiyatından Uzaklık", ascending=False)


# Güncellenmiş DataFrame'i yazdır veya kaydet
zararli_urunler_df.to_excel("Anormal Fiyatlı Ürünler.xlsx", index=False)


