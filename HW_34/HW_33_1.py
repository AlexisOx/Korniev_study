from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

options = Options()
options.add_argument("--no-sandbox")

def test_clickable_Sign_In():
    driver = webdriver.Chrome(service=Service('D:\\Korniev_Hillel\\P1\\Selenium\\tests_pytest\\chromedriver.exe'),
                              options=options)

    user = "guest"
    password = "welcome2qauto"
    driver.get("https://" + user + ":" + password + "@" + "qauto2.forstudy.space/")

    # CLICK by clickable
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Sign In')]"))).click()

    # GET ATTRIBUTE
    signIn_attr = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Sign In')]"))).get_attribute("class")
    # signIn = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "signinEmail"))).get_attribute("formcontrolname")
    print("Check attribute: " + signIn_attr)

    # CLICK be presense
    # WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Sign In')]"))).click()

    elem = driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]")
    elem.click()

    # goButton = driver.find_element(By.ID, "submit")
    # goButton.click()

    assert "No results found." not in driver.page_source
    driver.close()