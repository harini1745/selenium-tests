import sys
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", default=False,
                     help="Run tests in headless mode")

@pytest.fixture
def driver(request):
    options = Options()

    if request.config.getoption("--headless"):
        options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        print("\n[headless mode ON]")
    else:
        print("\n[headless mode OFF - browser visible]")

    d = webdriver.Chrome(options=options)
    yield d
    d.quit()