from selenium import webdriver
from selenium.webdriver.common.by import By

# constants for the app
SITE_URL = 'https://www.finanssivalvonta.fi/paaomamarkkinat/liikkeeseenlaskijat-ja-sijoittajat/johtohenkiloiden-liiketoimet/lyhyeksimyynti-taulukko'
download_path = 'E:/'
chromedriver_path = "E:/Utilities/chromedriver.exe"

# set up chrome options
chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : download_path}
chromeOptions.add_experimental_option("prefs",prefs)

driver = webdriver.Chrome(executable_path=chromedriver_path, options=chromeOptions)
driver.implicitly_wait(30)

# Open the website
driver.get(SITE_URL)

print ('loaded...')

# button = driver.find_element_by_xpath("//button/span[contains(text(), '(.csv)')]")

button = driver.find_element_by_xpath("//button[.//span[contains(text(), '(.csv)')]]")

print (button.get_attribute('aria-controls'))

button.send_keys("\n")


