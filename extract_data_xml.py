import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

address = input('Enter Location: ')
if len(address) < 1: 
    address = ' http://py4e-data.dr-chuck.net/comments_42.xml'

url = address #urllib.parse.urlencode(address)
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')
#print(data.decode())
 
tree = ET.fromstring(data)
#print(tree)
comments = tree.findall('comments/comment')
print('Count:', len(comments))
sum = 0
for comment in comments:
    #print(comment.find('name').text,comment.find('count').text)
    sum = sum + int(comment.find('count').text)
print('Sum:',sum)