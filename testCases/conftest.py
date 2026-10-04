import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
import pytest_html
from Utilities.read_properties import ReadProperties
base_url=ReadProperties.get_url()
# @pytest.fixture()
# def setup(browser):
#     if browser == "firefox":
#         driver = webdriver.Firefox()
#         driver.implicitly_wait(10)
#         driver.maximize_window()
#         driver.get(base_url)
#         return driver
#     elif browser == "chrome":
#         driver = webdriver.Chrome()
#         driver.implicitly_wait(10)
#         driver.maximize_window()
#         driver.get(base_url)
#         return driver
#     else:
#          driver = webdriver.Edge()
#          driver.maximize_window()
#          driver.implicitly_wait(10)
#          driver.get(base_url)
#          return driver
def pytest_addoption(parser):
    parser.addoption("--browser", action="store",default="edge")

@pytest.fixture()
def browser(request):
    browser = request.config.getoption("--browser")
    if browser=="edge":
        driver = webdriver.Edge()
    elif browser=="chrome":
        driver = webdriver.Chrome()
    elif browser=="firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError("Unknown browser,edge,chrome,firefox")
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(base_url)
    return driver
@pytest.fixture
def setup(browser):
    return browser
 ###code of pytest html###
def pytest_metadata(metadata):
   metadata["Project"] = "final nop commerce"
   metadata["Qa Engineer"] = "Abdullah Elmorsy"

# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("project name", None)
#     metadata.pop("tester", None)
