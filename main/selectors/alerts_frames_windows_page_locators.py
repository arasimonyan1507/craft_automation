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


class FramesPageLocators:
    FIRST_FRAME = (By.CSS_SELECTOR, "#frame1")
    SECOND_FRAME = (By.CSS_SELECTOR, "#frame2")
    FRAME_H1_TITLE = (By.CSS_SELECTOR, "h1#sampleHeading")


class NestedFramePageLocators:
    PARENT_FRAME = (By.CSS_SELECTOR, "#frame1")
    PARENT_FRAME_TEXT = (By.XPATH, "/html/body")
    CHILD_FRAME = (By.CSS_SELECTOR, 'iframe[srcdoc="<p>Child Iframe</p>"]')
    CHILD_FRAME_TEXT = (By.CSS_SELECTOR, "body>p")


class ModalDialogsPageLocators:
    SMALL_MODAL_BUTTON = (By.CSS_SELECTOR, "#showSmallModal")
    SMALL_MODAL_TITLE = (By.CSS_SELECTOR, " #example-modal-sizes-title-sm")
    X_BUTTON = (By.CSS_SELECTOR, "button.close")
    SMALL_MODAL_TEXT = (By.CSS_SELECTOR, 'div[class = "modal-body"]')
    SMALL_MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, "#closeSmallModal")
    LARGE_MODAL_BUTTON = (By.CSS_SELECTOR, "#showLargeModal")
    LARGE_MODAL_TITLE = (By.CSS_SELECTOR, "#example-modal-sizes-title-lg")
    LARGE_MODAL_TEXT = (By.CSS_SELECTOR, "div.modal-body>p")
    LARGE_MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, "#closeLargeModal")


