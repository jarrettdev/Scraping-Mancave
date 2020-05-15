import requests
from bs4 import BeautifulSoup
import io
'''
#define base_url
base_url = 'https://www.worldometers.info/coronavirus/'

#define crawl delay
crawl_delay = 0

#get response
response = requests.get(base_url)

#textify response
response = response.text

#write response to file
with io.open('response.html', 'w', encoding= 'utf-8') as html_file:
	html_file.write(response)
'''
#define respone in file-read scope
response = ''
#read response from file
with io.open('response.html', 'r', encoding= 'utf-8') as html_file:
	for line in html_file.read():
		response += line


#create bs object to parse content
content = BeautifulSoup(response, 'lxml')

#print(content)

table_data = content.findAll('td',{'style':'font-weight: bold; text-align:right'})

for td in table_data:
	print(td.text)