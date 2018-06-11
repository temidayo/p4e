import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('trackdb2.sqlite')
cur = conn.cursor()

genre = 'apala'
cur.execute('SELECT * FROM Genre WHERE name = ? ', (genre, ))
genre_row = cur.fetchone()
print(genre_row)



