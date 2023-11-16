from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:
    NEW_TAB = (By.CSS_SELECTOR, "#tabButton")
    NEW_WINDOW = (By.CSS_SELECTOR, "#windowButton")
    NEW_WINDOW_MESSAGE = (By.CSS_SELECTOR, "#messageWindowButton")
    NEW_TAB_TEXT = (By.CSS_SELECTOR, "#sampleHeading")


class AlertsPageLocators:
    ALERT_BUTTON = (By.CSS_SELECTOR, "#alertButton")
    TIMER_ALERT_BUTTON = (By.CSS_SELECTOR, "#timerAlertButton")
    CONFIRM_BUTTON = (By.CSS_SELECTOR, "#confirmButton")
    PROMPT_BUTTON = (By.CSS_SELECTOR, "#promtButton")
    RESULT_AFTER_CONFIRMING = (By.CSS_SELECTOR, "#confirmResult")
    RESULT_AFTER_PROMPT = (By.CSS_SELECTOR, "#promptResult")
