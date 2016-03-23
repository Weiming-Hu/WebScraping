#===============================================================================
# chapter 7
# cleaning your data
# n-gram
#===============================================================================

from urllib.request import urlopen
from bs4 import BeautifulSoup
from pprint import pprint
import re
import string


def ngrams(input, n):
    output = []
    for i in range(len(input)-n+1):
        output.append(input[i:i+n])
    return output

def cleanContent(input):
    print("cleanning data...")
    # clean up minor information
    # replace all instances of the newline character
    content = re.sub('\n+', ' ', input)
    # replace all instances of multiple spaces in a row with a single space
    content = re.sub(' +', ' ', content)
    # escape characters are eliminated by encoding the content with UTF-8
    content = bytes(content, "UTF-8")
    content = content.decode("ascii", "ignore")
    
    cleanInput = []
    content = content.split(' ')
    for item in content:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInput.append(item)
            
    return cleanInput


print("connecting...")
html = urlopen("https://en.wikipedia.org/wiki/Python_(programming_language)")
print("parsing...")
bsObj = BeautifulSoup(html, "html.parser")
content = bsObj.find("div", {"id":"mw-content-text"}).get_text()
content = cleanContent(content)
ngrams = ngrams(content, 2)

pprint(ngrams[:100])
print("2grams count is: " + str(len(ngrams)))