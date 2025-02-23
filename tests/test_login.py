import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.login_popup import LoginPopup

@pytest.mark.parametrize("username, password, expected_success", [
    ("tester41", "testowehaslo41", True),   # Poprawne dane
    ("tester41", "zlehaslo", False),        # Złe hasło
    ("nieistniejacy", "testowehaslo41", False),  # Nieistniejący użytkownik
])
def test_login(driver, username, password, expected_success):
    login_popup = LoginPopup(driver)
    login_popup.click_open_login_popup()

    # Oczekiwanie na pojawienie się formularza logowania
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(login_popup.LOGIN_BUTTON))

    # Wprowadź dane logowania
    login_popup.enter_username(username)
    login_popup.enter_password(password)
    login_popup.click_login()

    if expected_success:
        # Oczekujemy, że użytkownik się zaloguje
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(login_popup.welcome_user_title()))
        welcome_message = driver.find_element(By.ID, "nameofuser").text
        assert username in welcome_message, f"Expected {username} in welcome message, but got {welcome_message}"
    else:
        # Oczekujemy, że logowanie się nie powiedzie (pojawi się alert)
        try:
            # Czekaj na pojawienie się alertu
            WebDriverWait(driver, 10).until(EC.alert_is_present())
            alert = driver.switch_to.alert  # Przełącz się na alert
            alert_text = alert.text  # Pobierz tekst alertu

            # Sprawdź, czy alert zawiera oczekiwany komunikat błędu
            assert "Wrong password" in alert_text or "User does not exist" in alert_text, \
                f"Unexpected alert text: {alert_text}"

            alert.accept()  # Zamknij alert
        except TimeoutException:
            pytest.fail("Expected alert did not appear after invalid login attempt.")