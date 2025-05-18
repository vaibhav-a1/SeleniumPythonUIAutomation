from seleniumautomation.constants import LocatorType, ElementFunction, GeneralLocators, CampaignPlusLocators
from seleniumautomation.error import VegaAppException
from seleniumautomation.uitest import UiTest
from seleniumautomation.utils import SeleniumExecutor
import time


class Testcampaigns(UiTest, SeleniumExecutor):
    def get_to_camp_page(self):
        browser = self.login()
        element_type_value = [
            (LocatorType.CSS, ElementFunction.CLICK_BUTTON, GeneralLocators.CAMPAIGNS_PLUS_BUTTON, browser),
            (LocatorType.CSS, ElementFunction.CLICK_BUTTON, CampaignPlusLocators.ADD_FOLDER_BUTTON, browser),
            (LocatorType.CSS, ElementFunction.ENTER_TEXT_IN_FIELD, CampaignPlusLocators.NEW_FOLDER_NAME_FIELD, browser,
             "Auto_Content23"),
            (LocatorType.CSS, ElementFunction.CLICK_BUTTON, CampaignPlusLocators.NEW_FOLDER_SAVE_BUTTON, browser),
            (LocatorType.XPATH, ElementFunction.CLICK_BUTTON, CampaignPlusLocators.AUTO_CONTENT_FOLDER, browser),
            (LocatorType.CSS, ElementFunction.CLICK_BUTTON, CampaignPlusLocators.NEW_CAMPAIGN_BUTTON, browser),
            (LocatorType.ID, ElementFunction.ENTER_TEXT_IN_FIELD, CampaignPlusLocators.NEW_CAMPAIGN_NAME_FIELD, browser,
             "CM_LastPrBrowsed_ProdStatus"),
            (LocatorType.ID, ElementFunction.CLICK_BUTTON, CampaignPlusLocators.NEW_CAMPAIGN_NEXT_BUTTON, browser),
            (LocatorType.CSS, ElementFunction.CLICK_BUTTON, CampaignPlusLocators.INCLUDE_BUTTON, browser),
            (LocatorType.XPATH, ElementFunction.CLICK_BUTTON, CampaignPlusLocators.CUSTOMER_ATTRIBUTES, browser),
            (LocatorType.XPATH, ElementFunction.CLICK_BUTTON, CampaignPlusLocators.CITY, browser),
            (LocatorType.CSS, ElementFunction.CLICK_BUTTON, CampaignPlusLocators.FILTER_TYPE_DROP_DOWN,
             browser),
            (LocatorType.CSS, ElementFunction.CLICK_BUTTON, CampaignPlusLocators.FILTER_TYPE_SELECT,
             browser),
            (LocatorType.CSS, ElementFunction.HOVER_OVER_ELEMENT, CampaignPlusLocators.MULTI_INPUT_HOVER_BUTTON,
             browser),
            (LocatorType.CSS, ElementFunction.CLICK_BUTTON, CampaignPlusLocators.MULTI_INPUT_BUTTON_MANUAL, browser),
            (LocatorType.CSS, ElementFunction.ENTER_TEXT_IN_FIELD, CampaignPlusLocators.VALUE_INPUT_FIELD_MANUAL,
             browser, "San Jose"),
            (LocatorType.CSS, ElementFunction.CLICK_BUTTON, CampaignPlusLocators.VALUE_INPUT_CONFIRM_BUTTON,
             browser),
            (LocatorType.CSS, ElementFunction.CLICK_BUTTON, CampaignPlusLocators.MAKE_PAGE_INTERACTABLE, browser),
            (LocatorType.ID, ElementFunction.CLICK_BUTTON, CampaignPlusLocators.CAMPAIGNS_AUDIENCE_NEXT, browser),
            (LocatorType.ID, ElementFunction.CLICK_BUTTON, CampaignPlusLocators.CAMPAIGN_BUILDER_NEXT, browser),
            (LocatorType.CSS, ElementFunction.CLICK_BUTTON, CampaignPlusLocators.ADD_CONTENT, browser),
            (LocatorType.XPATH, ElementFunction.CLICK_BUTTON, CampaignPlusLocators.LAST_PRODUCT_BROWSED, browser),
            (LocatorType.XPATH, ElementFunction.CLICK_BUTTON, CampaignPlusLocators.AVAILABILITY_STATUS, browser),
            (LocatorType.CSS, ElementFunction.CLICK_BUTTON, CampaignPlusLocators.APPLY_BUTTON, browser),
            (LocatorType.ID, ElementFunction.CLICK_BUTTON, CampaignPlusLocators.CAMPAIGN_CONTENT_NEXT, browser),
            (LocatorType.CSS, ElementFunction.CLICK_BUTTON, CampaignPlusLocators.NEW_BUTTON, browser),
            (LocatorType.XPATH, ElementFunction.CLICK_BUTTON, CampaignPlusLocators.TEST_STPF_CONNECTOR_SELECT, browser),
            (LocatorType.ID, ElementFunction.CLICK_BUTTON, CampaignPlusLocators.CAMPAIGN_DESTINATION_NEXT, browser),
            (LocatorType.CSS, ElementFunction.CLICK_BUTTON, CampaignPlusLocators.SEND_NOW_BUTTON, browser),
        ]

        try:
            for element in element_type_value:
             self.execute_step(element)
             time.sleep(5)
            return browser
        except Exception as e:
            raise VegaAppException(f"Exception {e} occurred during get_to_camp_page steps")

    def run_campaign(self):
        browser = None
        browser = self.get_to_camp_page()
        self.close_browser(browser)

    def test_campaign(self):
        self.run_campaign()

    def execute_step(self, element):
        locator_type, function, locator, browser, *args = element
        # Example logic for handling actions based on function
        if function == ElementFunction.CLICK_BUTTON:
            browser.find_element(locator_type.value, locator.value).click()
        elif function == ElementFunction.ENTER_TEXT_IN_FIELD:
            text = args[0]
            browser.find_element(locator_type.value, locator.value).send_keys(text)