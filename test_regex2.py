import re

product_name = "TaffSPORT Bantal Angin Travel Inflatable - BAT23 - Blue"
brand_names = ['TaffSPORT', 'TaffLED', 'Taffware']

# Gabungkan merek-merek menjadi satu pola regex dengan operator OR
brand_regex = '|'.join(brand_names)

# Buat pola regex untuk mencari merek di awal kalimat
regex = r'^(?:{})\b\s*'.format(brand_regex)

# Hapus merek dari judul produk
result = re.sub(regex, '', product_name)
print(result)
