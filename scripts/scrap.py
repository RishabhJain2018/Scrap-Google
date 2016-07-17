import urllib
import urllib2
import re
import requests
from bs4 import BeautifulSoup

words = ["google"]

url = "https://www.google.co.in/search"
headers = {'Referer':'https://www.google.co.in/', 'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
payload = { 'q' : words[0], 'start' : '0' }
response = requests.get(url, params=payload, headers=headers)

# print (response.url)

# print response.status_code

soup = BeautifulSoup(response.content, 'html.parser')  

print(soup.prettify())

# f=open('response.txt', 'w')

# f.write(soup.prettify().encode('utf-8'))

# f.close()

# h3tags = soup.find_all('h3', class_='r')
# print h3tags
# print "AAAAAAAAAAAa"

# for h3 in h3tags:
#     try:
#         print (re.search('url\?q=(.+?)\&sa', h3.a['href']).group(1))
#         print "1"
#     except:
#         continue