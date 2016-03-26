import time
from urllib.request import urlretrieve
from selenium import webdriver
from PIL import Image as PIL_Image

# may have problems when executed by pytno35

# create new Selenium driver
driver = webdriver.PhantomJS(executable_path="phantomjs.exe")
# driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")

print("connecting...")
driver.get("http://www.amazon.com/War-Peace-Leo-Nikolayevich-Tolstoy/dp/1427030200")
time.sleep(2)

# click on the book preview button
print("clicking...")
driver.find_element_by_id("sitbLogoImg").click()
imageList = set()
print("loading preview page...")

# wait for the page to load
time.sleep(5)
# while the right arrow is available for clicking, turn through pages
while "pointer" in driver.find_element_by_id("sitbReaderTightPageTurner").get_attribute("style"):
    print("getting one new page...")
    driver.find_element_by_id("sitbReaderRightPageTurner").click()
    time.sleep(2)
    # Get any new pages that have loaded (multiple pages can load at once, but duplicates will not be added to a set)
    pages = driver.find_element_by_xpath("//div[@class='pageImge']/div/img")
    for page in pages:
        image = page.get_attribute("src")
        imageList.add(image)

driver.quit()

# start processing the images we've collected URLs for with Tesseract
# skip ******************
for image in imageList:
    print(image)

urlretrieve(imageList[0], "firstImage.jpg")
firstImg = PIL_Image.open("firstImage.jpg")
firstImg.show()
    