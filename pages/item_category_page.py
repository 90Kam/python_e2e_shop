import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class PhonesCategoryPage(BasePage):
    CLICK_PHONES_CATEGORY = (By.LINK_TEXT, 'Phones')

    def click_open_phones_category(self):
        self.click(*self.CLICK_PHONES_CATEGORY)


class LaptopsCategoryPage(BasePage):
    CLICK_LAPTOPS_CATEGORY = (By.LINK_TEXT, "Laptops")

    def click_open_laptops_category(self):
        self.click(*self.CLICK_LAPTOPS_CATEGORY)


class MonitorsCategoryPage(BasePage):
    CLICK_MONITORS_CATEGORY = (By.LINK_TEXT, "Monitors")

    def click_open_monitors_category(self):
        self.click(*self.CLICK_MONITORS_CATEGORY)