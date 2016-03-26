from selenium import webdriver
from pprint import pprint

driver = webdriver.PhantomJS(executable_path="phantomjs.exe")
driver.get("http://pythonscraping.com")
driver.implicitly_wait(1)
pprint(driver.get_cookies())

savedCookies = driver.get_cookies()

# it must load the website first so that Selenium knows which website the cookies belong to, even if the act of loading the website does nothing useful for us
driver2 = webdriver.PhantomJS(executable_path="phantomjs.exe")

driver2.get("http://pythonscraping.com")
driver2.delete_all_cookies()
for cookie in savedCookies:
    driver2.add_cookie(cookie)
    
    
    

driver2.get("http://pythonscraping.com")
driver.implicitly_wait(1)
print(driver2.get_cookies())