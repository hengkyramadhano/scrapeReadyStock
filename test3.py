import requests
from bs4 import BeautifulSoup

# Send a request to the website
url = 'https://www.jakartanotebook.com/p/taffstudio-wireless-uhf-call-center-mic-with-transmitter-hx-w002-black'
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Find the element containing the data you want to scrape
data_element = soup.find('h1', {'class': 'bHQSTV'}).text
data_element2 = soup.find('span', {'class': 'kFanSE'}).text
# data_element3 = soup.find_all("img", {"class":"hijjRv"})
data_element3 = soup.article.get_text()

for link in soup.find_all("img", {"class":"hijjRv"}):
    print(link.get('src'))

# for i in data_element3 :
#     print(i)

# Extract the data you want from the element
# data = data_element.text

# Print the data
print(f"\n{data_element}\n\n{data_element2}\n\n{data_element3}\n")