import requests
from bs4 import BeautifulSoup
import io
import json

base_url = 'https://www.schooloutlet.com/Stool_Style_Seating_s/4091.htm?#prodPerPage=20&SortBy=undefined'
response = requests.get(base_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0'})

with io.open('diablo.html','w', encoding = 'utf-8') as html_file:
	html_file.write(response.text)

content = BeautifulSoup(response.text,'lxml')
try:
    print(response.json())
except json.decoder.JSONDecodeError:
    print("It's not JSON")
#cards = content.findAll('div', {'class':'productCard'})
