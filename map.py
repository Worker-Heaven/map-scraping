from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import time
import csv

def get_data(data):
  if len(data) > 0:
    return data[0].text
  else:
    return 'NaN'

def scrape_data(driver):
  time.sleep(1)
  name = driver.find_element_by_xpath("//h1[@class='section-hero-header-title']").text

  ratings = driver.find_elements_by_xpath("//span[@class='section-star-display']")
  rating = get_data(ratings)

  reviews = driver.find_elements_by_xpath("//li[@class='section-rating-term']//button[@class='widget-pane-link']")
  review = get_data(reviews)
   
  addresses = driver.find_elements_by_xpath("//div[@data-section-id='ad']//span[@class='section-info-text']//span[@class='widget-pane-link']")
  address = get_data(addresses)
  
  pluscodes = driver.find_elements_by_xpath("//div[@data-section-id='ol']//span[@class='section-info-text']//span[@class='widget-pane-link']")
  pluscode = get_data(pluscodes)

  websites = driver.find_elements_by_xpath("//div[@data-section-id='ap']//span[@class='section-info-text']//span[@class='widget-pane-link']")
  website = get_data(websites)

  phones = driver.find_elements_by_xpath("//div[@data-section-id='pn0']//span[@class='section-info-text']//span[@class='widget-pane-link']")
  phone = get_data(phones)
  
  photoUrl = driver.find_elements_by_xpath("//div[@class='section-image-pack-image-container']//img")[0].get_attribute('src')

  print ('name', name)
  print ('rating', rating)
  print ('review', review)
  print ('address', address)
  print ('website', website)
  print ('phone', phone)
  print ('photo url', photoUrl)

  with open('E:/result.csv', 'a+') as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow([name, rating, review, address, pluscode, website, phone, photoUrl])

  backBtn = driver.find_element_by_xpath("//button[contains(@class, 'section-back-to-list-button')]")
  backBtn.send_keys("\n")
  time.sleep(1)


# constants for the app
SITE_URL = 'https://maps.google.com/'
download_path = 'E:/'
chromedriver_path = "E:/Utilities/chromedriver.exe"


with open('E:/result.csv', 'w') as csvfile:
  writer = csv.writer(csvfile)

  writer.writerow(['name', 'rating', 'review', 'address', 'plus code', 'website', 'phone', 'photoUrl'])

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

searchInput = driver.find_element_by_id('searchboxinput')
searchInput.send_keys("apartments near Scotland, UK")

searchButton = driver.find_element_by_id("searchbox-searchbutton")
searchButton.send_keys("\n")


while (1):
  for index in range(20):
    time.sleep(1)

    try:
      items = driver.find_elements_by_xpath("//div[@class='section-result']")
    except NoSuchElementException:
      driver.close()

    items[index].send_keys("\n")
    scrape_data(driver)

  time.sleep(2)
  driver.find_element_by_xpath("//button[@id='n7lv7yjyC35__section-pagination-button-next']").send_keys("\n")

