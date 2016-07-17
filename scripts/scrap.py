import requests
import csv
import thread
from bs4 import BeautifulSoup

with open('words.csv', 'rb') as csvfile:

	for line in csvfile.readlines():
		words=line.split(',')
		# print words

class scrapThread(threading.Thread):
	def __init__(self, threadID, name, counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter


	def run(self):
		print "Starting " + self.name
		threadLock.acquire()
		scrap(self.name, self.counter, word)
		threadLock.release()


def scrap(threadname, counter, word):
	# j=0
	# while j < len(words):

	url = "https://www.google.co.in/search"
	headers = {'Referer':'https://www.google.co.in/', 'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
	payload = { 'q' : str(word), 'start' : '0' }
	response = requests.get(url, params=payload, headers=headers)
	# print "j : ", response
	soup = BeautifulSoup(response.content, 'html.parser')
# f=open('text.html', 'w')
# f.write(soup.prettify().encode('utf-8'))
# f.close()
	f=open(str(files[j]) + ".txt", 'a')
	h3tags = soup.find_all('h3', class_='r')
	for h3 in h3tags:
	    try:
	    	print "enter try"
	    	f.write( h3.text + "  \n ")
	    except:
	    	print "*********************************"
	    	# print "Enter except : ", j
	    	print "words ", word
	    	print "*********************************"
	    	continue
	# j=j+1    	
	# print " Completed : ", j
	f.close()

