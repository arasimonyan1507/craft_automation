import time

from selenium.common import UnexpectedAlertPresentException

from main.generator.generator import generated_person
from main.pages.base_page import BasePage
from main.selectors.alerts_frames_windows_page_locators import BrowserWindowsPageLocators, AlertsPageLocators


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
