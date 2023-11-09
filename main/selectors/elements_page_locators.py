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


