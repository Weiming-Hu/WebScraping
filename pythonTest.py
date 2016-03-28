import unittest
from urllib.request import urlopen
from bs4 import BeautifulSoup

# class TestAddition(unittest.TestCase):
#     def setUp(self):
#         print("setting up the test")
#     
#     
#     def tearDown(self):
#         print("tearing down the test")
#     
#     
#     def test_twoPlusTwo(self):
#         total = 2+2
#         self.assertEqual(4, total)

class TestWikipedia(unittest.TestCase):
    bsObj = None
    def setUpClass():
        global bsObj
        url = "http://en.wikipedia.org/wiki/Monty_Python"
        bsObj = BeautifulSoup(urlopen(url), "html.parser")
    
    def test_titleText(self):
        global bsObj
        pageTitle = bsObj.find("h1").get_text()
        self.assertEqual("Monty Python", pageTitle)
    
    def test_contentExists(self):
        global bsObj
        content = bsObj.find("div", {"id":"mw-content-text"})
        self.assertIsNotNone(content)
        

if __name__ == '__main__':
    unittest.main()
    