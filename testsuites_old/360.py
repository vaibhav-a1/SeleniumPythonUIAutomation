
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import allure
service_obj=Service()
driver= webdriver.Chrome(service=service_obj)


# driver.find_element(By.LINK_TEXT,"Forgot password?").click()
# driver.find_element(By.XPATH,"//form/md-input-container/input").send_keys("vaibhav.verma@aqcuia.com")
# driver.find_element(By.XPATH,"//form/div[2]/input").send_keys("123456")
# driver.find_element(By.XPATH,"//form/div[3]/input").send_keys("123456")
# driver.find_element(By.XPATH,"//button[@type='submit']").click()


@allure.feature("Login Feature")
@allure.story("Valid Login")
@allure.title("Test Login with valid credentials")
def test_login_pass():
        driver = webdriver.Chrome()
        try:
                driver.get("https://qa-vega.agilone.com/login")
                wait = WebDriverWait(driver, 10)
                element = wait.until(EC.presence_of_element_located((By.XPATH, "//form/md-input-container/input")))

                # Enter text into the input field
                element.send_keys("aruna.boddu@acquia.com")
                element = wait.until(EC.presence_of_element_located((By.XPATH, "//form/div/button"))).click()
                element = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='input_2']"))).send_keys("ArunaAgilOne@1")
                element = wait.until(EC.presence_of_element_located((By.XPATH, "//form/div[2]/button"))).click()
                time.sleep(10)
                assert True

        finally:
                driver.quit()

@allure.feature("Login Feature")
@allure.story("Invalid Login")
@allure.title("Test Login with invalid credentials")
def test_login__fail():
        driver = webdriver.Chrome()
        try:
                driver.get("https://qa-vega.agilone.com/login")
                wait = WebDriverWait(driver, 10)
                element = wait.until(EC.presence_of_element_located((By.XPATH, "//form/md-input-container/input")))

                # Enter text into the input field
                element.send_keys("vaibhav.verma@acquia.com")
                element = wait.until(EC.presence_of_element_located((By.XPATH, "//form/div/button"))).click()
                element = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='input_2']"))).send_keys("VAibhav@3554")
                element = wait.until(EC.presence_of_element_located((By.XPATH, "//form/div[2]/button"))).click()
                time.sleep(10)
                assert False

        finally:
                driver.quit()