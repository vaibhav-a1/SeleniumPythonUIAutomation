
from seleniumautomation.constants import LocatorType, ElementFunction, GeneralLocators, CustomAttribute
from seleniumautomation.error import VegaAppException
from seleniumautomation.uitest import UiTest
from seleniumautomation.utils import SeleniumExecutor
import time


##This class is used to test the a360 profiles age.
class TestCustomAttibute(UiTest, SeleniumExecutor):
    def campaign_attribute(self):
        browser = self.login()

        element_type_value = [(LocatorType.XPATH, ElementFunction.CLICK_BUTTON, GeneralLocators.CDP_STUDIO, browser),
                              (LocatorType.XPATH, ElementFunction.CLICK_BUTTON, CustomAttribute.Launch, browser),
                              (LocatorType.XPATH, ElementFunction.CLICK_BUTTON, CustomAttribute.TABLE_SELECT, browser),
                              (LocatorType.XPATH, ElementFunction.CLICK_BUTTON, CustomAttribute.ATTRIBUTE_SELECT, browser),
                                (LocatorType.XPATH, ElementFunction.CLICK_BUTTON, CustomAttribute.FORM_FIELD_2, browser)]



        try:
            for element in element_type_value:
                self.execute_steps_list([element])
                time.sleep(5)
            return browser
        except Exception as e:
            raise VegaAppException(f"Exception {e} occurred during a360 steps")

    def test_campaign_attribute(self):
        browser = None
        browser = self.campaign_attribute()
