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

def test_click_settings():
    driver = webdriver.Chrome(service=Service('D:\\Korniev_Hillel\\P1\\Selenium\\tests_pytest\\chromedriver.exe'),
                              options=options)

    user = "guest"
    password = "welcome2qauto"
    driver.get("https://" + user + ":" + password + "@" + "qauto2.forstudy.space/")

    goButton = driver.find_element(By.XPATH, "//button[contains(text(), 'Sign In')]")
    goButton.click()

    inputElement = driver.find_element(By.ID, "signinEmail")
    inputElement.send_keys("hanigip462@gam1fy.com")
    inputElement = driver.find_element(By.ID, "signinPassword")
    inputElement.send_keys("Qwerty0708")

    goButton = driver.find_element(By.XPATH, "(//button[@type='button'])[3]")
    goButton.click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//a[contains(text(),'Settings')])[2]"))).click()

    assert "Settings" in driver.page_source

    driver.close()