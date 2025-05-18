import logging
import time
from os import environ
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException,ElementNotInteractableException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.remote_connection import RemoteConnection
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

from seleniumautomation.constants import LocatorType, ElementFunction
from seleniumautomation.vega_utils import VegaSelenium

log = logging.getLogger(__name__)


class SeleniumExecutor:
    def execute_element_action(self, key_lookup_type, element_type, element_key, browser, element_value=None,
                               wait_time_in_sec=15, tries=0):
        key = None
        if key_lookup_type not in [LocatorType.NAME, LocatorType.CSS, LocatorType.CLASS, LocatorType.ID,
                                   LocatorType.XPATH]:
            raise ValueError(f"Found key look up type: {key_lookup_type} and element_type: {element_type}, "
                             f"but supported list for key look up type = [{LocatorType.CSS}, {LocatorType.NAME},"
                             f" {LocatorType.ID}, {LocatorType.CLASS},{LocatorType.XPATH}] ")
        vega_selenium = VegaSelenium()
        vega_selenium.wait_till_loading_completes(browser, wait_time_in_sec)
        try:
            key_lookup_type_map = {LocatorType.NAME: self.element_by_name,
                                   LocatorType.ID: self.element_by_id,
                                   LocatorType.CSS: self.element_by_css,
                                   LocatorType.CLASS: self.element_by_class,
                                   LocatorType.XPATH: self.element_by_xpath}
            key = key_lookup_type_map[key_lookup_type](element_key, wait_time_in_sec, browser)
        except Exception as e:
            if "text()=" not in element_key:
                log.info(f"Found an exception: {e} for locator type {element_type} and value {element_key}")
            raise e
        try:
            if key is not None:
                return vega_selenium.execute_action(element_type, element_value, element_key, key, browser)
            else:
                return ''
        except (StaleElementReferenceException, ElementClickInterceptedException, ElementNotInteractableException) as e:
            tries += 1
            if tries < 5:
                time.sleep(0.5)
                log.info(f"Retrying attempt : {tries}")
                self.execute_element_action(key_lookup_type, element_type, element_key, browser, tries=tries)
            else:
                log.info(f"Found an exception during execute_element_action: {e}")
                raise e
        except Exception as e:
            log.info(f"Found an exception during execute_element_action: {e}")
            raise e

    def execute_steps_list(self, _list):
        text = str()
        for element in _list:
            if element[1] == ElementFunction.ELEMENT_TEXT:
                text = self.execute_element_action(*element)
                time.sleep(5)
            else:
                self.execute_element_action(*element)
        return text

    def close_browser(self, browser):
        try:
            browser.quit()
        except Exception as e:
            print(f"Unable to close browser {browser}. Exception messsage: {e}")

    def switch_to_default_frame(self, browser):
        browser.switch_to_default_content()



# Use this function to run local tests
    def get_browser_local(self, url):
        options = Options()
        options.headless = False
        #browser = webdriver.Chrome(ChromeDriverManager().install("133.0.6943.127"), options=options)
        #browser = webdriver.Chrome(ChromeDriverManager(version="133.0.6943.127").install(), options=options)
        browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        #browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        browser.get(url)
        browser.maximize_window()
        return browser

    def get_browser_lambda(self, url, username, access_key):
        log.info("Trying with Lambda browser")
        desired_caps = {}

        browser = {
            "platform": "macOS Big Sur",
            "browserName": "chrome",
            "version": "93",
            "headless": False,
        }

        desired_caps.update(browser)
        test_name = "ml-qa"   #request.node.name
        build = environ.get('BUILD', "MLQA")
        # tunnel_id = environ.get('TUNNEL', False)
        selenium_endpoint = f"https://{username}:{access_key}@hub.lambdatest.com/wd/hub"
        desired_caps['build'] = build
        desired_caps['name'] = test_name
        executor = RemoteConnection(selenium_endpoint, resolve_ip=False)
        browser = webdriver.Remote(
            command_executor=executor,
            desired_capabilities=desired_caps
        )
        browser.get(url)
        return browser

    def element_by_name(self, element_key, wait_time_in_sec, browser):
        element_clickable = ec.element_to_be_clickable((By.NAME, element_key))
        WebDriverWait(browser, wait_time_in_sec).until(element_clickable)
        key = browser.find_element_by_name(element_key)
        return key

    def element_by_css(self, element_key, wait_time_in_sec, browser):
        element_clickable = ec.element_to_be_clickable((By.CSS_SELECTOR, element_key))
        WebDriverWait(browser, wait_time_in_sec).until(element_clickable)
        key = browser.find_element_by_css_selector(element_key)
        return key

    def element_by_xpath(self, element_key, wait_time_in_sec, browser):
        element_clickable = ec.element_to_be_clickable((By.XPATH, element_key))
        WebDriverWait(browser, wait_time_in_sec).until(element_clickable)
        key = browser.find_element_by_xpath(element_key)
        return key

    def element_by_id(self, element_key, wait_time_in_sec, browser):
        element_clickable = ec.element_to_be_clickable((By.ID, element_key))
        WebDriverWait(browser, wait_time_in_sec).until(element_clickable)
        key = browser.find_element_by_id(element_key)
        return key

    def element_by_class(self, element_key, wait_time_in_sec, browser):
        element_clickable = ec.element_to_be_clickable((By.CLASS_NAME, element_key))
        WebDriverWait(browser, wait_time_in_sec).until(element_clickable)
        key = browser.find_element_by_class_name(element_key)
        return key

    def get_text(self, key):
        text = key.text
        return text

    def click_button(self, key):
        key.click()
        return ""

    def send_to_field(self, key, element_value):
        key.send_keys(element_value)
        return ""

    def hover(self, browser, key):
        hover = ActionChains(browser).move_to_element(key)
        hover.perform()
        return ""
