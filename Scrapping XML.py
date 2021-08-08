import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as et


total = 0
url_link = input('Enter location: ')
handler = urllib.request.urlopen(url_link).read()
print('Retrieving', url_link)
print('Retrieved', len(handler), "characters")

tree = et.fromstring(handler)
counts = tree.findall('.//count')
for item in counts:
    total += int(item.text)
print('Count:', len(counts))
print('Sum:', total)
