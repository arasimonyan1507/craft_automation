import random

from selenium.webdriver.common.by import By


class PracticeFormPageLocators:
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, "#firstName")
    LAST_NAME_FIELD = (By.CSS_SELECTOR, "#lastName")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#userEmail")
    MOBILE_NUMBER_FIELD = (By.CSS_SELECTOR, "#userNumber")
    DATE_OF_BIRTH_INPUT = (By.CSS_SELECTOR, "#dateOfBirthInput")
    SUBJECTS_FIELD = (By.CSS_SELECTOR, 'input[id="subjectsInput"]')
    CHOOSE_FILE = (By.CSS_SELECTOR, "#uploadPicture")
    gender_selector = f'div[class^="custom-control"]>label[for="gender-radio-{random.randint(1,3)}'
    GENDER = (By.CSS_SELECTOR, gender_selector)
    GENDER_PARENT_ELEMENT = (By.CSS_SELECTOR, 'input[name="gender"]')
    UPLOAD_FILE = (By.CSS_SELECTOR, 'input[id="uploadPicture"]')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="currentAddress"]')
    STATE_DROPDOWN = (By.CSS_SELECTOR, 'div[id="state"]>div>div.css-1hwfws3')
    STATE_NAME = (By.CSS_SELECTOR, f'#react-select-3-option-{random.randint(0,3)}')
    CITY_DROPDOWN = (By.CSS_SELECTOR, 'div#city>div>div.css-1hwfws3')
    CITY_NAME = (By.CSS_SELECTOR, f'#react-select-4-option-{random.randint(0, 1)}')
    SUBMIT = (By.CSS_SELECTOR, 'div[class^="text-right"]>button#submit')
    STUDENT_TABLE_DATA = (By.CSS_SELECTOR, "td:nth-child(2)")
