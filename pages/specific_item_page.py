import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AddItemToCart(BasePage):
    CLICK_ADD_TO_CART_BUTTON = (By.LINK_TEXT, 'Add to cart')
    CLICK_HOME_BUTTON = (By.XPATH, "//a[@class='nav-link']")

    def add_item_to_cart(self):
        self.click(*self.CLICK_ADD_TO_CART_BUTTON)

    def return_to_homepage(self):
        self.click(*self.CLICK_HOME_BUTTON)

