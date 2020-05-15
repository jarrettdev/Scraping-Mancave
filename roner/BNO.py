import requests
from bs4 import BeautifulSoup
import io
'''
#Define base url
base_url = 'https://docs.google.com/spreadsheets/u/0/d/e/2PACX-1vR30F8lYP3jG7YOq8es0PBpJIE5yvRVZffOyaqC0GgMBN6yt0Q-NI8pxS7hd1F9dYXnowSC6zpZmW9D/pubhtml/sheet?headers=false&gid=0&range=A1:I214'

#Crawl delay from robots.txt
crawl_delay = 1

#get response
response = requests.get(base_url)

#textify response
response = response.text

with io.open('response.html','w',encoding= 'utf-8') as html_file:
	html_file.write(response)
'''
response = ''

with io.open('response.html', 'r', encoding='utf-8') as html_file:
	for line in html_file.read():
		response += line

content = BeautifulSoup(response, 'lxml')



table_data = content.findAll('td')

for td in table_data:
	print(td.text,'\n\n\n')
