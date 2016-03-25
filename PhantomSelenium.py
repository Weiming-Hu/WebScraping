# NOTE: Selenium is perfectly compatible with Python 2.7, but flawed with Python 3.5

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def showPreloadHTML():
    driver = webdriver.PhantomJS(executable_path='phantomjs.exe')
    driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
    
    # this is to wait the browser to finish connecting the page
    time.sleep(3)
    
    print(driver.find_element_by_id("content").text)
    # other functions you can try out:
    # driver.find_element_by_css_selector(css_selector)
    # driver.find_element_by_tag_name(name)
    # [with s]
    # driver.find_elements_by_css_selector(css_selector)
    # driver.find_elements_by_tag_name(name)

    driver.close()

def waitUntilLoadedButton():
    driver = webdriver.PhantomJS(executable_path="phantomjs.exe")
    driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
    try:
        # an implicit wait waits for some state in the DOM (Document Object Model) to occur before continuing
        # the triggering DOM state is defined by expected-condition (EC here)
        element = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.ID, "loadedButton")))
    finally:
        print(driver.find_element_by_id("content").text)
        driver.close()    


if __name__ == '__main__':
#     showPreloadHTML()
#     waitUntilLoadedButton()
    