# -*- coding: utf-8 -*- 

from urllib.request import urlopen
from bs4 import BeautifulSoup

# define encoding and parse the txt manually
html = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt")
print(str(html.read(), 'utf-8'))
print("\n-------------------\n")

# BeautifulSoup has already parsed the txt
html = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt")
bsObj = BeautifulSoup(html, "html.parser")
print(bsObj)

# Codes below are from the book Web Scraping
# content = bsObj.find("pre", {"id":"mw-content-text"}).get_text()
# print(type(content))
# content = bytes(content, "UTF-8")
# print(type(content))
# content = content.decode("UTF-8")
# print(type(content))
