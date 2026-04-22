import pytest
import allure
from pages.login_page import LoginPage

@allure.feature("Login")
class TestLogin:

    @allure.story("Parametrized login tests")
    @pytest.mark.parametrize("username, password, expected", [
        ("student",     "Password123",     "Congratulations"),
        ("student",     "wrongpass",       "Your password is invalid!"),
        ("wronguser",   "Password123",     "Your username is invalid!"),
        ("",            "",                "Your username is invalid!"),
        ("student",     "",                "Your password is invalid!"),
    ])
    def test_login(self, driver, username, password, expected):
        with allure.step(f"Login with username='{username}'"):
            page = LoginPage(driver)
            page.open()
            page.login(username, password)

        with allure.step(f"Verify '{expected}' in page"):
            assert expected in page.get_body_text()