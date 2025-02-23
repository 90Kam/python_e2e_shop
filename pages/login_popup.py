import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPopup(BasePage):

    USERNAME_FIELD = (By.ID, 'loginusername')
    PASSWORD_FIELD = (By.ID, 'loginpassword')
    LOGIN_BUTTON = (By.XPATH, "//*[@id='logInModal']/div/div/div[3]/button[2]")
    CLOSE_BUTTON = (By.XPATH, "//button[@class='close']")
    OPEN_LOGIN_POPUP = (By.ID,"login2")
    WELCOME_USER_TITLE = (By.ID, "nameofuser")

    def click_open_login_popup(self):
        self.click(*self.OPEN_LOGIN_POPUP)

    def enter_username(self, username):
        self.send_keys(*self.USERNAME_FIELD, username)

    def enter_password(self, password):
        self.send_keys(*self.PASSWORD_FIELD, password)

    def click_login(self):
        self.click(*self.LOGIN_BUTTON)

    def close_popup(self):
        self.click(*self.CLOSE_BUTTON)

    def welcome_user_title(self):
        return (By.ID, "nameofuser")

