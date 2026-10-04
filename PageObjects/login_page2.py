import time


from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select,WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
import pytest_html
class LoginPage:

    email_element=(By.XPATH, '//input[@placeholder="Username"]')
    password_element = (By.XPATH, '//input[@placeholder="Password"]')
    login_button = (By.XPATH, '//button[@type="submit"]')
    triangle_btn=(By.XPATH, '// i[@class ="oxd-icon bi-caret-down-fill oxd-userdropdown-icon"]')
    logout_btn=(By.XPATH,'//a[@href="/web/index.php/auth/logout"]')

    def __init__(self, driver):
      self.driver = driver


    def login(self, email, password):
     self.driver.find_element(*self.email_element).clear()
     self.driver.find_element(*self.email_element).send_keys(email)
     self.driver.find_element(*self.password_element).clear()
     self.driver.find_element(*self.password_element).send_keys(password)


    def click_login(self):
     self.driver.find_element(*self.login_button).click()
    def logout1(self):
     self.driver.find_element(*self.triangle_btn).click()
     self.driver.find_element(*self.logout_btn).click()