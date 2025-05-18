import logging

from seleniumautomation.constants import LocatorType, ElementFunction, CampaignPlusLocators, LocatorsLoginPage, GeneralLocators, Locators360, LocatorsMetrics
from seleniumautomation.error import VegaAppException
from seleniumautomation.uitest import UiTest

from seleniumautomation.utils import SeleniumExecutor

log = logging.getLogger(__name__)

class TestSSOLogin(UiTest, SeleniumExecutor):
    def test_login(self):
        browser = None
        try:
            url = "https://qa-vega.agilone.com/"
            # browser = self.get_browser_lambda(url, os.getenv('LAMBDA_TEST_USERNAME'),
            #                                   os.getenv('LAMBDA_TEST_ACCESS_KEY'))
            browser = self.get_browser_local(url)
            username = "vaibhav.verma@acquia.com"
            passw = "Vaibhav@3554"
            element_type_value = [
                (LocatorType.NAME, ElementFunction.ENTER_TEXT_IN_FIELD, LocatorsLoginPage.USERNAME_FIELD, browser,
                 username),
                (LocatorType.CSS, ElementFunction.CLICK_BUTTON, LocatorsLoginPage.LOGIN_BUTTON, browser),
                (LocatorType.NAME, ElementFunction.ENTER_TEXT_IN_FIELD, LocatorsLoginPage.PASSWORD_FIELD, browser,
                 passw),
                (LocatorType.CSS, ElementFunction.CLICK_BUTTON, LocatorsLoginPage.LOGIN_BUTTON, browser),
                (LocatorType.CSS, ElementFunction.CLICK_BUTTON, GeneralLocators.PROFILE_BUTTON, browser),
                (LocatorType.ID, ElementFunction.CLICK_BUTTON, 'tenant-id-3', browser)]
            self.execute_steps_list(element_type_value)
        except Exception as e:
            log.warning(f"Error Logging in. Error Message: {e}")
            if browser is not None:
                self.close_browser(browser)
            raise e
        return browser



    def test_login_invalid(self):
    # Test with valid credentials
        browser = None
    # Test with invalid username
        try:
            url = "https://qa-vega.agilone.com/"
            username = "vaibhav.verma@acquia.com"
            passw = "Vaibha3554"
            browser = self.get_browser_local(url)
            element_type_value = [
                (LocatorType.NAME, ElementFunction.ENTER_TEXT_IN_FIELD, LocatorsLoginPage.USERNAME_FIELD, browser,
                 username),
                (LocatorType.CSS, ElementFunction.CLICK_BUTTON, LocatorsLoginPage.LOGIN_BUTTON, browser),
                (LocatorType.NAME, ElementFunction.ENTER_TEXT_IN_FIELD, LocatorsLoginPage.PASSWORD_FIELD, browser,
                 passw),
                (LocatorType.CSS, ElementFunction.CLICK_BUTTON, LocatorsLoginPage.LOGIN_BUTTON, browser)]
            self.execute_steps_list(element_type_value)
        except Exception as e:
            log.warning(f"Error Logging in. Error Message: {e}")
            if browser is not None:
                self.close_browser(browser)
            raise e
        log.info("Invalid test completed")
        return browser