import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class PhonesCategoryPage(BasePage):
    CLICK_PHONES_CATEGORY = (By.LINK_TEXT, 'Phones')
    CLICK_SAMSUNG_GALAXY_S6 = (By.LINK_TEXT,"Samsung galaxy s6")

    def open_phones_category(self):
        self.click(*self.CLICK_PHONES_CATEGORY)
    def select_samsung_galaxy_s6(self):
        self.click(*self.CLICK_SAMSUNG_GALAXY_S6)


class LaptopsCategoryPage(BasePage):
    CLICK_LAPTOPS_CATEGORY = (By.LINK_TEXT, "Laptops")
    CLICK_SONY_VAIO_I5 = (By.LINK_TEXT, "Sony vaio i5")

    def open_laptops_category(self):
        self.click(*self.CLICK_LAPTOPS_CATEGORY)
    def select_sony_vaio_i5(self):
        self.click(*self.CLICK_SONY_VAIO_I5)


class MonitorsCategoryPage(BasePage):
    CLICK_MONITORS_CATEGORY = (By.LINK_TEXT, "Monitors")
    CLICK_ASUS_FULL_HD = (By.LINK_TEXT, "ASUS Full HD")

    def open_monitors_category(self):
        self.click(*self.CLICK_MONITORS_CATEGORY)
    def select_asus_full_hd(self):
        self.click(*self.CLICK_ASUS_FULL_HD)