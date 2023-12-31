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


class RadioButtonPageLocators:
    YES_RADIO_BUTTON = (By.CSS_SELECTOR, "label[class^='custom-control-label'][for='yesRadio']")
    IMPRESSIVE_RADIO_BUTTON = (By.CSS_SELECTOR, "label[class^='custom-control-label'][for='impressiveRadio']")
    NO_RADIO_BUTTON = (By.CSS_SELECTOR, "label[class^='custom-control-label'][for='noRadio']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, '.mt-3>span[class = "text-success"]')


class WebTablesPageLocators:
    ADD_BUTTON = (By.ID, "addNewRecordButton")
    FIRST_NAME_INPUT = (By.ID, "firstName")
    LAST_NAME_INPUT = (By.ID, "lastName")
    EMAIL_INPUT = (By.ID, "userEmail")
    AGE_INPUT = (By.ID, "age")
    SALARY_INPUT = (By.ID, "salary")
    DEPARTMENT_INPUT = (By.ID, "department")
    SUBMIT_BUTTON = (By.ID, "submit")
    PEOPLE_LIST = (By.CSS_SELECTOR, 'div[class="rt-tr-group"]')
    SEARCH_FIELD = (By.CSS_SELECTOR, "#searchBox")
    DELETE_BUTTON = (By.CSS_SELECTOR, 'span[title="Delete"]')
    PARENT_ROW = './/ancestor::div[@class="rt-tr-group"]'
    EDIT_BUTTON = (By.CSS_SELECTOR, 'span[title="Edit"]')
    ROWS_NO_FOUND = (By.CSS_SELECTOR, 'div.rt-noData')
    ROWS_DROPDOWN = (By.CSS_SELECTOR, 'span.select-wrap.-pageSizeOptions')


class ButtonsPageLocators:
    DOUBLE_CLICK_BUTTON = (By.CSS_SELECTOR, "#doubleClickBtn")
    RIGHT_CLICK_BUTTON = (By.CSS_SELECTOR, '#rightClickBtn')
    CLICK_BUTTON = (By.XPATH, '//div[3]/button')
    DOUBLE_CLICK_MESSAGE = (By.CSS_SELECTOR, "#doubleClickMessage")
    RIGHT_CLICK_MESSAGE = (By.CSS_SELECTOR, '#rightClickMessage')
    CLICK_MESSAGE = (By.CSS_SELECTOR, '#dynamicClickMessage')


class LinksPageLocators:
    HOME_LINK = (By.CSS_SELECTOR, '#simpleLink')
    BAD_REQUEST = (By.CSS_SELECTOR, "#bad-request")


class UploadAndDownloadPageLocators:
    DOWNLOAD_BUTTON = (By.CSS_SELECTOR, "#downloadButton")
    UPLOAD_BUTTON = (By.CSS_SELECTOR, "#uploadFile")
    UPLOADED_FILE_PATH = (By.CSS_SELECTOR, "#uploadedFilePath")


class DynamicPropertiesLocators:
    CHANGE_COLOR = (By.CSS_SELECTOR, "#colorChange")
    VISIBLE_AFTER_5_SECONDS = (By.CSS_SELECTOR, "#visibleAfter")
    ENABLE_AFTER_5_SEC = (By.CSS_SELECTOR, "#enableAfter")


