# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#1.url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html' #input('Enter - ')
#2.url = 'http://py4e-data.dr-chuck.net/known_by_Montgomery.html'
#3.url = 'http://py4e-data.dr-chuck.net/known_by_Mhairade.html'
#4.url = 'http://py4e-data.dr-chuck.net/known_by_Butchi.html'

url = 'http://py4e-data.dr-chuck.net/known_by_Anayah.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
firstLoop = 0
for tag in tags:
    firstLoop = firstLoop + 1
    newUrl = tag.get('href', None)
    #print(newUrl)
    if (firstLoop == 3):
        print('The choosen',newUrl)
        #newHTML = urllib.request.urlopen(url, context=ctx).read()