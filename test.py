from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
import time

def get_driver(browser):
    if browser == "chrome":
        return webdriver.Chrome()
    elif browser == "firefox":
        return webdriver.Firefox()
    elif browser == "edge":
        return webdriver.Edge()
    else:
        raise ValueError(f"Unknown browser: {browser}")

def test_login(browser):
    print(f"\n--- Testing on {browser.upper()} ---")
    driver = get_driver(browser)

    try:
        driver.get("https://practicetestautomation.com/practice-test-login/")
        wait = WebDriverWait(driver, 20)

        wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys("student")
        driver.find_element(By.ID, "password").send_keys("Password123")
        driver.find_element(By.ID, "submit").click()
        time.sleep(3)

        body = driver.find_element(By.TAG_NAME, "body").text
        if "Congratulations" in body:
            print(f"✓ PASS on {browser}")
        else:
            print(f"✗ FAIL on {browser}")
    finally:
        driver.quit()

# Run on all three browsers
for browser in ["chrome", "firefox", "edge"]:
    test_login(browser)