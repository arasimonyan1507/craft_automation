import time

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


@pytest.fixture(scope="function")
def driver_with_add_blocker():
    ext = webdriver.ChromeOptions()
    ext.add_extension(
        r"C:\Users\araga\AppData\Local\Google\Chrome\User Data\Default\Extensions\cjpalhdlnbpafiamejdnhcphjbkeiagm\1.53.0_0.crx")
    driver = webdriver.Chrome(options=ext)
    driver.maximize_window()
    yield driver
    driver.quit()
