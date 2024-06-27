import re
# [3]
text = "ZHONG XING PENG YUE Gelas Ukur Lab Kimia Borosilicate Glass 1000 ml - GG-17 - Transparent"
lastWord_pattern = r'.*[\s-]([^-\s]*)$'
firstWord_pattern = r'^(.*?)\s-\s'

result = re.findall(firstWord_pattern, text)
result2 = re.findall(lastWord_pattern, text)

for item in range(len(result)):
    print(result[item])

for item2 in range(len(result2)):
    print(result2[item2])

# [2] 
product_name = "Taffware Bantal Angin Travel Inflatable - BAT23 - Blue"
brand_names = ['TaffSPORT', 'TaffLED', 'Taffware', 'TaffGO', 'One Two Cups', 'TaffHOME', 'TaffGUARD', 'Rhodey']

# Gabungkan merek-merek menjadi satu pola regex dengan operator OR
brand_regex = '|'.join(brand_names)

# Buat pola regex untuk mencari merek di awal kalimat
rgx = r'^(?:{})\b\s*'.format(brand_regex)

# Hapus merek dari judul produk
hasil = re.sub(rgx, '', product_name)
print(hasil)

# [1] Hilangkan Merek dengan huruf kapital pada awal judul kalimat
regex = r'^(?:[A-Z]+\s)*[A-Z]+(?=\s) '

result = re.sub(regex, '', text)
print(result)