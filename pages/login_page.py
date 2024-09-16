from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def username(self, username:str):
        username_field = self.find_element(By.ID, "username")
        username_field.send_keys(username)
        
    def password(self, password:str):
        password_field = self.find_element(By.ID, "password")
        password_field.send_keys(password)
        
    def click_submit(self):
        submit_btn = self.find_element(By.ID, "submit")
        submit_btn.click()
        
    def get_page_source(self):
        return self.driver.page_source
    
    def logout_btn_displayed(self):
        return self.find_element(By.XPATH, "//a[normalize-space()='Log out']")
    
    def error_message(self):
        return self.find_element(By.ID, "error").text
    
         