import pytest
from pages.login_page import LoginPage

class TestLogin:

    # All test data in one place - add more rows anytime
    @pytest.mark.parametrize("username, password, expected", [
        ("student",     "Password123",     "Congratulations"),
        ("student",     "wrongpass",       "Your password is invalid!"),
        ("wronguser",   "Password123",     "Your username is invalid!"),
        ("",            "",                "Your username is invalid!"),
        ("student",     "",                "Your password is invalid!"),
    ])
    def test_login(self, driver, username, password, expected):
        page = LoginPage(driver)
        page.open()
        page.login(username, password)
        assert expected in page.get_body_text()