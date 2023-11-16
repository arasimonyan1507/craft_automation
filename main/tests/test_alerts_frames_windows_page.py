import time
import pytest
from main.pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage


@pytest.mark.skip
class TestBrowserWindowsPage:
    def test_new_tab(self, drive):
        browser_windows_page = BrowserWindowsPage(drive, "https://demoqa.com/browser-windows")
        browser_windows_page.open()
        new_tab_message = browser_windows_page.check_opened_new_tab()
        assert new_tab_message == "This is a sample page", "new tab was not opened successfully"

    def test_new_window(self, drive):
        browser_windows_page = BrowserWindowsPage(drive, "https://demoqa.com/browser-windows")
        browser_windows_page.open()
        new_window_text = browser_windows_page.check_opened_new_window()
        assert new_window_text == "This is a sample page", "new tab was not opened successfully"


class TestAlertsPage:
    @pytest.mark.skip
    def test_alert_button(self, drive):
        alert_page = AlertsPage(drive, "https://demoqa.com/alerts")
        alert_page.open()
        alert_message = alert_page.check_alert_button()
        assert alert_message == "You clicked a button", "alert message is incorrect"

    @pytest.mark.skip
    def test_timer_alert_button(self, drive):
        alert_page = AlertsPage(drive, "https://demoqa.com/alerts")
        alert_page.open()
        timer_alert_message = alert_page.check_timer_alert_button()
        assert timer_alert_message == "This alert appeared after 5 seconds", "timer alert message is incorrect"

    @pytest.mark.skip
    def test_confirm_alert_button(self, drive):
        alert_page = AlertsPage(drive, "https://demoqa.com/alerts")
        alert_page.open()
        result_after_confirming = alert_page.check_confirm_alert_button()
        assert result_after_confirming == "You selected Ok", "result after confirming is incorrect"

    @pytest.mark.skip
    def test_alert_prompt(self, drive):
        alert_page = AlertsPage(drive, "https://demoqa.com/alerts")
        alert_page.open()
        entered_name, returned_message = alert_page.check_alert_prompt()
        assert returned_message == f"You entered {entered_name}", "message after filling the prompt is incorrect"


