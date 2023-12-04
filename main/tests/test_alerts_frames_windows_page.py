import time

import allure
import pytest

from main.pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage, FramesPage, NestedFramesPage, \
    ModalDialogsPage


@allure.suite("Test Browser Windows Page")
class TestBrowserWindowsPage:
    @allure.title("test_new_tab")
    def test_new_tab(self, drive):
        browser_windows_page = BrowserWindowsPage(drive, "https://demoqa.com/browser-windows")
        browser_windows_page.open()
        new_tab_message = browser_windows_page.check_opened_new_tab()
        assert new_tab_message == "This is a sample page", "new tab was not opened successfully"

    @allure.title("test new window")
    def test_new_window(self, headless_driver):
        browser_windows_page = BrowserWindowsPage(headless_driver, "https://demoqa.com/browser-windows")
        browser_windows_page.open()
        new_window_text = browser_windows_page.check_opened_new_window()
        assert new_window_text == "This is a sample page", "new tab was not opened successfully"


@allure.suite("Test Alerts Page")
class TestAlertsPage:
    @allure.title("test alert button")
    def test_alert_button(self, headless_driver):
        alert_page = AlertsPage(headless_driver, "https://demoqa.com/alerts")
        alert_page.open()
        alert_message = alert_page.check_alert_button()
        assert alert_message == "You clicked a button", "alert message is incorrect"

    @allure.title("test timer alert button")
    def test_timer_alert_button(self, headless_driver):
        alert_page = AlertsPage(headless_driver, "https://demoqa.com/alerts")
        alert_page.open()
        timer_alert_message = alert_page.check_timer_alert_button()
        assert timer_alert_message == "This alert appeared after 5 seconds", "timer alert message is incorrect"

    @allure.title("test confirm alert button")
    def test_confirm_alert_button(self, headless_driver):
        alert_page = AlertsPage(headless_driver, "https://demoqa.com/alerts")
        alert_page.open()
        result_after_confirming = alert_page.check_confirm_alert_button()
        assert result_after_confirming == "You selected Ok", "result after confirming is incorrect"

    @allure.title("test alert prompt")
    def test_alert_prompt(self, headless_driver):
        alert_page = AlertsPage(headless_driver, "https://demoqa.com/alerts")
        alert_page.open()
        entered_name, returned_message = alert_page.check_alert_prompt()
        assert returned_message == f"You entered {entered_name}", "message after filling the prompt is incorrect"


@allure.suite("Test Frames Page")
class TestFramesPage:
    @allure.title("test first frame")
    def test_first_frame(self, driver_with_add_blocker):
        frames_page = FramesPage(driver_with_add_blocker, "https://demoqa.com/frames")
        frames_page.open()
        text, width, height = frames_page.check_frame("frame1")
        assert text == "This is a sample page", "First frames text is incorrect"
        assert width == "500px", "width size is incorrect"
        assert height == "350px", "height size is incorrect"

    @allure.title("test second frame")
    def test_second_frame(self, headless_driver):
        frames_page = FramesPage(headless_driver, "https://demoqa.com/frames")
        frames_page.open()
        text, width, height = frames_page.check_frame("frame2")
        assert text == "This is a sample page", "Second frames text is incorrect"
        assert width == "100px"
        assert height == "100px"


@allure.suite("Test Nested Frames Page")
class TestNestedFramesPage:
    @allure.title("test parent frame")
    def test_parent_frame(self, headless_driver):
        nested_frame_page = NestedFramesPage(headless_driver, "https://demoqa.com/nestedframes")
        nested_frame_page.open()
        parent_frame_text, child_frame_text = nested_frame_page.check_parent_frame()
        assert parent_frame_text == "Parent frame", "Parent frame doesn't exist"
        assert child_frame_text == "Child Iframe", "Nested frame doesn't exist"


@allure.suite("Test Modal Dialogs Page")
class TestModalDialogsPage:
    @allure.title("test small modal button")
    def test_small_modal_button(self, headless_driver):
        modal_dialogs_page = ModalDialogsPage(headless_driver, "https://demoqa.com/modal-dialogs")
        modal_dialogs_page.open()
        modal_title, modal_text = modal_dialogs_page.check_small_modal()
        assert modal_title == "Small Modal", "Small modals title is incorrect"
        assert modal_text == "This is a small modal. It has very less content", "Small modals text is incorrect"

    @allure.title("test large modal button")
    def test_large_modal_button(self, headless_driver):
        modal_dialogs_page = ModalDialogsPage(headless_driver, "https://demoqa.com/modal-dialogs")
        modal_dialogs_page.open()
        modal_title, modal_text = modal_dialogs_page.check_large_modal()
        assert modal_title == "Large Modal", "Large modals title is incorrect"
        for word in ["Lorem", "dummy", "passages"]:
            assert word in modal_text, "Large modals text is incorrect"


