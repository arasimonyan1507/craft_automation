import time
import random
from main.pages.base_page import BasePage
from main.selectors.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablesPageLocators
from main.generator.generator import generated_person, generated_registration_form
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
    locators = RadioButtonPageLocators()

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
    



class WebTablesPage(BasePage):
    locators = WebTablesPageLocators()

    def add_new_person(self, count=1):
        while count:
            reg_form = next(generated_registration_form())
            first_name = reg_form.first_name
            last_name = reg_form.last_name
            email = reg_form.email
            age = str(reg_form.age)
            salary = str(reg_form.salary)
            department = reg_form.department
            self.element_is_visible(self.locators.ADD_BUTTON).click()
            self.element_is_visible(self.locators.FIRST_NAME_INPUT).send_keys(first_name)
            self.element_is_visible(self.locators.LAST_NAME_INPUT).send_keys(last_name)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
            self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
            count -= 1
            return [first_name, last_name, age, email, salary, department]

    def get_list_of_people(self):
        people_list = self.elements_are_exist(self.locators.PEOPLE_LIST)
        people_data = []
        for person in people_list:
            people_data.append(person.text.splitlines())
        return people_data

    def check_new_added_person(self):
        list_of_people = self.elements_are_exist(self.locators.PEOPLE_LIST)
        people_data = []
        for el in list_of_people:
            people_data.append(el.text.splitlines())
        return people_data

    def search_person(self, key_word):
        search_field = self.element_is_visible(self.locators.SEARCH_FIELD)
        search_field.send_keys(key_word)
        return search_field

    def check_search_person(self):
        delete_button = self.element_is_visible(self.locators.DELETE_BUTTON)
        rows = delete_button.find_element(By.XPATH, self.locators.PARENT_ROW)
        return rows.text.splitlines()

    def update_person(self):
        new_person_info = next(generated_registration_form())
        new_email = new_person_info.email
        self.element_is_visible(self.locators.EDIT_BUTTON).click()
        email_input = self.element_is_visible(self.locators.EMAIL_INPUT)
        email_input.clear()
        email_input.send_keys(new_email)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        return new_email

    def delete_person(self):
        self.element_is_visible(self.locators.DELETE_BUTTON).click()

    def check_person_is_deleted(self):
        rows_not_found = self.element_is_visible(self.locators.ROWS_NO_FOUND)
        return rows_not_found.text

    def change_count_of_rows(self):
        list_of_count_rows = [5, 10, 20, 25]
        data = []
        for x in list_of_count_rows:
            row_dropdown = self.element_exists(self.locators.ROWS_DROPDOWN)
            self.scroll_to_element(row_dropdown)
            row_dropdown.click()
            count_row = self.element_is_visible((By.CSS_SELECTOR, f'span.select-wrap.-pageSizeOptions>select>option['
                                                                  f'value="{x}"]'))
            count_row.click()
            data.append(self.check_count_of_rows_is_changed())
        return data

    def check_count_of_rows_is_changed(self):
        list_of_people = self.elements_are_exist(self.locators.PEOPLE_LIST)
        return len(list_of_people)












