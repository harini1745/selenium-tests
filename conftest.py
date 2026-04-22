import sys
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Browser to run tests on: chrome, firefox, edge")
    parser.addoption("--headless", action="store_true", default=False,
                     help="Run tests in headless mode")

@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
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