import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.login_popup import LoginPopup
from pages.item_category_page import PhonesCategoryPage, LaptopsCategoryPage, MonitorsCategoryPage
from pages.specific_item_page import AddItemToCart
from pages import specific_item_page


@pytest.fixture
def logged_in_page(driver):
    login_popup = LoginPopup(driver)
    login_popup.click_open_login_popup()


    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(login_popup.LOGIN_BUTTON))

    login_popup.enter_username("tester41")
    login_popup.enter_password("testowehaslo41")
    login_popup.click_login()
    time.sleep(5)
    return driver

def test_add_phone_to_cart(logged_in_page):

    phones_page = PhonesCategoryPage(logged_in_page)
    phones_page.click_open_phones_category()

    time.sleep(2)
    specific_phone_page = AddItemToCart(logged_in_page)
    specific_phone_page.add_item_to_cart()
    specific_phone_page.return_to_homepage()

    laptops_page = LaptopsCategoryPage(logged_in_page)
    time.sleep(2)
    laptops_page.click_open_laptops_category()

    time.sleep(2)
    specific_laptop_page = AddItemToCart(logged_in_page)
    specific_laptop_page.add_item_to_cart()
    specific_laptop_page.return_to_homepage()



    #specific_item_page.AddItemToCart(driver)


    #AddItemToCart.add_item_to_cart()
    time.sleep(3)
    #AddItemToCart.return_to_homepage()