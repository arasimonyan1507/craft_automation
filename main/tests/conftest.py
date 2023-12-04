import time

import allure
from selenium.common import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver


@pytest.fixture()
def drive(request):
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    allure.title(request.function.__name__)
    yield driver
    screenshot = driver.get_screenshot_as_png()
    allure.attach(screenshot,attachment_type=allure.attachment_type.PNG)
    driver.quit()


@pytest.fixture(scope="function")
def driver_with_add_blocker():
    ext = webdriver.ChromeOptions()
    ext.add_extension(
        r"C:\Users\araga\AppData\Local\Google\Chrome\User Data\Default\Extensions\cjpalhdlnbpafiamejdnhcphjbkeiagm\1.53.0_0.crx")
    driver = webdriver.Chrome(options=ext)
    time.sleep(2)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def headless_driver():
    option = webdriver.ChromeOptions()
    option.add_argument("--headless=new")
    driver = webdriver.Chrome(options=option)
    driver.maximize_window()
    yield driver
    driver.quit()
