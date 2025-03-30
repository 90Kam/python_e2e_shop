from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException, TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def find_elements(self, by, value):
        return self.driver.find_elements(by, value)

    def click(self, by, value):
        return self.find_element(by, value).click()

    def send_keys(self, by, value, text):
        return self.find_element(by, value).send_keys(text)

    def accept_alert_if_present(self, timeout=3):
        try:
            WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
            Alert(self.driver).accept()
            return True
        except (NoAlertPresentException, TimeoutException):
            return False