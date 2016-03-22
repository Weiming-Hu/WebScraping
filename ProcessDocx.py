from zipfile import ZipFile
from urllib.request import urlopen
from io import BytesIO
from bs4 import BeautifulSoup

print("connecting...")
wordFile = urlopen("http://pythonscraping.com/pages/AWordDocument.docx").read()
print("parsing...")
wordFile = BytesIO(wordFile)
document = ZipFile(wordFile)
xml_content = document.read('word/document.xml')
# print(xml_content.decode('utf-8'))

wordObj = BeautifulSoup(xml_content.decode('utf-8'), 'html.parser')
textStrings = wordObj.findAll("w:t")
for textElem in textStrings:
    print(textElem.text)
# there will be something wrong with the printed results since the tags are complicated in Docx
# actually, parsing HTML and Docx are much of the same