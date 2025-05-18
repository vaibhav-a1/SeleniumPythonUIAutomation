import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from configurations.credntials import Credentials
from configurations.env import Environment
# import pandas as pd
# from GDPRWF import run_data
import http.client
import json
import ssl
from datetime import datetime
import time

from datetime import datetime, timedelta



import time
import allure

# from modules.QA.GDPRWF import run_data

service_obj=Service()
driver= webdriver.Chrome(service=service_obj)
wait = WebDriverWait(driver, 30)

@allure.feature("GDPR")
@allure.story("GDPR UI")
@allure.title("Test if able to access Data Erasure UI")
def test_gdpr():
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
    #element = wait.until(EC.presence_of_element_located((By.XPATH,"//a[href='/cdp/data-erasure']"))).click()
    #element = wait.until(EC.presence_of_element_located((By.XPATH,"//a[href='https://qa-vega.agilone.com/360profiles']"))).click()

   # element = wait.until(EC.presence_of_element_located((By.XPATH,"//a[text()=' Data Erasure ']"))).click()

    time.sleep(5)


@allure.feature("GDPR")
@allure.story("GDPR UI")
@allure.title("Test if able to create a request through Data Erasure UI")
def test_gdpr2():
    element=wait.until(EC.presence_of_element_located((By.XPATH,"/html[1]/body[1]/div[2]/div[1]/div[1]/md-sidenav[1]/aside[1]/div[1]/ul[1]/li[1]/ul[1]/li[8]/menu-link[1]/a[1]/span[1]"))).click()

    element=wait.until(EC.presence_of_element_located((By.XPATH,"/html[1]/body[1]/div[2]/div[1]/div[1]/md-sidenav[1]/aside[1]/div[1]/ul[1]/li[1]/ul[1]/li[8]/menu-link[1]/a[1]/span[1]"))).click()
    time.sleep(5)
    element=wait.until(EC.presence_of_element_located((By.XPATH,"/html[1]/body[1]/dxp-web-root[1]/dxp-web-mc-cdp-layout[1]/div[1]/div[2]/div[1]/dxp-mc-cdp-purge-web-list[1]/dxp-web-ui-page[1]/dxp-web-ui-page-header[1]/div[1]/div[1]/div[1]/dxp-web-ui-page-actions[1]/button[1]"))).click()
    time.sleep(5)
    element=wait.until(EC.presence_of_element_located((By.XPATH,"/html[1]/body[1]/dxp-web-root[1]/dxp-web-mc-cdp-layout[1]/div[1]/div[2]/div[1]/dxp-mc-cdp-purge-customer360-list[1]/dxp-web-ui-page[1]/dxp-mc-cdp-purge-customer360-search[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"))).send_keys("Mark")
    time.sleep(5)
    element=wait.until(EC.presence_of_element_located((By.XPATH,"/html[1]/body[1]/dxp-web-root[1]/dxp-web-mc-cdp-layout[1]/div[1]/div[2]/div[1]/dxp-mc-cdp-purge-customer360-list[1]/dxp-web-ui-page[1]/dxp-mc-cdp-purge-customer360-search[1]/form[1]/div[1]/button[1]"))).click()
    time.sleep(5)
    element=wait.until(EC.presence_of_element_located((By.XPATH,"/html[1]/body[1]/dxp-web-root[1]/dxp-web-mc-cdp-layout[1]/div[1]/div[2]/div[1]/dxp-mc-cdp-purge-customer360-list[1]/dxp-web-ui-page[1]/dxp-web-ui-state-container[1]/div[1]/div[2]/div[1]/p-table[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/p-tablecheckbox[1]/div[1]/div[2]"))).click()
    time.sleep(5)
    element=wait.until(EC.presence_of_element_located((By.XPATH,"/html[1]/body[1]/dxp-web-root[1]/dxp-web-mc-cdp-layout[1]/div[1]/div[2]/div[1]/dxp-mc-cdp-purge-customer360-list[1]/dxp-web-ui-page[1]/dxp-web-ui-state-container[1]/div[1]/div[1]/div[1]/div[1]/button[1]"))).click()
    time.sleep(5)
    element=wait.until(EC.presence_of_element_located((By.XPATH,"/html[1]/body[1]/dxp-web-root[1]/dxp-web-mc-cdp-layout[1]/div[1]/div[2]/div[1]/dxp-mc-cdp-purge-customer360-list[1]/dxp-web-ui-page[1]/dxp-web-ui-page-header[1]/div[1]/div[1]/div[1]/dxp-web-ui-page-actions[1]/button[1]/span[1]"))).click()
    time.sleep(5)
    # current_date = datetime.now()
    # desired_date = current_date
    # formatted_date=desired_date.strftime('%m/%d/%Y')
    # print(formatted_date)
    # # element=wait.until(EC.presence_of_element_located((By.XPATH,"/html[1]/body[1]/dxp-web-root[1]/dxp-web-mc-cdp-layout[1]/div[1]/div[2]/div[1]/dxp-mc-cdp-purge-data-erasure-review[1]/dxp-web-ui-page[1]/dxp-web-ui-page-body[1]/form[1]/p-calendar[1]/span[1]/div[1]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[3]/td[1]"))).send_keys(formatted_date)
    # time.sleep(5)
    # dateelement=driver.find_element(By.ID,"min-max")
    # dateelement.send_keys(formatted_date)
    # time.sleep(10)
    #
    # element=wait.until(EC.presence_of_element_located((By.XPATH,"/html[1]/body[1]/dxp-web-root[1]/dxp-web-mc-cdp-layout[1]/div[1]/div[2]/div[1]/dxp-mc-cdp-purge-data-erasure-review[1]/dxp-web-ui-page[1]/dxp-web-ui-page-actions[1]/div[1]/p[1]/button[1]")))
    # time.sleep(5)
    element=wait.until(EC.presence_of_element_located((By.ID,"min-max"))).click()
    element=wait.until(EC.presence_of_element_located((By.XPATH,"/html[1]/body[1]/dxp-web-root[1]/dxp-web-mc-cdp-layout[1]/div[1]/div[2]/div[1]/dxp-mc-cdp-purge-data-erasure-review[1]/dxp-web-ui-page[1]/dxp-web-ui-page-body[1]/form[1]/p-calendar[1]/span[1]/div[1]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[4]/span[1]"))).click()
    time.sleep(5)
    element=wait.until(EC.presence_of_element_located((By.XPATH,"/html[1]/body[1]/dxp-web-root[1]/dxp-web-mc-cdp-layout[1]/div[1]/div[2]/div[1]/dxp-mc-cdp-purge-data-erasure-review[1]/dxp-web-ui-page[1]/dxp-web-ui-page-actions[1]/div[1]/p[1]/button[1]"))).click()
    time.sleep(5)
    driver.quit()

@allure.feature("GDPR")
@allure.story("GDPR UI")
@allure.title("Test if API call Data Erasure WF completes successfully")
def test_gdpr_api():
    ssl._create_default_https_context = ssl._create_unverified_context

    conn = http.client.HTTPSConnection("qa-auth.agilone.com")
    payload = ''
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic dmFpYmhhdi52ZXJtYUBhY3F1aWEuY29tOlZhaWJoYXZAMzU1NA=='
    }
    conn.request("POST", "/authentication?action=login", payload, headers)
    res = conn.getresponse()
    x = res.read()
    data = x.decode("utf-8")
    values = json.loads(data)
    print(values)
    # print(db['teacher_db'][0]['name'])
    # for x in values:
    #     token=x["access_token"]
    token = values["access_token"]
    endpoint = "https://qa-api6.agilone.com/v2/3/orchstatus?limit=1&since="

    # headers = {"Authorization": "Bearer 3bf81688-8dbe-4d7d-91ad-c55e6c79d3ae"}
    #
    # headers = {"Authorization": "Bearer 77db82ac-e3f1-4c00-8417-7db299000e61"}

    conn1 = http.client.HTTPSConnection("qa-configapi.agilone.com")
    payload1 = ''
    headers1 = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer {}'.format(token)}
    conn1.request("GET", "/v2/3/orchstatus?limit=100&since=", payload1, headers1)
    res1 = conn1.getresponse()
    x1 = res1.read()
    data1 = x1.decode("utf-8")
    values1 = json.loads(data1)
    y1 = 0

    def run_data():
        conn1.request("POST", "/v2/3/config/workflows/DATA_ERASURE_DEFAULT?action=run", payload1, headers1)
        print("---------------------------------------")
        print("Running Data Erasure WF")
        res3 = conn1.getresponse()
        x3 = res3.read()
        data3 = x3.decode("utf-8")
        values3 = json.loads(data3)
        print(values3.get('eventId'))
        return values3

    run_data()

    def check_status():
        timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

        params = {
            "limit": "3",
            "since": timestamp
        }
        # conn1.request("GET", "/v2/3/orchstatus?limit=3&since={{$timestamp}}", headers1, params)
        response = requests.get("https://qa-api6.agilone.com/v2/3/orchstatus?", params=params, headers=headers1)

        # res4 = conn1.getresponse()
        # x4 = res4.read()
        # data4 = x4.decode("utf-8")
        # values4 = json.loads(data4)
        json_data = response.json()
        latest_entry = None
        latest_entry_status = None

        # Iterate through each entry in the JSON response
        for entry in json_data:
            if entry['workflowName'] == 'DATA_ERASURE_DEFAULT':
                # Check if this entry has the latest timestamp
                if latest_entry is None or datetime.strptime(entry['started'], '%m-%d-%Y %H:%M:%S') > datetime.strptime(
                        latest_entry['started'], '%m-%d-%Y %H:%M:%S'):
                    latest_entry = entry

        # If a latest entry with 'DATA_ERASURE_DEFAULT' workflowName is found
        if latest_entry:
            latest_entry_status = latest_entry['status']
            print("Latest status of DATA_ERASURE_DEFAULT:", latest_entry_status)
        else:
            print("No entry with workflowName 'DATA_ERASURE_DEFAULT' found in the response")

    while True:
        # Get the latest status
        status = check_status()

        # Check if the status is 'COMPLETED'
        if status == 'SUCCEEDED':
            print("Workflow status is COMPLETED. Exiting loop.")
            break

        # Wait for 60 seconds before pinging the URL again
        time.sleep(60)

    check_status()




# @allure.feature("GDPR")
# @allure.story("Test GDPR WF")
# @allure.title("Run the WF from the config")
# def test_gdpr3():
#     environment = Environment
#     driver.get(Environment.QA)
#     element = wait.until(EC.presence_of_element_located((By.XPATH, "//form/md-input-container/input")))
#     credentials = Credentials
#     # Enter text into the input field
#     element.send_keys(Credentials.username)
#     element = wait.until(EC.presence_of_element_located((By.XPATH, "//form/div/button"))).click()
#     element = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='input_2']"))).send_keys(Credentials.password)
#     element = wait.until(EC.presence_of_element_located((By.XPATH, "//form/div[2]/button"))).click()
#     element = wait.until(EC.presence_of_element_located((By.XPATH,"/html[1]/body[1]/div[2]/div[1]/div[1]/md-sidenav[1]/aside[1]/div[1]/ul[1]/li[1]/ul[1]/li[8]/menu-link[1]/a[1]/span[1]"))).click()
#
#     eventid= run_data()
#     print(eventid)
#     tables=pd.read_html(driver.get_page_source("https://qa-vega.agilone.com/cdp/data-erasure/status-list"))
#     tables=pd.read_html("https://qa-vega.agilone.com/cdp/data-erasure/status-list")
#     print(tables)
