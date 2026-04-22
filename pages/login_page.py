from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage:
    # URL
    URL = "https://practicetestautomation.com/practice-test-login/"

    # Locators - all in one place
    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    SUBMIT_BUTTON  = (By.ID, "submit")
    BODY           = (By.TAG_NAME, "body")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def open(self):
        self.driver.get(self.URL)

    def enter_username(self, username):
        field = self.wait.until(EC.visibility_of_element_located(self.USERNAME_FIELD))
        field.send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)

    def click_submit(self):
        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_submit()
        time.sleep(3)

    def get_body_text(self):
        return self.driver.find_element(*self.BODY).text