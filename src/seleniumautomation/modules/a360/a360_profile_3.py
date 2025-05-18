from seleniumautomation.constants import LocatorType, ElementFunction, GeneralLocators, Locators360
from seleniumautomation.error import VegaAppException
from seleniumautomation.uitest import UiTest
from seleniumautomation.utils import SeleniumExecutor
import time

##This class is used to test the a360 profiles age.

class Test360Profile(UiTest, SeleniumExecutor):
    def  a360_profile(self):
        browser = self.login()
        element_type_value = [(LocatorType.CSS, ElementFunction.CLICK_BUTTON, GeneralLocators.BUTTON_360, browser),
                              ]

        try:
            for element in element_type_value:

                self.execute_steps_list([element])
                time.sleep(5)
            return browser
        except Exception as e:
            raise VegaAppException(f"Exception {e} occurred during a360 steps")




    def a360_search(self,browser):
        element_type_value = [(LocatorType.NAME, ElementFunction.ENTER_TEXT_IN_FIELD, Locators360.SCN, browser,"C-644161__202408051226140561126443663400"),
                              (LocatorType.XPATH, ElementFunction.CLICK_BUTTON, Locators360.USERSELECT, browser),
                              (LocatorType.XPATH, ElementFunction.CLICK_BUTTON, Locators360.USER, browser)
                              ]
        try:
            for element in element_type_value:
                self.execute_steps_list([element])
                time.sleep(5)


            return browser
        except Exception as e:
            raise VegaAppException(f"Exception {e} occurred during a360 steps")

    def a360_tab(self,browser):
        element_type_value = [(LocatorType.XPATH, ElementFunction.CLICK_BUTTON, Locators360.PROFILE,browser),
                              (LocatorType.XPATH, ElementFunction.CLICK_BUTTON, Locators360.JOURNEY, browser),
                              (LocatorType.XPATH, ElementFunction.CLICK_BUTTON, Locators360.TRANS, browser),
                              (LocatorType.XPATH, ElementFunction.CLICK_BUTTON, Locators360.ML, browser),
                              (LocatorType.XPATH, ElementFunction.CLICK_BUTTON, Locators360.IDENTITIES, browser),
                              (LocatorType.XPATH, ElementFunction.CLICK_BUTTON, Locators360.SUBS, browser),
                              (LocatorType.XPATH, ElementFunction.CLICK_BUTTON, Locators360.HOUSEHOLD, browser),
                              (LocatorType.XPATH, ElementFunction.CLICK_BUTTON, Locators360.MC, browser)
                              ]

        try:
            for element in element_type_value:
                self.execute_steps_list([element])
                time.sleep(5)


            return browser
        except Exception as e:
            raise VegaAppException(f"Exception {e} occurred during a360 steps")




    def test_parent(self):
        browser = None
        browser = self.a360_profile()
        print("Test Case- 1 Passed")
        browser = self.a360_search(browser)
        print("Test Case- 2 Passed")
        browser = self.a360_tab(browser)
        print("Test Case- 3 Passed")
        self.close_browser(browser)


