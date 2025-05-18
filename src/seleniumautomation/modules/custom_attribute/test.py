from seleniumautomation.constants import LocatorType, ElementFunction
from seleniumautomation.error import VegaAppException
from seleniumautomation.uitest import UiTest
from seleniumautomation.utils import SeleniumExecutor
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class TestDataExport(UiTest, SeleniumExecutor):
    def execute_data_export_recording(self):
        try:
            # Log into the application
            browser = self.login()

            # Set the browser window size


            # Navigate to the data export page


            # Click the "New Data Export" using text-based XPath
            self.click_element(By.XPATH, '//span[normalize-space(text())="New Data Export"]')

            # Enter the name for the data export
            self.enter_text(By.ID, "setupDataExportName", "TEST DE 1")

            # Click to proceed to the next step
            self.click_element(By.ID, "dataExportSetupNext")

            # Click on "Address"
            self.click_element(By.XPATH, '//button[contains(., "Address")]')

            # Toggle the first address checkbox
            self.click_element(By.XPATH, '//button/md-icon[contains(@class, "md-icon")]')

            # Continue with adding other data elements similarly, e.g., "Customer", "Transaction Item", etc.
            self.click_element(By.XPATH, '//button[contains(., "Customer")]')
            self.double_click_element(By.XPATH, '//button/md-icon[contains(@class, "md-icon")]')

            self.click_element(By.XPATH, '//button[contains(., "Transaction Item")]')
            self.click_element(By.XPATH, '//button/md-icon[contains(@class, "md-icon")]')

            self.click_element(By.XPATH, '//button[contains(., "Master Customer")]')
            self.double_click_element(By.XPATH, '//button/md-icon[contains(@class, "md-icon")]')

            # Proceed to the next step
            self.click_element(By.ID, "dataExportContentNext")

            # Select SFTP #2 from a dropdown
            self.click_element(By.ID, "select_value_label_369")
            self.click_element(By.XPATH, '//md-option[normalize-space(text())="SFTP #2"]')

            # Send the data export now
            self.click_element(By.ID, "dataExportSendNow")

            # Confirm the send action
            self.click_element(By.XPATH, '//button[contains(., "Send")]')

        finally:
            self.browser.quit()




    def click_element(self, by, value):
        """Wait for an element to be clickable, then click."""
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((by, value)))
        element.click()

    def enter_text(self, by, value, text):
        """Wait for an element to be visible, clear it, then send keys."""
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((by, value)))
        element.clear()
        element.send_keys(text)

    def double_click_element(self, by, value):
        """Wait for an element to be clickable, then double click."""
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((by, value)))
        webdriver.ActionChains(self.driver).double_click(element).perform()


# Instantiate and run the test
if __name__ == "__main__":
    test = TestDataExport()
    test.execute_data_export_recording()