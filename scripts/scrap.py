import requests
from bs4 import BeautifulSoup

words = ["google"]

url = "https://www.google.co.in/search"
headers = {'Referer':'https://www.google.co.in/', 'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
payload = { 'q' : words[0], 'start' : '0' }
response = requests.get(url, params=payload, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')

f=open('response.txt', 'a')

h3tags = soup.find_all('h3', class_='r')
for h3 in h3tags:
    try:
    	f.write( h3.text + "  \n ")
    	print h3.text
    except:
    	continue
f.close()
