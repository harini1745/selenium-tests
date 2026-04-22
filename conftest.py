import sys
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Create screenshots folder if it doesn't exist
os.makedirs("screenshots", exist_ok=True)

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Browser: chrome, firefox, edge")
    parser.addoption("--headless", action="store_true", default=False,
                     help="Run headless")

@pytest.fixture
def driver(request):
    browser  = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    if browser == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless")
            options.add_argument("--window-size=1920,1080")
        d = webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        d = webdriver.Firefox(options=options)

    elif browser == "edge":
        options = EdgeOptions()
        if headless:
            options.add_argument("--headless")
        d = webdriver.Edge(options=options)

    else:
        raise ValueError(f"Unknown browser: {browser}")

    print(f"\nRunning on: {browser.upper()} | headless: {headless}")
    yield d
    d.quit()

# ---- Screenshot on failure ----
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report  = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            # Save screenshot with test name
            filename = f"screenshots/{item.name}.png"
            driver.save_screenshot(filename)
            print(f"\nScreenshot saved: {filename}")