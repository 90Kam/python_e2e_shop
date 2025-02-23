import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options  # Zmiana: Poprawny import dla Options
import os


CHROMEDRIVER_PATH = os.path.join(os.getcwd(), 'drivers', 'chromedriver.exe')  # Używaj właściwej ścieżki do chromedrivera


@pytest.fixture(scope="function")
def driver():

    options = Options()


    service = Service(executable_path="C:\chromedriver\chromedriver-win64\chromedriver.exe")  # Ścieżka do chromedrivera
    driver = webdriver.Chrome(service=service, options=options)  # Dodanie opcji


    driver.get("https://www.demoblaze.com")
    driver.maximize_window()
    yield driver

    # Po zakończeniu testu zamknij przeglądarkę
    driver.quit()
