import requests
import json
from bs4 import BeautifulSoup
import io
'''
#define a url
base_url = 'https://www.asus.com/us/OfficialSiteAPI.asmx/GetModelResults?WebsiteId=52&ProductLevel2Id=155&FiltersCategory=5993&Filters=&Sort=3&PageNumber=1&PageSize=20'

#get http response

#response = requests.get(base_url, headers= {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0','Cookie':'ASP.NET_SessionId=jtm2wt2xzp11qrcbslnok2pz; __AntiXsrfToken=64ceaae73b5349b88f7516c242ad35b3; search_initproduct=52,,; isReadCookiePolicyDNT=; current_site=; BuinsessCookie='''

#with io.open('response.html', 'w', encoding='utf-8') as html_file:
	#html_file.write(json.dumps(response.json()))

response = ''

with io.open('response.html','r',encoding='utf-8') as html_file:
	for line in html_file.read():
		response += line

json_data = json.loads(response)
for item in json_data['Result']['Obj']:
	print(json_data['Result']['Obj'], '\n\n\n\n')
#print(json_data['Result']['Obj'][1])
