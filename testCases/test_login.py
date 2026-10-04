import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
import random,string
import pytest_html
from PageObjects.login_page import LoginPage
from Utilities.read_properties import ReadProperties
from Utilities.customlogger import CustomLogger
def random_generator(size=8, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
class TestLogin:
    cus_email=random_generator()+"@gmail.com"
    email = ReadProperties.get_email()
    password=ReadProperties.get_password()
    logger=CustomLogger.method_logger()
    @pytest.mark.regressions
    def test_home_page_title(self,setup):
        self.driver = setup
        self.lp = LoginPage(self.driver)
        self.lp.login(self.email ,self.password)
        self.lp.click_login()
        self.lp.login2()
        self.lp.login3()
        self.lp.click_add_new()
        self.logger.info("** providing customer id**")
        self.lp.get_security(self.cus_email,"123456")
        self.lp.get_all_names("ali2","osama")
        self.lp.get_gender("Male")
        self.lp.get_company_name("Elmansoura")
        # self.lp.get_customer_role("Guests")
        self.lp.select_vendor(1)
        self.lp.get_admin_comments("I will try more and more till achieve my goals with all my efforts")
        self.lp.click_save()
        self.logger.info("**End providing customer id**")
        self.logger.info("**End searching customer id**")
        # self.lp.assert_email(self.cus_email)
        self.lp.assert_all_names("ali2","osama")
        self.lp.click_search()
        # status=self.lp.customer_search_email(self.cus_email)
        status = self.lp.customer_search_names("ali2","osama")


        act_title=self.driver.title
        if act_title=="Customers / nopCommerce administration" and status==True:
            self.logger.info("**test is successful**")
            self.driver.save_screenshot(".\\screenshots1\\customer2.png")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots1\\customer.png")
            assert False


        # act_title = self.driver.title
        # # self.driver.close()
        # if act_title=="":
        #   self.logger.info("***** case is passed *****")
        #   self.driver.close()
        #   assert True
        #
        # else:
        #     self.logger.info("***** case is failed *****")
        #     self.driver.save_screenshot(".\\screenshots1\\automation.png")
        #     assert False
    # def test_login_page(self,setup):
    #     self.driver = setup
    #     self.lp=LoginPage(self.driver)
    #     self.lp.login(self.email ,self.password)
    #     self.lp.click_login()
    #     act_title=self.driver.title
    #     self.lp.logout1()
    #     self.driver.close()
    #     if act_title=="OrangeHRM":
    #       self.logger.info("***** case is passed *****")
    #       assert True
    #     else:
    #        self.driver.save_screenshot(".\\screenshots1\\automation.png")
    #        self.logger.info("***** case is failed because of website (cloud flare)*****")
    #        assert False
