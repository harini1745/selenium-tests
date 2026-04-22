from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class DropdownPage:
    URL = "https://the-internet.herokuapp.com/dropdown"
    DROPDOWN = (By.ID, "dropdown")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def select_option(self, text):
        el = self.wait.until(EC.presence_of_element_located(self.DROPDOWN))
        Select(el).select_by_visible_text(text)

    def get_selected_option(self):
        el = self.driver.find_element(*self.DROPDOWN)
        return Select(el).first_selected_option.text