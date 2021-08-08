import urllib.request, urllib.parse, urllib.error
import json


url_link = input('Enter location: ')
print('Retrieving:', url_link)
handler = urllib.request.urlopen(url_link).read()
js = json.loads(handler)
print('Retrieved', len(handler), "characters")
total = 0
count = 0
for comment in js['comments']:
    count += 1
    total += comment['count']
print('Count:', count)
print('Sum:', total)
