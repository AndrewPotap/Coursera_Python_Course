import re


handler = open('Assignement text.txt')
total = 0
for line in handler:
    line = line.strip()
    words = re.findall('[0-9]+', line)
    for i in words:
        total += int(i)
print(total)
