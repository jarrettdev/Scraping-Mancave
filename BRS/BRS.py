import requests
import io
from bs4 import BeautifulSoup
'''
#define base_url
base_url = 'https://www.bulkreefsupply.com/catalog/category/ajax/id/116/?p=1'

#define crawl delay
crawl_delay = 0

#get response
response = requests.get(base_url)

#textify response
response = response.text

#write response to file
with io.open('response.html', 'w', encoding= 'utf-8') as html_file:
	html_file.write(response)


#define response in scope

'''

response = ''

#read from file
with io.open('response.html', 'r', encoding= 'utf-8') as html_file:
	for line in html_file.read():
		response += line


#create bs4 ojbect
content = BeautifulSoup(response, 'lxml')

pg = content.find('ul',{'class':'products-grid'})

links = pg.findAll('a')

prices = pg.findAll('span',{'class':'price'})


for price in prices:
	print(price.text)

