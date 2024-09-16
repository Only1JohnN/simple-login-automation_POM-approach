from selenium import webdriver
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self,driver:webdriver.Chrome):
        self.driver = driver
        
    def find_element(self, by:By, value:str):
        return self.driver.find_element(by, value)
    
    def get_current_url(self):
        return self.driver.current_url