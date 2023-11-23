import time

import selenium.webdriver.support.relative_locator

from main.generator.generator import generated_color, generated_date
from main.pages.base_page import BasePage
from main.selectors.widgets_page_locators import AccordianPageLocators, AutoCompletePageLocators, \
    DatePickerPageLocators, SlidersPageLocators, ProgressBarPageLocators, TabsPageLocators, ToolTipsPageLocators
from selenium.webdriver.common.by import By
import pytest
import random
from selenium.webdriver.common.keys import Keys


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    def check_accordian(self, name):
        accordian_dict = {
            "first": {"title": (By.CSS_SELECTOR, self.locators.FIRST_ACCORDIAN),
                      "content": (By.CSS_SELECTOR, self.locators.FIRST_ACCORDIAN_CONTENT)},
            "second": {"title": (By.CSS_SELECTOR, self.locators.SECOND_ACCORDIAN),
                       "content": (By.CSS_SELECTOR, self.locators.SECOND_ACCORDIAN_CONTENT)},
            "third": {"title": (By.CSS_SELECTOR, self.locators.THIRD_ACCORDIAN),
                      "content": (By.CSS_SELECTOR, self.locators.THIRD_ACCORDIAN_CONTENT)}}
        accordian = accordian_dict[name]
        accordian_title = self.element_exists(accordian["title"])
        self.scroll_to_element(accordian_title)
        accordian_title.click()
        title = accordian_title.text
        accordian_content = self.element_is_visible(accordian["content"])
        content = accordian_content.text
        return title, content


class AutoCompletePage(BasePage):
    locators = AutoCompletePageLocators()

    def check_multiple_complete_input(self):
        multiple_complete_input = self.element_is_visible(self.locators.MULTIPLE_COMPLETE)
        colors_data = generated_color()
        input_of_colors = random.sample(colors_data, random.randint(1, len(colors_data)))
        for color in input_of_colors:
            multiple_complete_input.send_keys(color)
            multiple_complete_input.send_keys(Keys.ENTER)
        selected_list_of_colors = self.elements_are_exist(self.locators.SELECTED_LIST_OF_COLORS)
        output_of_colors = []
        for el in selected_list_of_colors:
            output_of_colors.append(el.text)
        return input_of_colors, output_of_colors

    def check_delete_all_colors_button(self):
        self.check_multiple_complete_input()
        delete_button = self.element_is_visible(self.locators.DELETE_ALL_COLORS_BUTTON)
        delete_button.click()
        if self.element_is_invisible(self.locators.SELECTED_LIST_OF_COLORS):
            return True

    def check_delete_exact_color_button(self):
        input_of_colors, colors_before_deleting = self.check_multiple_complete_input()
        delete_buttons = self.elements_are_exist(self.locators.DELETE_EXACT_COLOR_BUTTON)
        for delete in delete_buttons:
            delete.click()
            break
        selected_list = self.elements_are_exist(self.locators.SELECTED_LIST_OF_COLORS)
        colors_after_deleting = []
        for color in selected_list:
            colors_after_deleting.append(color.text)
        return len(colors_before_deleting), len(colors_after_deleting)

    def check_single_complete_input(self):
        single_complete_input = self.element_is_visible(self.locators.SINGLE_COMPLETE)
        colors_data = generated_color()
        random_color = colors_data[random.randint(0, len(colors_data))]
        single_complete_input.send_keys(random_color)
        single_complete_input.send_keys(Keys.ENTER)
        selected_color = self.element_exists(self.locators.SELECTED_SINGLE_COLOR).text
        return random_color, selected_color


#
# class DatePickerPage(BasePage):
#     locators = DatePickerPageLocators()
#
#     def open_select_date(self):
#         self.element_is_visible(self.locators.SELECT_DATE).click()
#
#     def select_date_month(self, m=(random.randint(0, 11))):
#         self.element_is_visible(self.locators.DATE_MONTH_DROPDOWN).click()
#         month = self.element_exists((By.CSS_SELECTOR, 'select.react-datepicker__month-select>option[value=\"{}\"]'.format(m)))
#         month.click()
#         self.scroll_to_element(month)
#         return str(m+1), str(month.text)
#
#     def check_selected_date_month(self):
#         month = self.element_is_visible(self.locators.SELECT_DATE_CONTAINER_TITLE).text.split(" ")[0]
#         return month
#
#     def select_date_year(self, y=random.randint(1900, 2100)):
#         self.element_is_visible(self.locators.DATE_YEAR_DROPDOWN).click()
#         year = self.element_exists((By.CSS_SELECTOR, "select.react-datepicker__year-select>option[value=\"{}\"]".format(y)))
#         self.scroll_to_element(year)
#         year.click()
#         return str(year.text)
#
#     def check_selected_date_year(self):
#         year = self.element_is_visible(self.locators.SELECT_DATE_CONTAINER_TITLE).text.split(" ")[1]
#         return str(year)
#
#     def select_date_day(self, d=0):
#         list_of_days = self.elements_are_exist(self.locators.DATE_DAYS_LIST)
#         if not d:
#             d = random.randint(0, len(list_of_days)-1)
#         random_day = list_of_days[d]
#         text = random_day.text
#         self.double_click(random_day)
#         return str(text)
#
#     def check_selected_date_day(self):
#         self.open_select_date()
#         day = self.element_is_visible(self.locators.SELECTED_DATE_DAY).text
#         return str(day)
#
#     def get_selected_date(self):
#         date = self.element_exists(self.locators.SELECT_DATE).get_attribute("value")
#         return str(date)


class DatePickerPage(BasePage):
    locators = DatePickerPageLocators()

    def select_date(self):
        random_date = next(generated_date())
        select_date_input = self.element_exists(self.locators.SELECT_DATE)
        date_before_selecting = select_date_input.get_attribute("value")
        select_date_input.click()
        self.select_by_text(self.locators.DATE_MONTH_DROPDOWN, random_date.month)
        self.select_by_text(self.locators.DATE_YEAR_DROPDOWN, random_date.year)
        self.select_date_item_from_list(self.locators.DATE_DAYS_LIST, random_date.day)
        date_after_selecting = select_date_input.get_attribute("value")
        return date_before_selecting, date_after_selecting

    def select_date_and_time(self):
        random_date = next(generated_date())
        date_and_time_input = self.element_exists(self.locators.DATE_AND_TIME_INPUT)
        date_before_selecting = date_and_time_input.get_attribute("value")
        date_and_time_input.click()
        self.element_exists(self.locators.DATE_TIME_MONTH).click()
        self.select_date_item_from_list(self.locators.DATE_TIME_MONTH_LIST, random_date.month)
        self.element_exists(self.locators.DATE_TIME_YEAR).click()
        self.select_date_item_from_list(self.locators.DATE_TIME_YEAR_LIST, "2025")
        self.select_date_item_from_list(self.locators.DATE_TIME_DAYS_LIST, random_date.day)
        self.select_date_item_from_list(self.locators.DATE_TIME_TIME_LIST, random_date.time)
        date_after_selecting = date_and_time_input.get_attribute("value")
        return date_before_selecting, date_after_selecting

    def select_date_item_from_list(self, element, value):
        list_of_days = self.elements_are_exist(element)
        for item in list_of_days:
            if item.text == value:
                self.scroll_to_element(item)
                item.click()
                break


class SlidersPage(BasePage):
    locators = SlidersPageLocators()

    def change_slider(self):
        slider = self.element_exists(self.locators.SLIDER)
        value_before = slider.get_attribute("value")
        # y is equal to 0 for moving horizontally
        self.move_slider(slider, random.randint(0, 100), 0)
        value_after = self.element_exists(self.locators.SLIDER_VALUE).get_attribute("value")
        return value_before, value_after


class ProgressBarPage(BasePage):
    locators = ProgressBarPageLocators()

    def change_progress_bar(self):
        progress_bar = self.element_exists(self.locators.PROGRESS_BAR)
        before_starting = str(progress_bar.get_attribute("style")).split(" ")[1]
        start = self.element_exists(self.locators.START_BUTTON)
        start.click()
        time.sleep(random.randint(2, 5))
        start.click()
        after_starting = str(progress_bar.get_attribute("style")).split(" ")[1]
        return before_starting, after_starting


class TabsPage(BasePage):
    locators = TabsPageLocators()

    def check_tabs(self, tab_name="Origin"):
        tab = {
            "What": {"button": self.locators.WHAT,
                     "context": self.locators.WHAT_CONTEXT},
            "Origin": {"button": self.locators.ORIGIN,
                       "context": self.locators.ORIGIN_CONTEXT},
            "Use": {"button": self.locators.USE,
                    "context": self.locators.USE_CONTEXT}
        }
        button = self.element_is_visible(tab[tab_name]["button"])
        button.click()
        context = self.element_exists(tab[tab_name]["context"]).text
        return tab_name, context


class ToolTipsPage(BasePage):
    locators = ToolTipsPageLocators()

    def check_hover_texts(self, el_to_hover="button"):
        elements = {
            "button": {"el": self.locators.BUTTON_TO_HOVER,
                       "text": "You hovered over the Button"},
            "input": {"el": self.locators.INPUT_TO_HOVER,
                      "text": "You hovered over the text field"},
            "word": {"el": self.locators.WORD_TO_HOVER,
                     "text": "You hovered over the Contrary"},
            "int": {"el": self.locators.INT_TO_HOVER,
                    "text": "You hovered over the 1.10.32"}
        }
        page_title = self.element_exists(self.locators.TITLE_OF_PAGE)
        element_to_hover = self.element_exists(elements[el_to_hover]["el"])
        self.scroll_to_element(element_to_hover)
        self.hover_on_element(element_to_hover)
        actual_text = self.element_exists(self.locators.TEXT_AFTER_HOVERING).text
        self.scroll_to_element(page_title)
        self.hover_on_element(page_title)
        return actual_text, elements[el_to_hover]["text"]
