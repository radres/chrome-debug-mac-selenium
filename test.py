import time
from typing import List
import sys
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.command import Command
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import chromedriver_binary

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

class Driver:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)

        self.driver.find_element(By.CSS_SELECTOR, """.fbt.analysis""").click()
        self.driver.find_element(By.CSS_SELECTOR, "table:nth-child(1)").find_element(By.CSS_SELECTOR,)click()
        self.driver.find_element(By.CSS_SELECTOR, ".add").click()
        self.driver.find_element(By.CSS_SELECTOR, "span:nth-child(1) > strong").click()

driver = Driver()
