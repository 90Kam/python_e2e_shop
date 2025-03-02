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


def test_add_item_to_cart(logged_in_page):

    phones_page = PhonesCategoryPage(logged_in_page)
    phones_page.open_phones_category()
    phones_page.select_samsung_galaxy_s6()

    time.sleep(2)
    specific_phone_page = AddItemToCart(logged_in_page)
    specific_phone_page.add_item_to_cart()
    specific_phone_page.return_to_homepage()


    laptops_page = LaptopsCategoryPage(logged_in_page)
    time.sleep(2)
    laptops_page.open_laptops_category()
    laptops_page.select_sony_vaio_i5()

    time.sleep(2)
    specific_laptop_page = AddItemToCart(logged_in_page)
    specific_laptop_page.add_item_to_cart()
    specific_laptop_page.return_to_homepage()

    monitors_page = MonitorsCategoryPage(logged_in_page)
    time.sleep(2)
    monitors_page.open_monitors_category()
    time.sleep(2)
    monitors_page.select_asus_full_hd()

    specific_monitor_page = AddItemToCart(logged_in_page)
    time.sleep(2)
    specific_monitor_page.add_item_to_cart()
    specific_monitor_page.return_to_homepage()

    #specific_item_page.AddItemToCart(driver)


    #AddItemToCart.add_item_to_cart()
    time.sleep(3)
    #AddItemToCart.return_to_homepage()