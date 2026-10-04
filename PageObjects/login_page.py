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

    email_element=(By.XPATH, '//input[@class="email"]')
    password_element = (By.XPATH, '//input[@id="Password"]')
    login_button = (By.XPATH, '//button[text()="Log in"]')
    button = (By.XPATH, '//a[@href="/Admin"]')
    button2=(By.XPATH, '//i[@class="nav-icon far fa-user"]/parent::a')
    button3 = (By.XPATH, '//a[@href="/Admin/Customer/List"]')
    btn_add_new=(By.XPATH, '//a[@href="/Admin/Customer/Create"]')
    add_email=(By.XPATH, '//input[@id="Email"]')
    add_passowrd=(By.XPATH, '//input[@id="Password"]')
    add_firstname=(By.XPATH, '//input[@id="FirstName"]')
    add_lastname=(By.XPATH, '//input[@id="LastName"]')
    radio_btn_male=(By.XPATH, '//input[@id="Gender_Male"]')
    radio_btn_female=(By.XPATH, '//input[@id="Gender_Female"]')
    add_company=(By.XPATH, '//input[@id="Company"]')
    rm_click=(By.XPATH, '//span[@class="select2-selection__choice__remove"]')
    txt_customer_roles=(By.XPATH, '//label[contains(normalize-space(),"Customer roles")]/following::span[contains(@class,"select2-selection")][1]')
    lst_administrator=(By.XPATH, '//li[contains(text(),"Administrators")]')
    lst_registered=(By.XPATH, '//li[contains(text(),"Registered")]')
    lst_vendors=(By.XPATH, '//li[contains(text(),"Vendors")]')
    lst_guests=(By.XPATH, '//li[contains(text(),"Guests")]')
    lst_forum_moderators=(By.XPATH, '//li[contains(text(),"Forum Moderators")]')
    add_vendor=(By.XPATH, '//select[@id="VendorId"]')#//span[@id="select2-VendorId-container"]
    add_admin_comment=(By.XPATH, '//textarea[@name="AdminComment"]')
    btn_save=(By.XPATH, '//button[@name="save"]')
    # assertation area#
    email_asert=(By.XPATH, '//input[@id="SearchEmail"]')
    fname_asert = (By.XPATH, '//input[@id="SearchFirstName"]')
    lname_asert = (By.XPATH, '//input[@id="SearchLastName"]')
    btnsearch_asert = (By.XPATH, '//button[@id="search-customers"]')
    table_parent = (By.XPATH,"//table[contains(@class,'dataTable')][./tbody]")
    table_son=(By.XPATH,'//div[@id="customers-grid_wrapper"]//table[./tbody]')
    table_row=(By.XPATH,'//div[@id="customers-grid_wrapper"]//table[./tbody]/tbody/tr')
    table_column=(By.XPATH,'//div[@id="customers-grid_wrapper"]//table[./tbody]/tbody/tr[1]/td')
    def __init__(self, driver):
        self.driver = driver
    def login(self, email, password):
        self.driver.find_element(*self.email_element).clear()
        self.driver.find_element(*self.email_element).send_keys(email)
        self.driver.find_element(*self.password_element).clear()
        self.driver.find_element(*self.password_element).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()
    def login2(self):
        element1=self.driver.find_element(*self.button)
        element1.click()
    def login3(self):
        element1 = self.driver.find_element(*self.button2)
        element1.click()

        element2=self.driver.find_element(*self.button3)
        element2.click()
    def click_add_new(self):
        self.driver.find_element(*self.btn_add_new).click()
    def get_security(self,email2,password2):
        self.driver.find_element(*self.add_email).clear()
        self.driver.find_element(*self.add_email).send_keys(email2)
        self.driver.find_element(*self.add_passowrd).clear()
        self.driver.find_element(*self.add_passowrd).send_keys(password2)
    def get_all_names(self,firstname,lastname):
        self.driver.find_element(*self.add_firstname).clear()
        self.driver.find_element(*self.add_firstname).send_keys(firstname)
        self.driver.find_element(*self.add_lastname).clear()
        self.driver.find_element(*self.add_lastname).send_keys(lastname)
    def get_gender(self,gender):
        if gender=='Male':
            self.driver.find_element(*self.radio_btn_male).click()
        elif gender=='Female':
            self.driver.find_element(*self.radio_btn_female).click()

    def get_company_name(self,company):
        self.driver.find_element(*self.add_company).send_keys(company)
    # def get_customer_role(self,role):
    #     if role != "Registered":
    #
    #              self.driver.find_element(*self.rm_click).click()
        #
        #          self.driver.find_element(*self.txt_customer_roles).click()
        #
        #
        # if role=='Administrators':
        #    self.driver.find_element(*self.lst_administrator).click()
        # elif role=='Registered':
        #     self.driver.find_element(*self.lst_registered).click()
        # elif role=='Vendors':
        #    self.driver.find_element(*self.lst_vendors).click()
        # elif role=='Guests':
        #   self.driver.find_element(*self.lst_guests).click()

    def select_vendor(self,index):
        # WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(*self.add_vendor))
        select_dropdown = Select(self.driver.find_element(*self.add_vendor))
        select_dropdown.select_by_index(index)
    def get_admin_comments(self,comment):
        self.driver.find_element(*self.add_admin_comment).send_keys(comment)
    def click_save(self):
        self.driver.find_element(*self.btn_save).click()
    def assert_email(self,email):
        self.driver.find_element(*self.email_asert).send_keys(email)
    def assert_all_names(self,firstname,lastname):
        self.driver.find_element(*self.fname_asert).clear()
        self.driver.find_element(*self.fname_asert).send_keys(firstname)
        self.driver.find_element(*self.lname_asert).clear()
        self.driver.find_element(*self.lname_asert).send_keys(lastname)
    def click_search(self):
        self.driver.find_element(*self.btnsearch_asert).click()
    def get_num_rows(self):
        return len(self.driver.find_elements(*self.table_row))
    def get_num_columns(self):
        return len(self.driver.find_elements(*self.table_column))
    def customer_search_email(self,email):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,f'//div[@id="customers-grid_wrapper"]//tbody/tr[td[contains(normalize-space(),"{email}")]]')))
        return True

        # flag = False
        # for i in range(1,self.get_num_rows()+1):
        #     table = f"//div[@id='customers-grid_wrapper']/tbody/tr[{i}]/td[{2}"
        #     email_id=self.driver.find_element(By.XPATH,table).text
        #     if email==email_id:
        #         flag=True
        #         break
        # return flag
    def customer_search_names(self,firstname,lastname):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, f'//div[@id="customers-grid_wrapper"]//tbody/tr[td[contains(normalize-space(),"{firstname} {lastname}")]]')))
        return True


        

