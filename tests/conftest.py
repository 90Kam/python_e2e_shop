import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os

CHROMEDRIVER_PATH = os.path.join(os.getcwd(), 'drivers', 'chromedriver.exe')

@pytest.fixture(scope="class")
def driver():

    options = Options()

    service = Service(executable_path="C:\chromedriver\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)


    driver.get("https://www.demoblaze.com")
    driver.maximize_window()
    yield driver

    driver.quit()
