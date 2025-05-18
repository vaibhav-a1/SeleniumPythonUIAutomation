import logging

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.seleniumautomation.constants import GeneralLocators, ElementFunction

log = logging.getLogger(__name__)


class VegaSelenium:
    def wait_till_loading_completes(self, browser, wait_time_in_sec):
        loading_bar_absent = EC.invisibility_of_element((By.ID, GeneralLocators.LOADING_BAR))
        WebDriverWait(browser, wait_time_in_sec).until(loading_bar_absent)
        loading_bar_absent = EC.invisibility_of_element((By.ID, GeneralLocators.LOADING_BAR_SPINNER))
        WebDriverWait(browser, wait_time_in_sec).until(loading_bar_absent)

    def action_on_list(self, key, element_key, element_value, browser, action):
        wait_time_in_sec = 10
        try:
            element_clickable = EC.element_to_be_clickable((By.CSS_SELECTOR, element_key))
            WebDriverWait(browser, wait_time_in_sec).until(element_clickable)
            _list = browser.find_elements_by_css_selector(element_key)
            text_list = []
            for loc_key in _list:
                if action == ElementFunction.ENTER_TEXT_IN_FIELD:
                    loc_key.send_keys(element_value)
                elif action == ElementFunction.CLICK_BUTTON:
                    loc_key.click()
                elif action == ElementFunction.GET_COUNT:
                    if not _list:
                        log.warning("received None from VegaApp")
                        return 0
                    else:
                        return len(_list)
                else:
                    text_list.append(loc_key.text)
            return text_list
        except Exception as e:
            log.warning(f"Exception {e} occurred in function element_by_list")
            return []

    def execute_action(self, element_type, element_value, element_key, key, browser, action=None):
        test_text = str()
        # print("Key found :" + key.tag_name)
        # Perform an action with the element
        action_map = {
            ElementFunction.ENTER_TEXT_IN_FIELD: self.send_text,
            ElementFunction.CLEAR_FIELD: self.clear_field,
            ElementFunction.SWITCH_FRAME: self.switch_frame,
            ElementFunction.CLICK_BUTTON: self.click,
            ElementFunction.HOVER_OVER_ELEMENT: self.hover,
            ElementFunction.ELEMENT_TEXT: self.read_text,
            ElementFunction.ACTIONS_ON_LIST: self.action_on_list
        }
        test_text = action_map[element_type](key, element_key, element_value, browser, action)
        return test_text

    def click(self, key, element_key, element_value, browser, action):
        key.click()

    def read_text(self, key, element_key, element_value, browser, action):
        test_text = key.text
        return test_text

    def clear_field(self, key, element_key, element_value, browser, action):
        key.send_keys(Keys.CONTROL + "a")
        key.send_keys(Keys.DELETE)

    def hover(self, key, element_key, element_value, browser, action):
        hover = ActionChains(browser).move_to_element(key)
        hover.perform()

    def send_text(self, key, element_key, element_value, browser, action):
        key.send_keys(element_value)

    def switch_frame(self, key, element_key, element_value, browser, action):
        browser.switch_to.frame(element_key)