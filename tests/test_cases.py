import pytest
from selenium import webdriver
from pages.home_page import HomePage
from pages.login_page import LoginPage

@pytest.fixture
def setup_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
    

def test_navigate_to_login_page(setup_driver):
    driver = setup_driver
    home_page = HomePage(driver)
    driver.get("https://practicetestautomation.com")
    
    home_page.navigate_to_login_page()
    
    assert "https://practicetestautomation.com/practice-test-login/" in home_page.get_current_url()
    
def test_login_page(setup_driver):
    driver = setup_driver
    login_page = LoginPage(driver)
    
    driver.get("https://practicetestautomation.com/practice-test-login/")
    
    login_page.username("student")
    login_page.password("Password123")
    login_page.click_submit()
    
    assert "https://practicetestautomation.com/logged-in-successfully/" in login_page.get_current_url()
    
    assert "Congratulations student." in login_page.get_page_source() or "You successfully logged in!" in login_page.get_page_source()
    assert login_page.logout_btn_displayed()
    
def test_negative_username(setup_driver):
    driver = setup_driver
    login_page = LoginPage(driver)
    
    driver.get("https://practicetestautomation.com/practice-test-login/")
    
    login_page.username("incorrectUser")
    login_page.password("Password123")
    login_page.click_submit()
    
    assert "Your username is invalid!" in login_page.error_message()
    

def test_negative_password(setup_driver):
    driver = setup_driver
    login_page = LoginPage(driver)
    
    driver.get("https://practicetestautomation.com/practice-test-login/")
    
    login_page.username("student")
    login_page.password("incorrectPassword")
    login_page.click_submit()
    
    assert "Your password is invalid!" in login_page.error_message()    
    