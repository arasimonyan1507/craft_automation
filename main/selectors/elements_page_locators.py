from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    # fields
    FULL_NAME = (By.ID, "userName")
    EMAIL = (By.ID, "userEmail")
    CURRENT_ADDRESS = (By.ID, "currentAddress")
    PERMANENT_ADDRESS = (By.ID, "permanentAddress")
    SUBMIT = (By.CSS_SELECTOR, "#submit")

    # after submitting
    SUBMITTED_FULL_NAME = (By.ID, "name")
    SUBMITTED_EMAIL = (By.ID, "email")
    SUBMITTED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#currentAddress")
    SUBMITTED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#permanentAddress")


class CheckBoxPageLocators:
    EXPAND_ALL = (By.CSS_SELECTOR, 'button[title="Expand all"]')
    LIST_OF_CHECKBOXES = (By.CSS_SELECTOR, 'span.rct-title')
    CHECKED_CHECKBOX = (By.CSS_SELECTOR, "span.rct-checkbox>svg.rct-icon.rct-icon-check")
    ITEM_TITLE = './/ancestor::span[@class = "rct-text"]'
    CHECKBOXES_OUTPUT = (By.CSS_SELECTOR, '#result>span.text-success')


class RadioButtonLocators:
    YES_RADIO_BUTTON = (By.CSS_SELECTOR, "label[class^='custom-control-label'][for='yesRadio']")
    IMPRESSIVE_RADIO_BUTTON = (By.CSS_SELECTOR, "label[class^='custom-control-label'][for='impressiveRadio']")
    NO_RADIO_BUTTON = (By.CSS_SELECTOR, "label[class^='custom-control-label'][for='noRadio']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, '.mt-3>span[class = "text-success"]')



