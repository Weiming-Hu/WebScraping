from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os

# Chapter 5 Storing data

#--------------------------------------------------------

def downloadSingleFile():
    print("connecting...")
    html = urlopen("http://www.pythonscraping.com/")
    bsObj = BeautifulSoup(html, "html.parser")
    imageLocation = bsObj.find("a", {"id":"logo"}).find("img")["src"]
    print("downloading...")
    urlretrieve(imageLocation, "logo.jpg")

#--------------------------------------------------------

def getAbsoluteUrl(baseUrl, source):
    if source.startswith("http://www."):
        url = "http://" + source[11:]
    elif source.startswith("http://"):
        url = source
    elif source.startswith("www."):
        url = "http://" + source[4:]
    if baseUrl not in url:
        return None
    return url

def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
    path = absoluteUrl.replace("www.", "")
    path = path.replace(baseUrl, "")
    path = downloadDirectory + path
    directory = os.path.dirname(path)
    
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    return path

def downloadMultipleFiles():
    downloadDirectory = "downloaded"
    baseUrl = "http://pythonscraping.com"
    print('connecting...')
    html = urlopen("http://www.pythonscraping.com")
    bsObj = BeautifulSoup(html, "html.parser")
    downloadList = bsObj.findAll("img", src=True)
    print("number of items to be downloaded: %d" % len(downloadList))
    
    for download in downloadList:
        fileUrl = getAbsoluteUrl(baseUrl, download["src"])
        if fileUrl is not None:
            urlretrieve(fileUrl, getDownloadPath(baseUrl, fileUrl, downloadDirectory))
            print("downloaded " + fileUrl)

#--------------------------------------------------------

if __name__ == '__main__':
    print("""
    1 ------ download single file
    2 ------ download multiple files
    """)
    tag = int(input("tag:"))
    if tag == 1:
        downloadSingleFile()
    elif tag == 2:
        downloadMultipleFiles()
    else:
        print("no such tag!")
    print("done!")