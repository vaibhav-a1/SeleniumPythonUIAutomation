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

# Locators
username_input_field_xpath = "//input[@placeholder='Username']"
# password_input_field_xpath = "//input[@name='password']"
password_input_field_xpath = "//*[@id='input_2']"
next_button_xpath = "//*[text()='Next']"
# signIn_button_xpath = "//*[text()='Sign In']"
signIn_button_xpath = "//*[@id='login-form']/div[1]/form/div[2]/button"
profile_button = "//*[@id='right-nav-toggle']"
QA_regression = "//*[@id='tenant-id-40']/div/button"
# new_campaign = "//*[@id='vegaFiles']/div[2]/div[6]/button"
new_campaign = "//*[@id='vegaFiles']/div[2]/div[6]/button/span"
# go_wild = //*[@id="campaignPlaybook"]/div[1]/div/md-whiteframe/md-card[2]/div/div[1]/img
go_wild = "//img[@ng-src='https://images.agilone.com/aif/playbooks/GoWild.png']"
search_box = "//*[@id='campaignChannel']/div[1]/div[1]/div/input"
# search_box = "//input[@placeholder="Search"]"
SFTP_output_search_result= "//*[@id='campaignChannel']/div[1]/div[2]/md-whiteframe/md-card/div/div[1]/img"
# SFTP_output_search_result= "//img[@src='https://www.acquia.com/sites/default/files/integrations/FTP_CSV_210.png']"
name_input_xpath = "//*[@id='campNewName']"
# add_group_xpath = "//*[@class='md-ripple-container']"
add_group_xpath = "//*[@id='campaignAudience']/div[2]/div/div[1]/div[2]/div/button/span"
search_rule = "//*[@name='dataset-selection-search-text']"
search_rule_target_xpath = "//div[text()='First Transaction Date']"
date_input= "//input[@aria-label='Enter date']"
campaignAudienceNext = "//*[@id='campaignAudienceNext']/span"
campaignABNext = "//*[@id='campaignABNext']"
campaignContentNext = "//button[@id='campaignContentNext']"
campaignDestinationFtpNext = "//button[@id='campaignDestinationFtpNext']"
schedule_button = "//*[@id='scheduleFrame']//div[@class='md-container']"
# schedule_send_dropdown = "//*[@id='select_494']" ;"//*[@class='interval-dropdown ng-pristine ng-valid ng-empty ng-touched']"
schedule_send_dropdown = "(//md-select)[4]"
schedule_MINUTES = "//div[text()='MINUTES']"
schedule_send_every_dropdown = "(//md-select-value)[4]/span[2]"    #"//md-select-value[@class='md-select-value md-select-placeholder']/span[2]"
schedule_send_every_15min = "//div[@class='md-text ng-binding' and text()='15']"
schedule_date_input = "(//input[@class='md-datepicker-input'])[2]"
schedule_time_input = "(//*[@class='md-input'])[2]"
campaignSummarySave = "//button[@id='campaignSummarySave']"
campaignSummaryClose = "//button[@id='campaignSummaryClose']/span"
execution_calendar = "//a[@href='/execution-calendar']"


# Testdata
username = "aruna.boddu@acquia.com"
password = "ArunaAgilOne@1"
search_input_data = "SFTP output connector for automation"
randomname = ''.join(random.choice(string.ascii_letters+string.digits) for i in range(10))
Campaign_successful_message = f"Campaign {randomname} is saved"
print(randomname)
print(Campaign_successful_message)
current_date = date.today().strftime("%m/%d/%Y")
print(current_date)
current_time = datetime.now().strftime("%H:%M")
current_time_pm = current_time + " P"
search_rule_input_data = "First Transaction Date"


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://qa-vega.agilone.com/login")
driver.maximize_window()
wait = WebDriverWait(driver, 50)
username_element = wait.until(EC.visibility_of_element_located((By.XPATH, username_input_field_xpath)))

username_input_field = driver.find_element(By.XPATH, username_input_field_xpath)
username_input_field.send_keys(username)

Next_button = driver.find_element(By.XPATH, next_button_xpath)
Next_button.click()
time.sleep(15)
password_element = wait.until(EC.presence_of_element_located((By.XPATH, password_input_field_xpath))).send_keys(password)
Signin_element = wait.until(EC.presence_of_element_located((By.XPATH, signIn_button_xpath))).click()
element = wait.until(EC.presence_of_element_located((By.XPATH, profile_button))).click()
time.sleep(10)
try:
    driver.execute_script("window.scrollBy(0,100);")
    qa_regression_element = driver.find_element(By.XPATH, QA_regression)
    driver.execute_script("arguments[0].scrollIntoView();", qa_regression_element)

except Exception as e:
    print("The error is", e)
time.sleep(5)
qaregression_element = wait.until(EC.presence_of_element_located((By.XPATH, QA_regression))).click()
# driver.find_element(By.XPATH, QA_regression).click()
time.sleep(8)
new_campaign_element = wait.until(EC.presence_of_element_located((By.XPATH, new_campaign))).click()
time.sleep(10)
go_wild_element = wait.until(EC.presence_of_element_located((By.XPATH, go_wild))).click()
search_box_element = wait.until(EC.presence_of_element_located((By.XPATH, search_box))).send_keys(search_input_data)
time.sleep(3)
search_Result_element = wait.until(EC.presence_of_element_located((By.XPATH, SFTP_output_search_result))).click()
name_element = wait.until(EC.presence_of_element_located((By.XPATH, name_input_xpath))).send_keys(randomname)
next_button_element = wait.until(EC.presence_of_element_located((By.XPATH, next_button_xpath))).click()
time.sleep(3)
add_group_element = wait.until(EC.presence_of_element_located((By.XPATH, add_group_xpath))).click()
time.sleep(3)
search_rule_element = wait.until(EC.presence_of_element_located((By.XPATH, search_rule))).send_keys(search_rule_input_data)
select_rule_result_element = wait.until(EC.presence_of_element_located((By.XPATH, search_rule_target_xpath))).click()
time.sleep(3)
date_input_element = wait.until(EC.presence_of_element_located((By.XPATH, date_input))).send_keys(current_date)
campaignAudienceNext_element = wait.until(EC.presence_of_element_located((By.XPATH, campaignAudienceNext))).click()
time.sleep(3)
campaignABNext_element = wait.until(EC.presence_of_element_located((By.XPATH, campaignABNext))).click()
time.sleep(3)
campaignContentNext_element = wait.until(EC.presence_of_element_located((By.XPATH, campaignContentNext))).click()
time.sleep(3)
campaignDestinationFtpNext_element = wait.until(EC.presence_of_element_located((By.XPATH, campaignDestinationFtpNext))).click()
time.sleep(5)
schedule_button_element = wait.until(EC.presence_of_element_located((By.XPATH, schedule_button))).click()
time.sleep(3)
schedule_send_dropdown_element = wait.until(EC.presence_of_element_located((By.XPATH, schedule_send_dropdown))).click()
time.sleep(3)
schedule_MINUTES_element = wait.until(EC.presence_of_element_located((By.XPATH, schedule_MINUTES))).click()
time.sleep(3)

schedule_send_every_dropdown_element = driver.find_element(By.XPATH,schedule_send_every_dropdown)
driver.execute_script("arguments[0].click();", schedule_send_every_dropdown_element)

time.sleep(3)
schedule_send_every_15min_element = wait.until(EC.presence_of_element_located((By.XPATH, schedule_send_every_15min))).click()
time.sleep(3)
schedule_date_input_element = wait.until(EC.presence_of_element_located((By.XPATH, schedule_date_input))).send_keys(current_date)
time.sleep(3)
target_element = driver.find_element(By.XPATH, schedule_time_input)
action_chain = ActionChains(driver)
action_chain.double_click(target_element).perform()
time.sleep(10)
driver.find_element(By.XPATH, schedule_time_input).clear()
time.sleep(15)
schedule_time_input_element = wait.until(EC.presence_of_element_located((By.XPATH, schedule_time_input))).send_keys(current_time_pm)
time.sleep(15)
campaignSummarySave_element = wait.until(EC.presence_of_element_located((By.XPATH, campaignSummarySave))).click()
time.sleep(3)
campaignSummaryClose_element = wait.until(EC.presence_of_element_located((By.XPATH, campaignSummaryClose))).click()

# assertEquals(driver.getPageSource().contains("email"), true);
execution_calendar_element = wait.until(EC.presence_of_element_located((By.XPATH, execution_calendar))).click()
time.sleep(15)
#assertEquals(driver.getPageSource().contains("email"), true);

# if driver.getPageSource().contains(randomname):
#     print("Calender successfully Scheduled with 15 min Test pass")
# else:
#     print("Calender successfully Scheduled with 15 min Test Fail")





