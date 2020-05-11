import requests
from bs4 import BeautifulSoup
import io
import json

base_url = 'https://www.overstock.com/Home-Garden/Mattresses/Twin,/size,/2019/subcat.html?TID=Mattresses:01:Bmod-1:Twin'
response = requests.get(base_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0'})

with io.open('diablo.html','w', encoding = 'utf-8') as html_file:
	html_file.write(response.text)

content = BeautifulSoup(response.text,'lxml')
cards = content.findAll('div', {'class':'productCard'})

for card in cards:
	titleCard = content.findAll('div', {'class':'productCardInfoBarContainerWithTitle'})