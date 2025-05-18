import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LoginPage:
    username_input_field_xpath = "//input[@placeholder='Username']"
    password_input_field_xpath = "//*[@id='input_2']"
    next_button_xpath = "//*[text()='Next']"
    signIn_button_xpath = "//*[@id='login-form']/div[1]/form/div[2]/button"
    profile_button = "//*[@id='right-nav-toggle']"
    QA_regression = "//*[@id='tenant-id-40']/div/button"


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 50)

    def set_username(self, user_name):
        username_element_status = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.username_input_field_xpath)))
        assert username_element_status.is_enabled(), "User name Field is not Enabled"
        self.driver.find_element(By.XPATH, self.username_input_field_xpath).send_keys(user_name)
        next_button_status = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.next_button_xpath)))
        assert next_button_status.is_enabled(), "Next Button is not Enabled on Login Page"
        self.driver.find_element(By.XPATH, self.next_button_xpath).click()

    def set_password(self, password):
        password_element_status = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.password_input_field_xpath)))
        assert password_element_status.is_enabled(), "Password Field is not Enabled"
        self.driver.find_element(By.XPATH, self.password_input_field_xpath).send_keys(password)

    def click_on_signin_button(self):
        signin_button_status = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.signIn_button_xpath)))
        assert signin_button_status.is_enabled(), "Next Button is not Enabled on Login Page"
        self.driver.find_element(By.XPATH, self.signIn_button_xpath).click()
        time.sleep(3)
        # new_campaign_button_status = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.signIn_button_xpath)))
        # assert signin_button_status.is_enabled(), "Next Button is not Enabled on Login Page"

    def click_on_tenant_selection(self):
        self.driver.find_element(By.XPATH, self.profile_button).click()
        try:
            self.driver.execute_script("window.scrollBy(0,100);")
            qa_regression_element = self.driver.find_element(By.XPATH, self.QA_regression)
            self.driver.execute_script("arguments[0].scrollIntoView();", qa_regression_element)
        except Exception as e:
            print("The error is", e)
        time.sleep(5)
        qaregression_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.QA_regression))).click()
        print("selectTenant is Succesfull")



