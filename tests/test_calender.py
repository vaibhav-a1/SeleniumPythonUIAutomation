import time
import allure
import six
import unittest
import pytest
import allure_pytest

from pages.create_campaign import *
from pages.executioncalender import *
from pages.loginpage import *
from utilities.userlib import *
from utilities.readconfigfile import *
from testdata.data import *
from selenium import webdriver

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import random
from datetime import date
from datetime import datetime
from utilities.readconfigfile import ConfigData
from pages.loginpage import LoginPage
from pages.create_campaign import *
from pages.executioncalender import *


# Locators

# # new_campaign = "//*[@id='vegaFiles']/div[2]/div[6]/button"
# new_campaign = "//*[@id='vegaFiles']/div[2]/div[6]/button/span"
# # go_wild = //*[@id="campaignPlaybook"]/div[1]/div/md-whiteframe/md-card[2]/div/div[1]/img
# go_wild = "//img[@ng-src='https://images.agilone.com/aif/playbooks/GoWild.png']"
# search_box = "//*[@id='campaignChannel']/div[1]/div[1]/div/input"
# # search_box = "//input[@placeholder="Search"]"
# SFTP_output_search_result= "//*[@id='campaignChannel']/div[1]/div[2]/md-whiteframe/md-card/div/div[1]/img"
# # SFTP_output_search_result= "//img[@src='https://www.acquia.com/sites/default/files/integrations/FTP_CSV_210.png']"
# name_input_xpath = "//*[@id='campNewName']"
# # add_group_xpath = "//*[@class='md-ripple-container']"
# add_group_xpath = "//*[@id='campaignAudience']/div[2]/div/div[1]/div[2]/div/button/span"
# search_rule = "//*[@name='dataset-selection-search-text']"
# search_rule_target_xpath = "//div[text()='First Transaction Date']"
# date_input= "//input[@aria-label='Enter date']"
# campaignAudienceNext = "//*[@id='campaignAudienceNext']/span"
# campaignABNext = "//*[@id='campaignABNext']"
# campaignContentNext = "//button[@id='campaignContentNext']"
# campaignDestinationFtpNext = "//button[@id='campaignDestinationFtpNext']"
# schedule_button = "//*[@id='scheduleFrame']//div[@class='md-container']"
# # schedule_send_dropdown = "//*[@id='select_494']" ;"//*[@class='interval-dropdown ng-pristine ng-valid ng-empty ng-touched']"
# schedule_send_dropdown = "(//md-select)[4]"
# schedule_MINUTES = "//div[text()='MINUTES']"
# schedule_send_every_dropdown = "(//md-select-value)[4]/span[2]"    #"//md-select-value[@class='md-select-value md-select-placeholder']/span[2]"
# schedule_send_every_15min = "//div[@class='md-text ng-binding' and text()='15']"
# schedule_date_input = "(//input[@class='md-datepicker-input'])[2]"
# schedule_time_input = "(//*[@class='md-input'])[2]"
# campaignSummarySave = "//button[@id='campaignSummarySave']"
# campaignSummaryClose = "//button[@id='campaignSummaryClose']/span"
# execution_calendar = "//a[@href='/execution-calendar']"


# Testdata
# base_url = ConfigData.get_application_url()
# username = "aruna.boddu@acquia.com"
# password = "ArunaAgilOne@1"
# search_input_data = "SFTP output connector for automation"
# randomname = ''.join(random.choice(string.ascii_letters+string.digits) for i in range(10))
# Campaign_successful_message = f"Campaign {randomname} is saved"
# print(randomname)
# print(Campaign_successful_message)
# current_date = date.today().strftime("%m/%d/%Y")
# print(current_date)
# current_time = datetime.now().strftime("%H:%M")
# current_time_pm = current_time + " P"
# search_rule_input_data = "First Transaction Date"
# future_date = get_future_date()

# driver = webdriver.Chrome()

# wait = WebDriverWait(driver, 10)
# newcampaignName = randomname
# wait = WebDriverWait(driver, 50)

class TestExecutionCalender:
    base_url = ConfigData.get_application_url()
    username = ConfigData.get_user_name()
    pwd = ConfigData.get_password()
    campaign_name=get_randome_name()

    @allure.feature("calender")
    @allure.story("Test Login")
    @allure.title("Test if login  is successful")
    def test_login_session(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        login_page = LoginPage(self.driver)
        login_page.set_username(self.username)
        login_page.set_password(self.pwd)
        login_page.click_on_signin_button()

    @allure.feature("calender")
    @allure.story("create_campaign")
    @allure.title("test_verify_minutes_scdlr  is successful")
    def test_verify_minutes_scdlr(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        lp = LoginPage(self.driver)
        lp.set_username(self.username)
        lp.set_password(self.pwd)
        lp.click_on_signin_button()
        lp.click_on_tenant_selection()
        cp = CreateCampaign(self.driver)
        #cp.select_folder_listing_page()
        cp.create_campaign(self.campaign_name)
        time.sleep(3)
        cp.minutes_schedular()
        ec = ExecutionCalender(self.driver)
        ec.minutes_execution_calender(self.campaign_name)
    @allure.feature("calender")
    @allure.story("create_campaign")
    @allure.title("test_verify_minutes_scdlr  is successful")
    def test_verify_hours_scdlr(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        lp = LoginPage(self.driver)
        lp.set_username(self.username)
        lp.set_password(self.pwd)
        lp.click_on_signin_button()
        lp.click_on_tenant_selection()
        cp = CreateCampaign(self.driver)
        # cp.select_folder_listing_page()
        cp.create_campaign(self.campaign_name)
        time.sleep(3)
        cp.hours_schedular()
        ec = ExecutionCalender(self.driver)
        ec.hours_execution_calender(self.campaign_name)

    @allure.feature("calender")
    @allure.story("create_campaign")
    @allure.title("test_verify_once_scdlr is successful")
    def test_once_schedular(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        lp = LoginPage(self.driver)
        lp.set_username(self.username)
        lp.set_password(self.pwd)
        lp.click_on_signin_button()
        lp.click_on_tenant_selection()
        cp = CreateCampaign(self.driver)
        # cp.select_folder_listing_page()
        cp.create_campaign(self.campaign_name)
        time.sleep(3)
        cp.once_schedular()
        ec = ExecutionCalender(self.driver)
        ec.once_execution_calender(self.campaign_name)




    @allure.feature("calender")
    @allure.story("create_campaign")
    @allure.title("test_verify_weeks_scdlr is successful")
    def test_weeks_schedular(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        lp = LoginPage(self.driver)
        lp.set_username(self.username)
        lp.set_password(self.pwd)
        lp.click_on_signin_button()
        lp.click_on_tenant_selection()
        cp = CreateCampaign(self.driver)
        # cp.select_folder_listing_page()
        cp.create_campaign(self.campaign_name)
        time.sleep(3)
        cp.weeks_schedular()
        ec = ExecutionCalender(self.driver)
        ec.weeks_execution_calender(self.campaign_name)

    @allure.feature("calender")
    @allure.story("create_campaign")
    @allure.title("test_verify_days_scdlr is successful")
    def test_days_schedular(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        lp = LoginPage(self.driver)
        lp.set_username(self.username)
        lp.set_password(self.pwd)
        lp.click_on_signin_button()
        lp.click_on_tenant_selection()
        cp = CreateCampaign(self.driver)
        # cp.select_folder_listing_page()
        cp.create_campaign(self.campaign_name)
        time.sleep(3)
        cp.days_schedular()
        ec = ExecutionCalender(self.driver)
        ec.days_execution_calender(self.campaign_name)


