from urllib.request import urlopen

# This module implements a file-like class, StringIO, that reads and writes a string buffer (also known as memory files).
# So you won't  bother to create new files
# Reference: https://docs.python.org/2/library/stringio.html
from io import StringIO

import csv

data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii', 'ignore')

# raw data
print(data)
print("\n-------------------------------------\n")


# put csv in a list
dataFile = StringIO(data)
csvReader = csv.reader(dataFile)
for row in csvReader:
    print(row)

print("\n-------------------------------------\n")

# put csv in a dict
dataFile = StringIO(data)
csvDict = csv.DictReader(dataFile)
print(csvDict.fieldnames)
for row in csvDict:
    print(row)
