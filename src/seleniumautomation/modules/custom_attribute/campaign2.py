from seleniumautomation.constants import LocatorType, ElementFunction, GeneralLocators, CustomAttribute
from seleniumautomation.error import VegaAppException
from seleniumautomation.uitest import UiTest
from seleniumautomation.utils import SeleniumExecutor
import time
from selenium.webdriver.common.by import By

# This class is used to test the A360 profile page.
class TestCustomAttibute(UiTest, SeleniumExecutor):
    def campaign_attribute(self):
        browser = self.login()

        # Step 1: Locate and switch to the iframe
        try:
            # Replace 'iframe_xpath' with the actual XPath of the iframe
            iframe = browser.find_element(By.XPATH, "/html/body/bookmark-sidebar-fvcurrpok5k//iframe")
            browser.switch_to.frame(iframe)
            print("Switched to iframe successfully.")
        except Exception as e:
            raise VegaAppException(f"Failed to switch to iframe: {e}")

        # Step 2: Perform actions inside the iframe
        element_type_value = ([(LocatorType.XPATH, ElementFunction.CLICK_BUTTON, GeneralLocators.CDP_STUDIO, browser)],
                              [(LocatorType.XPATH, ElementFunction.CLICK_BUTTON, CustomAttribute.Launch, browser)])

        try:
            for element in element_type_value:
                self.execute_steps_list([element])
                time.sleep(5)
        except Exception as e:
            raise VegaAppException(f"Exception {e} occurred during A360 steps")

        # Step 3: Switch back to the main content after interactions
        browser.switch_to.default_content()
        print("Switched back to the main content.")

        return browser

    def test_campaign_attribute(self):
        browser = None
        browser = self.campaign_attribute()
