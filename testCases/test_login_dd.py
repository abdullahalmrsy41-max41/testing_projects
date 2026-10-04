import time
from email.mime import nonmultipart

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
import pytest_html
from PageObjects.login_page2 import LoginPage
from Utilities.read_properties import ReadProperties
from Utilities.customlogger import CustomLogger
from Utilities import Exelutils
class TestLogin:
    path=".//TestData/orange.xlsx"
    final_result=[]
    logger=CustomLogger.method_logger()
    @pytest.mark.sanity
    def test_login_page(self,setup):
        self.logger.info("***** with dd excel data *****")
        self.driver = setup
        self.lp=LoginPage(self.driver)
        self.rows=Exelutils.getRowCount(self.path,"Sheet1")
        for i in range(2,self.rows+1):
            self.email=Exelutils.readData(self.path,"Sheet1",i,1)
            self.password=Exelutils.readData(self.path,"Sheet1",i,2)
            self.expected=Exelutils.readData(self.path,"Sheet1",i,3)
            self.lp.login(self.email, self.password)
            self.lp.click_login()
            act_title = self.driver.title
            exp_title ="OrangeHRM"
            if"dashboard" in self.driver.current_url.lower():
                if self.expected=="pass":#true
                    self.logger.info("***** passed!!! *****")
                    self.lp.logout1()
                    time.sleep(2)
                    self.final_result.append("pass")
                elif self.expected=="fail" :
                    self.logger.info("***** failed!!! *****")
                    self.lp.logout1()
                    time.sleep(2)
                    self.final_result.append("fail")
            else:
                if self.expected=="pass" :
                    self.logger.info("*****failed!!!******")
                    self.final_result.append("fail")
                elif self.expected=="fail" :#true
                    self.logger.info("*****passed!!!*******")
                    self.final_result.append("pass")

            self.driver.delete_all_cookies()
        if "fail" in self.final_result:
                self.logger.info("*****failed!!!******* ")
                self.driver.close()
                assert False
        else:
                self.logger.info("*****passed!!!******* ")
                self.driver.close()
                assert True

        self.logger.info("**** test is completed *****")

        print(self.final_result)