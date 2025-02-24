import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.login_popup import LoginPopup
from test_login import test_login as TL

def test_login(driver):
    login_popup = LoginPopup(driver)
    login_popup.click_open_login_popup()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(login_popup.LOGIN_BUTTON))

    login_popup.enter_username("username")
    login_popup.enter_password("password")
    login_popup.click_login()

