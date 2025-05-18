import unittest
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException
from seleniumautomation.constants import LocatorType, ElementFunction, Locators360
from seleniumautomation.error import VegaAppException
from seleniumautomation.utils import SeleniumExecutor
from seleniumautomation.uitest import UiTest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class Test360ProfileNegativeScenarios(UiTest, SeleniumExecutor):
    def test_invalid_login(self):

        try:
            browser = self.login()
            self.fail("Login should have failed with invalid credentials")
        except VegaAppException as e:
            print(f"Expected failure: {e}")
        finally:
            self.close_browser(browser)

    def test_element_not_found(self):
        browser = self.login()
        element_type_value = [(LocatorType.CSS, ElementFunction.CLICK_BUTTON, "invalid_locator", browser)]
        try:
            self.execute_steps_list(element_type_value)
            self.fail("Test should have failed due to element not found")
        except NoSuchElementException as e:
            print(f"Expected failure: {e}")
        finally:
            self.close_browser(browser)

    def test_no_matching_customers(self):
        browser = self.login()
        element_type_value = [
            (LocatorType.NAME, ElementFunction.ENTER_TEXT_IN_FIELD, Locators360.CC, browser, "NonExistentCustomer"),
            (LocatorType.XPATH, ElementFunction.CLICK_BUTTON, Locators360.USERSELECT, browser)
        ]
        try:
            self.execute_steps_list(element_type_value)
            if "No matching customers found." in browser.page_source:
                print("No matching customers found.")
                raise Exception("Error: No matching customers found.")
        except Exception as e:
            print(f"Expected failure: {e}")
        finally:
            self.close_browser(browser)

    def test_element_not_clickable(self):
        browser = self.login()
        element_type_value = [(LocatorType.CSS, ElementFunction.CLICK_BUTTON, "unclickable_element", browser)]
        try:
            self.execute_steps_list(element_type_value)
            self.fail("Test should have failed due to element not clickable")
        except ElementClickInterceptedException as e:
            print(f"Expected failure: {e}")
        finally:
            self.close_browser(browser)

    def test_timeout_waiting_for_element(self):
        browser = self.login()
        element_type_value = [(LocatorType.CSS, ElementFunction.CLICK_BUTTON, "slow_loading_element", browser)]
        try:
            self.execute_steps_list(element_type_value)
            self.fail("Test should have failed due to timeout waiting for element")
        except TimeoutException as e:
            print(f"Expected failure: {e}")
        finally:
            self.close_browser(browser)

if __name__ == "__main__":
    unittest.main()