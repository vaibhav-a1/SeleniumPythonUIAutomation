import string
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import random
from datetime import date
from datetime import datetime

import pages.create_campaign
from testdata.data import minutes, hours, once, weeks, months, day



class ExecutionCalender():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 50)

    # EC OR ***
    execution_calder_leftside_navigation = "//a[@href='/execution-calendar']"
    table_header = "//thead[@md-head]"

    def minutes_execution_calender(self, newcampaignName):
        elementScript = '''document.evaluate("//a[@href='/execution-calendar']", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.scrollIntoView()'''
        self.driver.execute_script(elementScript)
        execution_calendar_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.execution_calder_leftside_navigation))).click()
        execution_calendar_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.table_header)))
        targetExecutioncalenderRecordRow = self.driver.find_element(By.XPATH,f"//tbody/tr/td/span[@aria-label='{newcampaignName}']/../..")
        actualRecordText = targetExecutioncalenderRecordRow.text
        print(actualRecordText)
        time.sleep(5)
        assert newcampaignName in actualRecordText
        assert minutes in actualRecordText
        print("test_verifyminutesExecutionCalenderCampaign is Succesfull")
    def hours_execution_calender(self, newcampaignName):
        elementScript = '''document.evaluate("//a[@href='/execution-calendar']", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.scrollIntoView()'''
        self.driver.execute_script(elementScript)
        execution_calendar_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.execution_calder_leftside_navigation))).click()
        execution_calendar_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.table_header)))
        targetExecutioncalenderRecordRow = self.driver.find_element(By.XPATH,f"//tbody/tr/td/span[@aria-label='{newcampaignName}']/../..")
        actualRecordText = targetExecutioncalenderRecordRow.text
        print(actualRecordText)
        time.sleep(5)
        assert newcampaignName in actualRecordText
        assert hours in actualRecordText
        print("test_verifyhoursExecutionCalenderCampaign is Succesfull")
    def once_execution_calender(self, newcampaignName):
        elementScript = '''document.evaluate("//a[@href='/execution-calendar']", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.scrollIntoView()'''
        self.driver.execute_script(elementScript)
        execution_calendar_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.execution_calder_leftside_navigation))).click()
        execution_calendar_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.table_header)))
        targetExecutioncalenderRecordRow = self.driver.find_element(By.XPATH,f"//tbody/tr/td/span[@aria-label='{newcampaignName}']/../..")
        actualRecordText = targetExecutioncalenderRecordRow.text
        print(actualRecordText)
        time.sleep(5)
        assert newcampaignName in actualRecordText
        assert once in actualRecordText
        print("test_verifyonceExecutionCalenderCampaign is Succesfull")

    def weeks_execution_calender(self, newcampaignName):
        elementScript = '''document.evaluate("//a[@href='/execution-calendar']", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.scrollIntoView()'''
        self.driver.execute_script(elementScript)
        execution_calendar_element = self.wait.until(
        EC.presence_of_element_located((By.XPATH, self.execution_calder_leftside_navigation))).click()
        execution_calendar_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.table_header)))
        targetExecutioncalenderRecordRow = self.driver.find_element(By.XPATH,f"//tbody/tr/td/span[@aria-label='{newcampaignName}']/../..")
        actualRecordText = targetExecutioncalenderRecordRow.text
        print(actualRecordText)
        time.sleep(5)
        assert newcampaignName in actualRecordText
        assert weeks in actualRecordText
        print("test_verifyweeksExecutionCalenderCampaign is Succesfull")

    def months_execution_calender(self, newcampaignName):
        elementScript = '''document.evaluate("//a[@href='/execution-calendar']", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.scrollIntoView()'''
        self.driver.execute_script(elementScript)
        execution_calendar_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.execution_calder_leftside_navigation))).click()
        execution_calendar_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.table_header)))
        targetExecutioncalenderRecordRow = self.driver.find_element(By.XPATH,
                                                                    f"//tbody/tr/td/span[@aria-label='{newcampaignName}']/../..")
        actualRecordText = targetExecutioncalenderRecordRow.text
        print(actualRecordText)
        time.sleep(5)
        assert newcampaignName in actualRecordText
        assert months in actualRecordText
        print("test_verifyMonthsExecutionCalenderCampaign is Succesfull")

    def days_execution_calender(self, newcampaignName):
        elementScript = '''document.evaluate("//a[@href='/execution-calendar']", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.scrollIntoView()'''
        self.driver.execute_script(elementScript)
        execution_calendar_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.execution_calder_leftside_navigation))).click()
        execution_calendar_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.table_header)))
        targetExecutioncalenderRecordRow = self.driver.find_element(By.XPATH,f"//tbody/tr/td/span[@aria-label='{newcampaignName}']/../..")
        actualRecordText = targetExecutioncalenderRecordRow.text
        print(actualRecordText)
        time.sleep(5)
        assert newcampaignName in actualRecordText
        assert day in actualRecordText
        print("test_verifyDaysExecutionCalenderCampaign is Succesfull")
