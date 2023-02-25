import requests
import pandas as pd
from bs4 import BeautifulSoup

# Send a request to the website
url = 'https://www.jakartanotebook.com/p/biutte.co-pembersih-telinga-korek-kuping-ear-wax-picker-7-pcs-jc7-silver'
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Find the element containing the data you want to scrape
nama_product = soup.find('h1', {'class': 'kQDke'}).text
product_name_dict = {"Nama Produk" : nama_product[:70]}

sku = soup.find('span', {'class': 'bwqOiD'}).text
sku_dict = {"SKU" : sku}

dt = ""
intro = soup.article.p.text
dt = f"{dt + intro}\n\n"

dt = f"{dt}Fitur\n"
title_fitur = soup.article.table.tbody.find_all('div')
desc_fitur = soup.article.table.tbody.find_all('p')
fj = 0
for de3 in title_fitur:
    dt = f"{dt + de3.text}\n{desc_fitur[fj].text}\n\n" #print(f"{spec.text} : {data_isi_spec[jml].text}")
    fj +=1

# Rincian
data_ele = soup.find('div', {'class': 'bqlxyt'}).p.string
dt = f"{dt + data_ele}\n"

# Isi Rincian
data_ele = soup.ul.find_all('li')
for ele in data_ele:
    dt = f"{dt + ele.text}\n"
dt = f"{dt}\n"

# Spesifikasi
spec_title = soup.find('h3', {'class': 'dgQyOe'}).string
dt = f"{dt + spec_title}:\n"

# Isi Spesifikasi
data_spec = soup.find_all('td', {'class': 'hnFYGQ'})
data_isi_spec = soup.find_all('div', {'class': 'iQVyZh'})
jml = 0
for spec in data_spec:
    dt = f"{dt + spec.text} : {data_isi_spec[jml].text}\n" #print(f"{spec.text} : {data_isi_spec[jml].text}")
    jml +=1
dt = f"{dt}\n"
dt = f"{dt}Jangan lupa follow toko kami yah... Selamat berbelanja :)"
print(dt)

desc_dict = {"Deskripsi" : dt}
cat_dict = {"Kode Kategori" : ""}
minOrder_dict = {"Minimum Pemesanan" : ""}
etalase_dict = {"Nomor Etalase" : 25230456}
preorder_dict = {"Waktu Proses Preorder" : ""}
kondisi = {"Kondisi" : ""}
video = {"URL Video Produk 1" : "", "URL Video Produk 2" : "", "URL Video Produk 3" : ""}

# Berat Product
berat = soup.find('div', {'class': 'dfnnPX'}).text
weight = int(float(berat[2:].replace(" kg",""))*1000)
berat_dict = {"Berat" : weight}

# harga = soup.find('div', {'class': 'bxSpwo'}).text
# print(f"Harga : {harga}")

imgDict1 = {"Foto Produk 1" : "", "Foto Produk 2": "", "Foto Produk 3": "", "Foto Produk 4": "", "Foto Produk 5": ""}
imgDict2 = imgDict1.copy()
count_img = 0
for link in soup.find_all("img", {"class":"fHuhkO"}):
    # print(link.get('src'))
    count_img += 1
    if count_img == 6 :
        break
    img = link.get('src')

    imgDict2.update({f"Foto Produk {count_img}" : img})

data_row = {}
data_row.update(product_name_dict)
data_row.update(desc_dict)
data_row.update(cat_dict)
data_row.update(berat_dict)
data_row.update(minOrder_dict)
data_row.update(etalase_dict)
data_row.update(preorder_dict)
data_row.update(imgDict2)
data_row.update(video)
data_row.update(sku_dict)

# export to excel
df = pd.DataFrame(data_row, index=[0])
df.to_excel('items.xlsx', index=False)

print(imgDict2)

# Print the data
print(f"\n{nama_product}\n\n{sku}\n\n{weight}\n")