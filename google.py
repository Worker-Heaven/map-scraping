from selenium import webdriver
from selenium.webdriver.common.by import By


url = 'http://google.com'


driver = webdriver.Chrome('E:/Utilities/chromedriver.exe')
driver.implicitly_wait(30)

driver.get(url)

driver.find_element_by_xpath('//*[@id="gbwa"]').click()

