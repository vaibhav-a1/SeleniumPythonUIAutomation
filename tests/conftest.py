import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)
    # wait = WebDriverWait(driver, 50)
    return driver


# @pytest.fixture()
# def setup(browser):
#     if browser == 'chrome':
#         driver = webdriver.Chrome()
#     elif browser == 'ff':
#         driver = webdriver.Firefox()
#
#     driver.maximize_window()
#     driver.implicitly_wait(3)
#     # wait = WebDriverWait(driver, 50)
#     return driver


# @pytest.fixture(scope='session')
# def browser(request):
#     return request.config.getoption("--browser")
#
# @pytest.fixture(scope='session')
# def env(request):
#     return request.config.getoption("--env")
#
#
# def pytest_adoption(parser):  # this will get value from CMD/hooks
#     parser.addoption("--browser")
#     parser.addoption("--env")



