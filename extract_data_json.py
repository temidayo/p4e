import urllib.request, urllib.parse, urllib.error
import json

address = input('Enter Location: ')
if len(address) < 1: 
    address = ' http://py4e-data.dr-chuck.net/comments_42.xml'

url = address #urllib.parse.urlencode(address)
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')
#print(data.decode())
 
info = json.loads(data)
print('User count:', len(info['comments']))
sum = 0
comments = info['comments']
for comment in comments:
    #print(comment['name'],comment['count'])
    sum = sum + int(comment['count'])
print('Sum:',sum)