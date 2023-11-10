import time
import random
from main.pages.base_page import BasePage
from main.selectors.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonLocators
from main.generator.generator import generated_person
from selenium.webdriver.common.by import By


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        sub = self.element_is_visible(self.locators.SUBMIT)
        self.scroll_to_element(sub)
        self.find_and_click(self.locators.SUBMIT)
        return full_name, email

    def check_filled_forms(self):
        full_name = self.element_exists(self.locators.SUBMITTED_FULL_NAME).text.split(":")[1]
        email = self.element_exists(self.locators.SUBMITTED_EMAIL).text.split(":")[1]
        # current_address = self.element_exists(self.locators.SUBMITTED_CURRENT_ADDRESS).text.split(":")[1]
        # permanent_address = self.element_exists(self.locators.SUBMITTED_CURRENT_ADDRESS).text.split(":")[1]
        return full_name, email


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL).click()

    def check_random_checkboxes(self):
        list_of_checkboxes = self.elements_are_visible(self.locators.LIST_OF_CHECKBOXES)
        count = random.randint(1, 16)
        while count:
            random_checkbox = list_of_checkboxes[random.randint(0, 16)]
            self.scroll_to_element(random_checkbox)
            random_checkbox.click()
            count -= 1

    def get_list_of_checked_checkboxes(self):
        checked_list = self.elements_are_exist(self.locators.CHECKED_CHECKBOX)
        data = []
        for box in checked_list:
            title = box.find_element(By.XPATH, self.locators.ITEM_TITLE)
            data.append(title.text)
        return str(data).replace(" ", "").replace(".doc", "").lower()

    def get_output_list_of_checkboxes(self):
        output_list = self.elements_are_exist(self.locators.CHECKBOXES_OUTPUT)
        output_data = []
        for output_title in output_list:
            output_data.append(output_title.text)
        return str(output_data).replace(" ", "").lower()


class RadioButtonPage(BasePage):
    locators = RadioButtonLocators()

    def click_on_button_and_check(self, radio_button):
        choices = {
            "yes": self.locators.YES_RADIO_BUTTON,
            "no": self.locators.NO_RADIO_BUTTON,
            "impressive": self.locators.IMPRESSIVE_RADIO_BUTTON
        }
        el = self.element_is_visible(choices[radio_button])
        el.click()
        selected_buttons_name = self.element_exists(self.locators.OUTPUT_RESULT).text
        return selected_buttons_name.lower()
