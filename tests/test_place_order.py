import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.login_popup import LoginPopup
from pages.item_category_page import PhonesCategoryPage, LaptopsCategoryPage, MonitorsCategoryPage

def login_as_valid_user(driver):
    login_popup = LoginPopup(driver)
    login_popup.click_open_login_popup()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(login_popup.LOGIN_BUTTON))

    login_popup.enter_username("username")
    login_popup.enter_password("password")
    login_popup.click_login()

def test_add_phone_to_cart(driver):
    phones_page = PhonesCategoryPage(driver)
    phones_page.click_open_phones_category()
