from webdriver_manager.chrome import ChromeDriverManager
import pytest
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

@pytest.fixture(scope="function")
def drive():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


