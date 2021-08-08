import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup


url_link = input('Enter - ')
handler = urllib.request.urlopen(url_link).read()
soup = BeautifulSoup(handler, 'html.parser')

total = 0
count = 0
tags = soup('span')
for tag in tags:
    count += 1
    total += int(tag.contents[0])
print('Count', count)
print('Sum', total)

