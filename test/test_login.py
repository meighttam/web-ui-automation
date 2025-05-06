import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage

def test_valid_login():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()

    login = LoginPage(driver)
    login.enter_username("Admin")
    login.enter_password("admin123")
    login.click_login()

    time.sleep(2)  # chwilowy stop na załadowanie (niezalecane, ale OK na start)
    
    assert "dashboard" in driver.current_url.lower() or "dashboard" in driver.page_source.lower()
    
    driver.quit()
