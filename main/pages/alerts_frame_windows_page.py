import time

from selenium.common import UnexpectedAlertPresentException

from main.generator.generator import generated_person
from main.pages.base_page import BasePage
from main.selectors.alerts_frames_windows_page_locators import BrowserWindowsPageLocators, AlertsPageLocators, \
    FramesPageLocators, NestedFramePageLocators, ModalDialogsPageLocators


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    def check_opened_new_tab(self):
        self.element_is_visible(self.locators.NEW_TAB).click()
        self.switch_to_tab_or_window(1)
        new_tab_message = self.element_exists(self.locators.NEW_TAB_TEXT).text
        return new_tab_message

    def check_opened_new_window(self):
        self.element_is_visible(self.locators.NEW_WINDOW).click()
        self.switch_to_tab_or_window(1)
        new_window_text = self.element_exists(self.locators.NEW_TAB_TEXT).text
        return new_window_text


class AlertsPage(BasePage):
    locators = AlertsPageLocators

    def check_alert_button(self):
        self.element_is_visible(self.locators.ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    def check_timer_alert_button(self):
        self.element_is_visible(self.locators.TIMER_ALERT_BUTTON).click()
        time.sleep(5)
        timer_alert_window = self.driver.switch_to.alert
        return timer_alert_window.text

    def check_confirm_alert_button(self):
        self.element_is_visible(self.locators.CONFIRM_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        if alert_window.text == "Do you confirm action?":
            alert_window.accept()
        else:
            return "alert window message is incorrect"
        return self.element_is_visible(self.locators.RESULT_AFTER_CONFIRMING).text

    def check_alert_prompt(self):
        random_name = next(generated_person()).full_name
        self.element_is_visible(self.locators.PROMPT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.send_keys(random_name)
        alert_window.accept()
        returned_message = self.element_is_visible(self.locators.RESULT_AFTER_PROMPT).text
        return random_name, returned_message


# a "frame" refers to an HTML element or construct that allows web developers to divide a browser window into
# multiple sections, each capable of displaying its own HTML document
class FramesPage(BasePage):
    locators = FramesPageLocators()

    def check_frame(self, frame_name):
        if frame_name == "frame1":
            first_frame = self.element_exists(self.locators.FIRST_FRAME)
            self.scroll_to_element(first_frame)
            width = first_frame.get_attribute("width")
            height = first_frame.get_attribute("height")
            self.switch_to_frame(first_frame)
            text = self.element_exists(self.locators.FRAME_H1_TITLE).text
            return text, width, height
        elif frame_name == "frame2":
            second_frame = self.element_exists(self.locators.SECOND_FRAME)
            self.scroll_to_element(second_frame)
            width = second_frame.get_attribute("width")
            height = second_frame.get_attribute("height")
            self.switch_to_frame(second_frame)
            text = self.element_exists(self.locators.FRAME_H1_TITLE).text
            return text, width, height


class NestedFramesPage(BasePage):
    locators = NestedFramePageLocators()

    def check_parent_frame(self):
        parent_frame = self.element_is_visible(self.locators.PARENT_FRAME)
        self.switch_to_frame(parent_frame)
        parent_text = self.element_exists(self.locators.PARENT_FRAME_TEXT).text
        child_frame = self.element_exists(self.locators.CHILD_FRAME)
        self.switch_to_frame(child_frame)
        child_text = self.element_is_visible(self.locators.CHILD_FRAME_TEXT).text
        return parent_text, child_text


class ModalDialogsPage(BasePage):
    locators = ModalDialogsPageLocators()

    def check_small_modal(self):
        self.element_is_visible(self.locators.SMALL_MODAL_BUTTON).click()
        modal_title = self.element_is_visible(self.locators.SMALL_MODAL_TITLE).text
        self.element_is_visible(self.locators.X_BUTTON)
        modal_text = self.element_is_visible(self.locators.SMALL_MODAL_TEXT).text
        self.element_is_visible(self.locators.SMALL_MODAL_CLOSE_BUTTON)
        return modal_title, modal_text

    def check_large_modal(self):
        self.element_is_visible(self.locators.LARGE_MODAL_BUTTON).click()
        modal_title = self.element_is_visible(self.locators.LARGE_MODAL_TITLE).text
        self.element_is_visible(self.locators.X_BUTTON)
        modal_text = self.element_is_visible(self.locators.LARGE_MODAL_TEXT).text
        self.element_is_visible(self.locators.LARGE_MODAL_CLOSE_BUTTON)
        return modal_title, modal_text

