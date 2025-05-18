from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from configurations.credntials import Credentials
from configurations.env import Environment

import time
import allure
service_obj=Service()
driver= webdriver.Chrome(service=service_obj)
wait = WebDriverWait(driver, 30)

@allure.feature("A360")
@allure.story("Test Login")
@allure.title("Test if login  is successfull ")
def test_loginsession():
    environment= Environment
    driver.get(Environment.QA)
    element = wait.until(EC.presence_of_element_located((By.XPATH, "//form/md-input-container/input")))
    credentials = Credentials
    # Enter text into the input field
    element.send_keys(Credentials.username)
    element = wait.until(EC.presence_of_element_located((By.XPATH, "//form/div/button"))).click()
    element = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='input_2']"))).send_keys(
        Credentials.password)
    element = wait.until(EC.presence_of_element_located((By.XPATH, "//form/div[2]/button"))).click()
    print("Login Succesfull")

@allure.feature("A360")
@allure.story("Profile A360 profile search")
@allure.title("Test whether A 360 page is getting search with provided details")
def test_360_profile_search():
    element = wait.until(EC.presence_of_element_located((By.XPATH,"/html[1]/body[1]/div[2]/div[1]/div[1]/md-sidenav[1]/aside[1]/div[1]/ul[1]/li[1]/ul[1]/li[3]/menu-link[1]/a[1]"))).click()
    element = wait.until(EC.presence_of_element_located((By.XPATH,"/html[1]/body[1]/div[2]/div[1]/div[1]/md-content[1]/div[1]/div[1]/div[1]/div[1]/div[1]/md-whiteframe[1]/div[1]/md-input-container[3]/input[1]"))).send_keys("202208040801263_11336688542700__inpls515@yopmail.com")
    element = wait.until(EC.presence_of_element_located((By.XPATH,"/html[1]/body[1]/div[2]/div[1]/div[1]/md-content[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/button[2]/span[1]"))).click()
    time.sleep(6)
    element = wait.until(EC.presence_of_element_located((By.XPATH,"/html[1]/body[1]/div[2]/div[1]/div[1]/md-content[1]/div[1]/div[2]/div[1]/md-table-container[1]/table[1]/tbody[1]/tr[1]/td[4]"))).click()
    time.sleep(6)


@allure.feature("A360")
@allure.story("Profile A360 profile match")
@allure.title("Test whether A 360 profiles details are getting matched")
def test_360_profile_page():

    element = wait.until(EC.presence_of_element_located((By.XPATH,"/html[1]/body[1]/div[2]/div[1]/div[1]/md-content[1]/customer360-component[1]/div[1]/md-tabs[1]/md-tabs-wrapper[1]/md-tabs-canvas[1]/md-pagination-wrapper[1]/md-tab-item[2]/span[1]"))).click()

    time.sleep(5)

    expected_values1 = {
        "//div[@class='contentContainer']//div[2]//div[2]": "FTP_CSV_37_C-524568__20220804080126311336688443900",
        "//div[@class='contentContainer']//div[4]//div[2]": "Y",
        "//div[@class='contentContainer']//div[5]//div[2]": "X",
        "//div[@class='contentContainer']//div[6]//div[2]": "U",
        "//div[@class='contentContainer']//div[8]//div[2]": "331-951-4132",
        "//div[@class='contentContainer']//div[9]//div[2]": "Female",
        "//div[@class='contentContainer']//div[10]//div[2]": "Physical",
        "//div[@class='contentContainer']//div[11]//div[2]": "Org2",
        "//div[@class='contentContainer']//div[24]//div[2]": "FTP_CSV_37_C-524568__20220804080126311336688443900"

    }
    for element_locator1, expected_value1 in expected_values1.items():
        try:
            # Find the element on the webpage
            element = wait.until(EC.presence_of_element_located((By.XPATH, element_locator1)))

            # Get the actual value of the element
            actual_value1 = element.text  # You might need to adjust this based on your use case

            # Assert that the actual value matches the expected value
            assert actual_value1 == expected_value1, f"For Profiles Element value mismatch for {element_locator1}. Expected: {expected_value1}, Actual: {actual_value1}"
        finally:
            print("Test Completed for profiles")

        # except AssertionError as e:
        #     print(f"Assertion error: {e}")

@allure.feature("A360")
@allure.story("Profile A360 Identities  match")
@allure.title("Test whether A 360 Identities details are getting matched")

def test_360_identities_page():
    element = wait.until(EC.presence_of_element_located((By.XPATH,"/html[1]/body[1]/div[2]/div[1]/div[1]/md-content[1]/customer360-component[1]/div[1]/md-tabs[1]/md-tabs-wrapper[1]/md-tabs-canvas[1]/md-pagination-wrapper[1]/md-tab-item[6]/span[1]"))).click()

    time.sleep(10)

    expected_values2 = {

        "//span[@name='timeline-data-primarySubFields-displayValue-2-Source System ID']": "FTP_CSV_37",
        "//span[@name='timeline-data-primarySubFields-displayValue-0-ID']": "FTP_CSV_37_C-524568__20220804080126311336688443900",
        "//span[@name='timeline-data-primarySubFields-displayValue-3-Source Customer Number']": "C-524568__20220804080126311336688443900",
        "//span[@name='timeline-data-primarySubFields-displayValue-4-Email Opt-out']": "Y",
        "//span[@name='timeline-data-primarySubFields-displayValue-5-Direct Mail Opt-out']": "U",
        "//span[@name='timeline-data-primarySubFields-displayValue-6-Call Opt-out']": "N",
        # "//span[@class='timeline-data-primarySubFields-displayValue-8-Email Address']": "202208040801263_11336688542700__inpls515@yopmail.com",
        "//div[@class='smallValue ng-binding']": "Aug 5, 2022",
        "//div[@class='smallLabel ng-binding']": "5:26 PM IST"
    }
    for element_locator2, expected_value2 in expected_values2.items():
        try:
            # Find the element on the webpage
            element = wait.until(EC.presence_of_element_located((By.XPATH, element_locator2)))

            # Get the actual value of the element
            actual_value2 = element.text  # You might need to adjust this based on your use case

            # Assert that the actual value matches the expected value
            assert actual_value2 == expected_value2, f"For Identities Element value mismatch for {element_locator2}. Expected: {expected_value2}, Actual: {actual_value2}"
        finally:
            print("Test Completed for Identites")

@allure.feature("A360")
@allure.story("Profile A360 Household  match")
@allure.title("Test whether A 360 Household details are getting matched")
def test_360_household_page():
    element = wait.until(EC.presence_of_element_located((By.XPATH,"/html[1]/body[1]/div[2]/div[1]/div[1]/md-content[1]/customer360-component[1]/div[1]/md-tabs[1]/md-tabs-wrapper[1]/md-tabs-canvas[1]/md-pagination-wrapper[1]/md-tab-item[8]/span[1]"))).click()
    #
    time.sleep(5)
    expected_values3 = {

        "//md-whiteframe[2]//div[2]//div[2]": "$14,920.43",
        "//md-whiteframe[2]//div[3]//div[2]": "$14,920.43",
        "//md-whiteframe[2]//div[4]//div[2]": "$0.00",
        "//md-whiteframe[2]//div[5]//div[2]": "150.0",
        "//md-whiteframe[2]//div[6]//div[2]": "150.0",
        "//md-whiteframe[2]//div[7]//div[2]": "0.0",
        "//md-whiteframe[2]//div[8]//div[2]": "$746.14",
        "//md-whiteframe[2]//div[9]//div[2]": "$ 75-100",
        "//md-whiteframe[2]//div[10]//div[2]": "155.982906",
        "//md-whiteframe[2]//div[11]//div[2]": "351.0",
        "//md-whiteframe[2]//div[12]//div[2]": "351.0",
        "//md-whiteframe[2]//div[13]//div[2]": "351.0",
        "//md-whiteframe[2]//div[14]//div[2]": "2022-08-04 16:38:04.584",
        "//md-whiteframe[2]//div[15]//div[2]": "2022-08-04 16:38:04.649",
        "//md-whiteframe[2]//div[16]//div[2]": "NIKE",
        "//md-whiteframe[2]//div[17]//div[2]": "Physical",
        "//md-whiteframe[2]//div[18]//div[2]": "Org2",
        "//md-whiteframe[1]//div[2]//div[2]": "FTP_CSV_37_C-524568__20220804080126311336688443900"
    }
    for element_locator3, expected_value3 in expected_values3.items():
        try:
            # Find the element on the webpage
            element = wait.until(EC.presence_of_element_located((By.XPATH, element_locator3)))

            # Get the actual value of the element
            actual_value3 = element.text  # You might need to adjust this based on your use case

            # Assert that the actual value matches the expected value
            assert actual_value3 == expected_value3, f"For Household Element value mismatch for {element_locator3}. Expected: {expected_value3}, Actual: {actual_value3}"


        finally:

            print("Test Completed for Household")
@allure.feature("A360")
@allure.story("Profile A360 Transactions  match")
@allure.title("Test whether A 360 Transactions details are getting matched")
def test_360_trasnacations():
    element = wait.until(EC.presence_of_element_located((By.XPATH,"/html[1]/body[1]/div[2]/div[1]/div[1]/md-sidenav[1]/aside[1]/div[1]/ul[1]/li[1]/ul[1]/li[3]/menu-link[1]/a[1]"))).click()
    element = wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Clear']"))).click()
    element = wait.until(EC.presence_of_element_located((By.XPATH,"/html[1]/body[1]/div[2]/div[1]/div[1]/md-content[1]/div[1]/div[1]/div[1]/div[1]/div[1]/md-whiteframe[1]/div[1]/md-input-container[3]/input[1]"))).send_keys("202305303509899_62857725991020809__qoqvi146@yopmail.com")
    time.sleep(5)

    element = wait.until(EC.presence_of_element_located((By.XPATH,"/html[1]/body[1]/div[2]/div[1]/div[1]/md-content[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/button[2]/span[1]"))).click()
    element = wait.until(EC.presence_of_element_located((By.XPATH,"//tr[@class='pointer md-row ng-scope']//td[@class='md-cell ng-binding'][normalize-space()='Amber']"))).click()
    time.sleep(5)
    element = wait.until(EC.presence_of_element_located((By.XPATH,"/html[1]/body[1]/div[2]/div[1]/div[1]/md-content[1]/customer360-component[1]/div[1]/md-tabs[1]/md-tabs-wrapper[1]/md-tabs-canvas[1]/md-pagination-wrapper[1]/md-tab-item[4]/span[1]"))).click()
    element = wait.until(EC.presence_of_element_located((By.XPATH,"/html[1]/body[1]/div[2]/div[1]/div[1]/md-content[1]/customer360-component[1]/div[1]/div[1]/md-content[1]/div[1]/div[1]/div[2]/vega-timeline[1]/div[1]/div[1]/div[3]/div[1]/div[1]/md-card[1]/div[1]/div[2]/div[1]/div[4]/button[1]/md-icon[1]"))).click()
    time.sleep(5)

    expected_values4 = {

        "//div[normalize-space()='Shipping Revenue']": "$99.25",
        "//div[normalize-space()='Transaction Line Date']": "May 30, 2023 IST",
        "//div[normalize-space()='Brand Name']": "NIKE"
    }


    for element_locator4, expected_value4 in expected_values4.items():
        try:
            # Find the element on the webpage
            element = wait.until(EC.presence_of_element_located((By.XPATH, element_locator4)))

            # Get the actual value of the element
            actual_value4 = element.text  # You might need to adjust this based on your use case

            # Assert that the actual value matches the expected value
            assert actual_value4 == expected_value4, f"For Transactions Element value mismatch for {element_locator4}. Expected: {expected_value4}, Actual: {actual_value4}"

        finally:
            print("Test Completed for Transactions")
        #     print("---------------------------------------------")
        #     print("\n")
        #     print(f"Assertion error: {e}")