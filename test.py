from selenium import webdriver

import lxml.html as lh
from selenium import webdriver

browser = webdriver.Chrome("E:/Utilities/chromedriver.exe")
browser.get('http://commons.wikimedia.org/wiki/File%3aBrad_Pitt_Cannes_2011.jpg')
content = browser.page_source
browser.quit()

doc = lh.fromstring(content)
for elt in doc.xpath('//span[a[contains(@title,"Use this file")]]/text()'):
    print (elt)