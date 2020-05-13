import requests
from bs4 import BeautifulSoup
import io
'''
base_url = 'https://dalessuperstore.com/'

response = requests.get(base_url)

with io.open('response.html', 'w', encoding= 'utf-8') as html_file:
	html_file.write(response.text)
'''
response = ''
with io.open('response.html', 'r', encoding= 'utf-8') as html_file:
	for line in html_file.read():
		response += line

content = BeautifulSoup(response,'lxml')
print(content)

links = content.findAll('a')

with io.open('bs_content.txt','w', encoding= 'utf-8') as content_file:
	for link in links:
		content_file.write(str(link))
		content_file.write('\n\n\n\n\n')
