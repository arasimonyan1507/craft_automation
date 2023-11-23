from selenium.webdriver.common.by import By


class AccordianPageLocators:
    FIRST_ACCORDIAN = "#section1Heading"
    FIRST_ACCORDIAN_CONTENT = "#section1Content"
    SECOND_ACCORDIAN = "#section2Heading"
    SECOND_ACCORDIAN_CONTENT = "#section2Content"
    THIRD_ACCORDIAN = "#section3Heading"
    THIRD_ACCORDIAN_CONTENT = "#section3Content"


class AutoCompletePageLocators:
    MULTIPLE_COMPLETE = (By.CSS_SELECTOR, "input#autoCompleteMultipleInput")
    SINGLE_COMPLETE = (By.CSS_SELECTOR, "INPUT#autoCompleteSingleInput")
    LIST_OF_AVAILABLE_COLORS = ["Red", "Blue", "Green", "Yellow", "Purple", "Black", "White", "Voilet", "Indigo", "Magenta", "Aqua"]
    SELECTED_LIST_OF_COLORS = (By.CSS_SELECTOR, 'div[class^="css-1rhbuit"]>div[class^="css-12jo7m5"]')
    SELECTED_SINGLE_COLOR = (By.CSS_SELECTOR, 'div.auto-complete__single-value.css-1uccc91-singleValue')
    DELETE_ALL_COLORS_BUTTON = (By.CSS_SELECTOR, 'div[aria-hidden="true"]')
    DELETE_EXACT_COLOR_BUTTON = (By.CSS_SELECTOR, 'div[class^="css-xb97g8"]')


class DatePickerPageLocators:
    # SELECT DATE
    SELECT_DATE = (By.CSS_SELECTOR, "#datePickerMonthYearInput")
    SELECT_DATE_CONTAINER_TITLE = (By.CSS_SELECTOR, 'div[class^="react-datepicker__current-month react-datepicker"]')
    DATE_MONTH_DROPDOWN = (By.CSS_SELECTOR, "select.react-datepicker__month-select")
    DATE_MONTHS_LIST = (By.CSS_SELECTOR, "select.react-datepicker__month-select>option")
    DATE_YEAR_DROPDOWN = (By.CSS_SELECTOR, "select.react-datepicker__year-select")
    DATE_YEARS_LIST = (By.CSS_SELECTOR, "select.react-datepicker__year-select>option")
    DATE_YEAR = (By.CSS_SELECTOR, "select.react-datepicker__year-select>option[value={}]")
    DATE_WEEK_DAYS_LIST = (By.CSS_SELECTOR, "div.react-datepicker__day-name")
    DATE_DAYS_LIST = (By.CSS_SELECTOR, 'div[class^="react-datepicker__day react-datepicker__day"]')
    SELECTED_DATE_DAY = (By.CSS_SELECTOR, 'div[class*="day--selected"]')
    # SELECT DATE AND TIME
    DATE_AND_TIME_INPUT = (By.CSS_SELECTOR, "#dateAndTimePickerInput")
    DATE_TIME_MONTH = (By.CSS_SELECTOR, "span.react-datepicker__month-read-view--down-arrow")
    DATE_TIME_YEAR = (By.CSS_SELECTOR, "span.react-datepicker__year-read-view--down-arrow")
    DATE_TIME_MONTH_LIST = (By.CSS_SELECTOR, "div.react-datepicker__month-option")
    DATE_TIME_YEAR_LIST = (By.CSS_SELECTOR, "div.react-datepicker__year-option")
    DATE_TIME_DAYS_LIST = (By.CSS_SELECTOR, 'div[class^="react-datepicker__day react-datepicker__day"]')
    DATE_TIME_TIME_LIST = (By.CSS_SELECTOR, 'li.react-datepicker__time-list-item')


class SlidersPageLocators:
    SLIDER = (By.CSS_SELECTOR, "input.range-slider.range-slider--primary")
    SLIDER_VALUE = (By.CSS_SELECTOR, "input#sliderValue")


class ProgressBarPageLocators:
    PROGRESS_BAR = (By.CSS_SELECTOR, '#progressBar>div[role="progressbar"]')
    START_BUTTON = (By.CSS_SELECTOR, "button#startStopButton")


class TabsPageLocators:
    WHAT = (By.CSS_SELECTOR, '#demo-tab-what')
    WHAT_CONTEXT = (By.CSS_SELECTOR, '#demo-tabpane-what>p')
    ORIGIN = (By.CSS_SELECTOR, "#demo-tab-origin")
    ORIGIN_CONTEXT = (By.CSS_SELECTOR, '#demo-tabpane-origin>p')
    USE = (By.CSS_SELECTOR, "#demo-tab-use")
    USE_CONTEXT = (By.CSS_SELECTOR, '#demo-tabpane-use>p')


class ToolTipsPageLocators:
    BUTTON_TO_HOVER = (By.CSS_SELECTOR, "button#toolTipButton")
    INPUT_TO_HOVER = (By.CSS_SELECTOR, "input#toolTipTextField")
    WORD_TO_HOVER = (By.CSS_SELECTOR, "#texToolTopContainer.mt-4>a:first-of-type")
    INT_TO_HOVER = (By.CSS_SELECTOR, "#texToolTopContainer.mt-4>a:last-of-type")
    TEXT_AFTER_HOVERING = (By.CSS_SELECTOR, "div.tooltip-inner")
    TITLE_OF_PAGE = (By.CSS_SELECTOR, "#buttonToolTopContainer>P")
