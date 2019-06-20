import urllib2
import sqlite3
from os import path


myList = []
for s in ['F', 'MSFT']:
    # alphavantage API Key: Q6GC7C2H6QQ23J73
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + s
    url = url + "?&apikey=Q6GC7C2H6QQ23J73&datatype=csv"
    sourceCode = urllib2.urlopen(url).read()
    splitSource = sourceCode.split('\r\n')
    for eachLine in splitSource:
        spl = eachLine.split(',')
        if len(spl) == 6 and len(spl[0]) == 10:
            tup = (spl[0], spl[1], spl[2], spl[3], spl[4], spl[5], s)
            myList.append(tup)

print len(myList)

ROOT = path.dirname(path.realpath(__file__))
conn = sqlite3.connect(ROOT + "/db/stocks.db")
c = conn.cursor()
c.executemany('INSERT into stockprices values(?,?,?,?,?,?,?)', myList)
conn.commit()
conn.close()
print c.rowcount
