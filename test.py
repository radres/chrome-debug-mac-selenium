from selenium.webdriver.chrome.options import Options
from selenium import webdriver

import chromedriver_binary

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")


class Driver:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://google.com")


driver = Driver()
