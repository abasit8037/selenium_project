import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('https://apps.lms.alnafi.com/authn/login')
    yield driver
    driver.quit()

def mycred():
    return [
        ('mybash29@gmail.com', 'Test!@12'),
        ('abubakrmuhammad271@gmail.com', 'abubakr1')
    ]

@pytest.mark.parametrize("username,password", mycred())
def test_login(driver, username, password):
    print("My pytest_login")
    driver.find_element(By.ID, 'emailOrUsername').send_keys(username)
    time.sleep(.7)
    driver.find_element(By.ID, 'password').send_keys(password)
    time.sleep(.5)
    print('Login Success')
