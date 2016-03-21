from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re
from pip._vendor.requests.exceptions import HTTPError
import json

# Web scrapying chapter 4
# user IP from Wiki articles and locate them to countries

def getLinks(articleUrl):
    print("connecting...")
    html = urlopen("https://en.wikipedia.org" + articleUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    return bsObj.find('div', {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))

def getHistoryIPs(pageUrl):
    pageUrl = pageUrl.replace("/wiki/", "")
    historyUrl = "https://en.wikipedia.org/w/index.php?title=" + pageUrl + "&action=history"
    print("history url is: " + historyUrl)
    html = urlopen(historyUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    ipAddresses = bsObj.findAll("a", {"class":"mw-userlink mw-anonuserlink"})
    addressList = set()
    for ipAddress in ipAddresses:
        addressList.add(ipAddress.get_text())
    return addressList

def getCountriy(ipAddress):
    try:
        response = urlopen("http://freegeoip.net/json/" + ipAddress).read().decode('utf-8')
    except HTTPError:
            return None
    responseJson = json.loads(response)
    return responseJson.get("country_code")
    
if __name__ == '__main__':
    print("generate random number...")
    random.seed(datetime.datetime.now())
    links = getLinks("/wiki/Python_(programming_language)")
    print("number of links: %d", len(links))

    while(len(links)>0):
        for link in links:
            print("---------------------")
            historyIPs = getHistoryIPs(link.attrs["href"])
            if not historyIPs:
                print("No revision history!")
            else:
                for historyIP in historyIPs:
                    country = getCountriy(historyIP)
                    print(historyIP + " is from " + country)
        
        newLink = links[random.randint(0, len(links)-1)].attrs["href"]
        links = getLinks(newLink)
    
    print("done!")