from selenium import webdriver
import time
driver = webdriver.Edge()
driver.delete_all_cookies()
driver.get("https://localhost:59579/Admin/Customer/List")
time.sleep(30)
driver.quit()