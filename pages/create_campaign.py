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

from testdata.data import *
from utilities.userlib import *


class CreateCampaign():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 50)

    # Object repositories
    # new_campaign = "//*[@id='vegaFiles']/div[2]/div[6]/button"
    new_campaign = "//*[@id='vegaFiles']/div[2]/div[6]/button/span"
    # go_wild = //*[@id="campaignPlaybook"]/div[1]/div/md-whiteframe/md-card[2]/div/div[1]/img
    go_wild = "//img[@ng-src='https://images.agilone.com/aif/playbooks/GoWild.png']"
    search_box = "//*[@id='campaignChannel']/div[1]/div[1]/div/input"
    # search_box = "//input[@placeholder="Search"]"
    SFTP_output_search_result = "//*[@id='campaignChannel']/div[1]/div[2]/md-whiteframe/md-card/div/div[1]/img"
    # SFTP_output_search_result= "//img[@src='https://www.acquia.com/sites/default/files/integrations/FTP_CSV_210.png']"
    name_input_xpath = "//*[@id='campNewName']"
    next_button_xpath = "//*[text()='Next']"
    # add_group_xpath = "//*[@class='md-ripple-container']"
    add_group_xpath = "//*[@id='campaignAudience']/div[2]/div/div[1]/div[2]/div/button/span"
    search_rule = "//*[@name='dataset-selection-search-text']"
    search_rule_target_xpath = "//div[text()='First Transaction Date']"
    date_input = "//input[@aria-label='Enter date']"
    campaignAudienceNext = "//*[@id='campaignAudienceNext']/span"
    campaignABNext = "//*[@id='campaignABNext']"
    campaignContentNext = "//button[@id='campaignContentNext']"
    campaignDestinationFtpNext = "//button[@id='campaignDestinationFtpNext']"
    schedule_button = "//*[@id='scheduleFrame']//div[@class='md-container']"
    # schedule_send_dropdown = "//*[@id='select_494']" ;"//*[@class='interval-dropdown ng-pristine ng-valid ng-empty ng-touched']"
    schedule_send_dropdown = "(//md-select)[4]"
    schedule_MINUTES = "//div[text()='MINUTES']"
    schedule_send_every_dropdown = "(//md-select-value)[4]/span[2]"  # "//md-select-value[@class='md-select-value md-select-placeholder']/span[2]"
    schedule_send_every_15min = "//div[@class='md-text ng-binding' and text()='15']"
    schedule_date_input = "(//input[@class='md-datepicker-input'])[2]"
    schedule_time_input = "(//*[@class='md-input'])[2]"
    schedule_button = "//*[@id='scheduleFrame']//div[@class='md-container']"
    schedule_hours_4hours= "// div[text() = '4 hours']"
    schedule_send_dropdown = "(//md-select)[4]"
    schedule_ONCE = "//div[text()='ONCE']"
    schedule_MINUTES = "//div[text()='MINUTES']"
    schedule_HOURLY = "//div[text()='HOURLY']"
    schedule_DAILY = "//div[text()='DAILY']"
    schedule_WEEKLY = "//div[text()='WEEKLY']"
    schedule_MONTHLY = "//div[text()='MONTHLY']"
    schedule_send_every_dropdown = "(//md-select-value)[4]/span[2]"
    schedule_hours_dropdown = "(//md-select-value)[5]/span[2]"
    schedule_hours_fourhours = "//div[text()='4 hours']"
    schedule_send_every_15min = "//div[@class='md-text ng-binding' and text()='15']"
    schedule_date_input = "(//input[@class='md-datepicker-input'])[2]"
    schedule_time_input = "(//*[@class='md-input'])[2]"
    campaignSummarySave = "//button[@id='campaignSummarySave']"
    campaignSummaryClose = "//button[@id='campaignSummaryClose']/span"
    execution_calendar = "//a[@href='/execution-calendar']"
    timepickericon = "//md-icon[@aria-label='mdp-access-time']"
    Data_platforn_label_leftside_navigation = "//span[contains(normalize-space(), 'Data Platform')]"
    actions_leftside_navigation = "(//div[contains(normalize-space(), 'Actions')])[5]"
    actions_campaign_leftside_navigation = "//a[@href='/campaign']"
    actions_campaign_plusleftside_navigation = "//a[@href='/actions/campaign']"


    def create_campaign(self,newcampaignName):
        #campaign_create_folder=self.campaign_create_folder
        #selectUIAutomationExe = self.driver.execute_script(r'document.evaluate("{campaign_create_folder}", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE,null).singleNodeValue.scrollIntoView();')
        #self.driverdriver.find_element(campaign_create_folder).click()
        #print("selectUIAutomationExe is Succesfull")
        time.sleep(3)
        new_campaign_element = self.wait.until(EC.presence_of_element_located((By.XPATH,self.new_campaign))).click()
        time.sleep(5)
        go_wild_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.go_wild))).click()
        search_box_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.search_box))).send_keys(search_input_data)
        time.sleep(3)
        search_Result_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.SFTP_output_search_result))).click()
        name_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.name_input_xpath))).send_keys(newcampaignName)
        next_button_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.next_button_xpath))).click()
        time.sleep(3)
        add_group_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.add_group_xpath))).click()
        time.sleep(3)
        search_rule_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.search_rule))).send_keys(search_rule_input_data)
        select_rule_result_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.search_rule_target_xpath))).click()
        time.sleep(3)
        current_date=get_current_date()
        date_input_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.date_input))).send_keys(current_date)
        campaignAudienceNext_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.campaignAudienceNext))).click()
        time.sleep(3)
        campaignABNext_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.campaignABNext))).click()
        time.sleep(3)
        campaignContentNext_element = self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.campaignContentNext))).click()
        time.sleep(3)
        campaignDestinationFtpNext_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.campaignDestinationFtpNext))).click()
        time.sleep(5)
        print("create campaign is set Succesfull")

    def minutes_schedular(self):
        schedule_button_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.schedule_button))).click()
        time.sleep(3)
        schedule_send_dropdown_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.schedule_send_dropdown))).click()
        time.sleep(3)
        schedule_MINUTES_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.schedule_MINUTES))).click()
        time.sleep(3)
        schedule_send_every_dropdown_element = self.driver.find_element(By.XPATH, self.schedule_send_every_dropdown)
        self.driver.execute_script("arguments[0].click();", schedule_send_every_dropdown_element)
        time.sleep(3)
        schedule_send_every_15min_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.schedule_send_every_15min))).click()
        time.sleep(3)
        future_date=get_future_date()
        schedule_date_input_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.schedule_date_input))).send_keys(future_date)
        time.sleep(15)
        campaignSummarySave_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.campaignSummarySave))).click()
        time.sleep(3)
        campaignSummaryClose_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.campaignSummaryClose))).click()
        print("Minutes Schedular is set Succesfull")

    def hours_schedular(self):
        schedule_button_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.schedule_button))).click()
        time.sleep(3)
        schedule_send_dropdown_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.schedule_send_dropdown))).click()
        time.sleep(3)
        schedule_HOURLY_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.schedule_HOURLY))).click()
        time.sleep(3)
        self.driver.execute_script("document.evaluate('(//md-select-value)[5]/span[2]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click();")
        time.sleep(3)
        schedule_hours_4hours_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.schedule_hours_4hours))).click()
        time.sleep(3)
        future_date=get_future_date()
        schedule_date_input_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.schedule_date_input))).send_keys(future_date)
        time.sleep(15)
        campaignSummarySave_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.campaignSummarySave))).click()
        time.sleep(3)
        campaignSummaryClose_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.campaignSummaryClose))).click()
        print("Hours Schedular is set Succesfull")
    def once_schedular(self):
        schedule_button_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.schedule_button))).click()
        time.sleep(3)
        schedule_send_dropdown_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.schedule_send_dropdown))).click()
        time.sleep(3)
        schedule_HOURLY_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.schedule_ONCE))).click()
        future_date=get_future_date()
        schedule_date_input_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.schedule_date_input))).send_keys(future_date)
        time.sleep(15)
        campaignSummarySave_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.campaignSummarySave))).click()
        time.sleep(3)
        campaignSummaryClose_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.campaignSummaryClose))).click()
        print("once Schedular is set Succesfull")
    def weeks_schedular(self):
        schedule_button_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.schedule_button))).click()
        time.sleep(3)
        schedule_send_dropdown_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.schedule_send_dropdown))).click()
        time.sleep(3)
        schedule_HOURLY_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.schedule_WEEKLY))).click()
        future_date=get_future_date()
        schedule_date_input_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.schedule_date_input))).send_keys(future_date)
        time.sleep(15)
        campaignSummarySave_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.campaignSummarySave))).click()
        time.sleep(3)
        campaignSummaryClose_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.campaignSummaryClose))).click()
        print("weekly Schedular is set Succesfull")

    def days_schedular(self):
        schedule_button_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.schedule_button))).click()
        time.sleep(3)
        schedule_send_dropdown_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.schedule_send_dropdown))).click()
        time.sleep(3)
        schedule_HOURLY_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.schedule_DAILY))).click()
        future_date = get_future_date()
        schedule_date_input_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.schedule_date_input))).send_keys(future_date)
        time.sleep(15)
        campaignSummarySave_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.campaignSummarySave))).click()
        time.sleep(3)
        campaignSummaryClose_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.campaignSummaryClose))).click()
        print("Daily Schedular is set Succesfull")

    def months_schedular(self):
        schedule_button_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.schedule_button))).click()
        time.sleep(3)
        schedule_send_dropdown_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.schedule_send_dropdown))).click()
        time.sleep(3)
        schedule_HOURLY_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.schedule_MONTHLY))).click()
        future_date = get_future_date()
        schedule_date_input_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.schedule_date_input))).send_keys(future_date)
        time.sleep(15)
        campaignSummarySave_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.campaignSummarySave))).click()
        time.sleep(3)
        campaignSummaryClose_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.campaignSummaryClose))).click()
        print("Months Schedular is set Succesfull")