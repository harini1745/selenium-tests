import pytest
import allure
from pages.login_page import LoginPage
from pages.data_reader import read_excel

# Read test data from Excel
test_data = read_excel("testdata.xlsx", "LoginTests")

# Convert to list of tuples for parametrize
login_data = [(d["username"], d["password"], d["expected"]) for d in test_data]

@allure.feature("Login - Excel Driven")
class TestLoginExcel:

    @allure.story("Login tests from Excel")
    @pytest.mark.parametrize("username, password, expected", login_data)
    def test_login_from_excel(self, driver, username, password, expected):
        with allure.step(f"Login with username='{username}'"):
            page = LoginPage(driver)
            page.open()
            page.login(username, password)

        with allure.step(f"Verify '{expected}' in page"):
            assert expected in page.get_body_text()