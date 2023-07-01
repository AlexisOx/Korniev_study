from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

# First test - expected result -> word "Results" should be on the page

options = Options()
options.add_argument("start-maximized"); # open Browser in maximized mode
# options.add_argument("disable-infobars"); # disabling infobars
# options.add_argument("--disable-extensions"); # disabling extensions
# options.add_argument("--disable-gpu"); # applicable to windows os only
# options.add_argument("--disable-dev-shm-usage"); # overcome limited resource problems
options.add_argument("--no-sandbox")
# options.add_argument("headless")

# START DRIVER
driver = webdriver.Chrome(service=Service("D:\\Korniev_Hillel\\P1\\Selenium_HW\\chromedriver.exe"), options=options)
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.w3schools.com/")
# time.sleep(20) #sleep for 2 sec
time.sleep(2) #sleep for 2 sec

# assert "Python" in driver.title

# find_element(By.TAG_NAME, "input")
# find_element(By.CLASS_NAME, "search-field")
# find_element(By.CSS_SELECTOR, "css selector")
# inputElement = driver.find_element(By.ID, "search2")

# elem = driver.find_element(By.NAME, "q")
goButton = driver.find_element(By.XPATH, '//*[@id="pagetop"]/div[2]/a[4]')
goButton.click()
# inputElement.send_keys("telPycon007")
# elem.send_keys(Keys.RETURN)
# goButton = driver.find_element(By.ID, "learntocode_searchbtn")



time.sleep(2) #sleep for 2 sec
# assert "No results found." not in driver.page_source
assert "Coding Bootcamps" in driver.page_source
driver.close()