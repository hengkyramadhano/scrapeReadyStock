from bs4 import BeautifulSoup
import requests

# Send a request to the website
url = 'https://www.jakartanotebook.com/p/biutte.co-pembersih-telinga-korek-kuping-ear-spoon-wax-picker-with-led-light-7-pcs-jc9-rose-gold'
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

for link in soup.section.find_all('a'):
    print(link.get('href'))