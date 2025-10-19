from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get ("https://www.saucedemo.com/")

driver.quit()
