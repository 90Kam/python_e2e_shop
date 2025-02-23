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
