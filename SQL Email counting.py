import sqlite3

connection = sqlite3.connect('email_count.sqlite')
handler = connection.cursor()

handler.execute('DROP TABLE IF EXISTS Counts')

handler.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

file_name = input('Enter file name: ')
if len(file_name) < 1:
    file_name = 'mbox.txt'
fh = open(file_name)
for line in fh:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    email = pieces[1]
    email_parts = email.split('@')
    email_domain = email_parts[1]
    handler.execute('SELECT count FROM Counts WHERE org = ?', (email_domain,))
    row = handler.fetchone()
    if row is None:
        handler.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (email_domain,))
    else:
        handler.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (email_domain,))
connection.commit()

sql_str = 'SELECT org, count FROM Counts ORDER BY count DESC'

for row in handler.execute(sql_str):
    print(str(row[0]), row[1])

handler.close()
