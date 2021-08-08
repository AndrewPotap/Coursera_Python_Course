import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url_link = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))
print('Retrieving:', url_link)


def parsing(url_link, loop_count):
    handler = urllib.request.urlopen(url_link).read()
    soup = BeautifulSoup(handler, 'html.parser')
    tags = soup('a')
    new_link = tags[position - 1].get('href', None)
    print('Retrieving:', new_link)
    loop_count -= 1
    if loop_count == 0:
        quit()
    parsing(new_link, loop_count)


parsing(url_link, count)
