import requests
from bs4 import BeautifulSoup
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}
url = 'https://covid.saude.gov.br/'
response = requests.get(url, headers=headers)
site = BeautifulSoup(response.text, 'html.parser')
paine = site.find_all('div', attrs={'class':'card-total col-left no-shadow'})
print(site.find('div', attrs={'class': 'card-total col-left no-shadow'}))
