import time
import pytest

from main.pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage, FramesPage, NestedFramesPage, \
    ModalDialogsPage


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


@pytest.mark.skip
class TestFramesPage:
    def test_first_frame(self, driver_with_add_blocker):
        frames_page = FramesPage(driver_with_add_blocker, "https://demoqa.com/frames")
        frames_page.open()
        text, width, height = frames_page.check_frame("frame1")
        assert text == "This is a sample page", "First frames text is incorrect"
        assert width == "500px", "width size is incorrect"
        assert height == "350px", "height size is incorrect"

    def test_second_frame(self, drive):
        frames_page = FramesPage(drive, "https://demoqa.com/frames")
        frames_page.open()
        text, width, height = frames_page.check_frame("frame2")
        assert text == "This is a sample page", "Second frames text is incorrect"
        assert width == "100px"
        assert height == "100px"


class TestNestedFramesPage:

    def test_parent_frame(self, drive):
        nested_frame_page = NestedFramesPage(drive, "https://demoqa.com/nestedframes")
        nested_frame_page.open()
        parent_frame_text, child_frame_text = nested_frame_page.check_parent_frame()
        assert parent_frame_text == "Parent frame", "Parent frame doesn't exist"
        assert child_frame_text == "Child Iframe", "Nested frame doesn't exist"


class TestModalDialogsPage:
    def test_small_modal_button(self, drive):
        modal_dialogs_page = ModalDialogsPage(drive, "https://demoqa.com/modal-dialogs")
        modal_dialogs_page.open()
        modal_title, modal_text = modal_dialogs_page.check_small_modal()
        assert modal_title == "Small Modal", "Small modals title is incorrect"
        assert modal_text == "This is a small modal. It has very less content", "Small modals text is incorrect"

    def test_large_modal_button(self, drive):
        modal_dialogs_page = ModalDialogsPage(drive, "https://demoqa.com/modal-dialogs")
        modal_dialogs_page.open()
        modal_title, modal_text = modal_dialogs_page.check_large_modal()
        assert modal_title == "Large Modal", "Large modals title is incorrect"
        for word in ["Lorem", "dummy", "passages"]:
            assert word in modal_text, "Large modals text is incorrect"


