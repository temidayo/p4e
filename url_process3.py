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

def processURL(url):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    firstLoop = 0
    for tag in tags:
        firstLoop = firstLoop + 1
        if (firstLoop == 18):
            newUrl = tag.get('href', None)
            return(newUrl)
url = 'http://py4e-data.dr-chuck.net/known_by_Alicja.html'
retry = 7
print(url)
while retry > 0:
   url = processURL(url)
   print(url)
   retry = retry - 1
            