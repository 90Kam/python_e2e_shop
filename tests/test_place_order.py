import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_popup import LoginPopup
from pages.item_category_page import PhonesCategoryPage, LaptopsCategoryPage, MonitorsCategoryPage
from pages.specific_item_page import AddItemToCart


@pytest.fixture
def logged_in_page(driver):
    login_popup = LoginPopup(driver)
    login_popup.click_open_login_popup()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(login_popup.LOGIN_BUTTON)
    )

    login_popup.enter_username("tester41")
    login_popup.enter_password("testowehaslo41")
    login_popup.click_login()

    # Oczekiwanie na widoczność elementu potwierdzającego logowanie
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "nameofuser"))
    )
    return driver


def test_add_item_to_cart(logged_in_page):
    driver = logged_in_page

    # Telefony
    phones_page = PhonesCategoryPage(driver)
    phones_page.open_phones_category()

    # Dodanie pierwszego produktu
    phones_page.select_samsung_galaxy_s6()
    item_page = AddItemToCart(driver)
    time.sleep(2)
    cena_tel = driver.find_element(By.XPATH,"//h3[@class='price-container']").text
    print("dupa  " , cena_tel)
    item_page.add_item_to_cart()

    # Użycie metody z BasePage do obsługi alertu
    if not item_page.accept_alert_if_present(timeout=5):
        pytest.fail("Alert nie pojawił się po dodaniu telefonu")
    item_page.return_to_homepage()

    # Laptopy
    laptops_page = LaptopsCategoryPage(driver)
    laptops_page.open_laptops_category()

    # Dodanie drugiego produktu
    time.sleep(2)
    laptops_page.select_sony_vaio_i5()
    item_page = AddItemToCart(driver)
    time.sleep(2)
    item_page.add_item_to_cart()

    # Użycie metody z BasePage
    if not item_page.accept_alert_if_present(timeout=5):
        pytest.fail("Alert nie pojawił się po dodaniu laptopa")
    item_page.return_to_homepage()

    # Monitory
    monitors_page = MonitorsCategoryPage(driver)
    monitors_page.open_monitors_category()

    # Dodanie trzeciego produktu
    time.sleep(2)
    monitors_page.select_asus_full_hd()
    item_page = AddItemToCart(driver)
    time.sleep(2)
    item_page.add_item_to_cart()

    # Użycie metody z BasePage
    if not item_page.accept_alert_if_present(timeout=5):
        pytest.fail("Alert nie pojawił się po dodaniu monitora")
    item_page.return_to_homepage()