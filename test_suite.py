import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

# ============================================
# FIXTURE - runs before and after every test
# ============================================
@pytest.fixture
def driver():
    d = webdriver.Chrome()
    d.implicitly_wait(10)
    yield d          # test runs here
    d.quit()         # always closes browser after test

# ============================================
# LOGIN TESTS
# ============================================
class TestLogin:

    def test_valid_login(self, driver):
        driver.get("https://practicetestautomation.com/practice-test-login/")
        wait = WebDriverWait(driver, 20)
        wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys("student")
        driver.find_element(By.ID, "password").send_keys("Password123")
        driver.find_element(By.ID, "submit").click()
        time.sleep(3)
        assert "Congratulations" in driver.find_element(By.TAG_NAME, "body").text

    def test_invalid_password(self, driver):
        driver.get("https://practicetestautomation.com/practice-test-login/")
        wait = WebDriverWait(driver, 20)
        wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys("student")
        driver.find_element(By.ID, "password").send_keys("wrongpass")
        driver.find_element(By.ID, "submit").click()
        time.sleep(3)
        assert "Your password is invalid!" in driver.find_element(By.TAG_NAME, "body").text

    def test_invalid_username(self, driver):
        driver.get("https://practicetestautomation.com/practice-test-login/")
        wait = WebDriverWait(driver, 20)
        wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys("wronguser")
        driver.find_element(By.ID, "password").send_keys("Password123")
        driver.find_element(By.ID, "submit").click()
        time.sleep(3)
        assert "Your username is invalid!" in driver.find_element(By.TAG_NAME, "body").text

# ============================================
# DROPDOWN TESTS
# ============================================
class TestDropdown:

    def test_select_option1(self, driver):
        driver.get("https://the-internet.herokuapp.com/dropdown")
        wait = WebDriverWait(driver, 10)
        dropdown = Select(wait.until(EC.presence_of_element_located((By.ID, "dropdown"))))
        dropdown.select_by_visible_text("Option 1")
        assert dropdown.first_selected_option.text == "Option 1"

    def test_select_option2(self, driver):
        driver.get("https://the-internet.herokuapp.com/dropdown")
        wait = WebDriverWait(driver, 10)
        dropdown = Select(wait.until(EC.presence_of_element_located((By.ID, "dropdown"))))
        dropdown.select_by_visible_text("Option 2")
        assert dropdown.first_selected_option.text == "Option 2"

# ============================================
# CHECKBOX TESTS
# ============================================
class TestCheckboxes:

    def test_checkboxes_can_be_toggled(self, driver):
        driver.get("https://the-internet.herokuapp.com/checkboxes")
        wait = WebDriverWait(driver, 10)
        checkboxes = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input[type='checkbox']")))

        # Store original states
        original_states = [c.is_selected() for c in checkboxes]

        # Click all checkboxes
        for c in checkboxes:
            c.click()

        # Verify all states flipped
        for i, c in enumerate(checkboxes):
            assert c.is_selected() != original_states[i]

# ============================================
# ALERT TESTS
# ============================================
class TestAlerts:

    def test_simple_alert(self, driver):
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
        wait = WebDriverWait(driver, 10)
        wait.until(EC.alert_is_present())
        alert = driver.switch_to.alert
        assert alert.text == "I am a JS Alert"
        alert.accept()
        time.sleep(2)
        result = driver.find_element(By.ID, "result").text
        assert "successfully clicked an alert" in result

    def test_confirm_ok(self, driver):
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
        wait = WebDriverWait(driver, 10)
        wait.until(EC.alert_is_present())
        driver.switch_to.alert.accept()
        time.sleep(2)
        assert "Ok" in driver.find_element(By.ID, "result").text

    def test_confirm_cancel(self, driver):
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
        wait = WebDriverWait(driver, 10)
        wait.until(EC.alert_is_present())
        driver.switch_to.alert.dismiss()
        time.sleep(2)
        assert "Cancel" in driver.find_element(By.ID, "result").text