from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    def navigate_to_login_page(self):
        practice = self.find_element(By.XPATH, "//a[normalize-space()='Practice']")
        practice.click()
        
        test_login_page = self.find_element(By.XPATH, "//a[normalize-space()='Test Login Page']")
        test_login_page.click()