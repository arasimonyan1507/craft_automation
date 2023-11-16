import random
import time
from pathlib import Path

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from main.pages.base_page import BasePage
from main.selectors.forms_page_locators import PracticeFormPageLocators
from main.generator.generator import generated_student_registration_form, generated_file, generated_subject_set


class PracticeFormPage(BasePage):
    locators = PracticeFormPageLocators()

    def fill_student_registration_form(self):
        student_data = next(generated_student_registration_form())
        first_name = student_data.first_name
        last_name = student_data.last_name
        email = student_data.email
        phone_number = student_data.phone_number[0:10]
        file_name, file_path = generated_file()
        Path.unlink(file_path)
        self.element_is_visible(self.locators.FIRST_NAME_FIELD).send_keys(first_name)
        self.element_is_visible(self.locators.LAST_NAME_FIELD).send_keys(last_name)
        self.element_is_visible(self.locators.EMAIL_FIELD).send_keys(email)
        self.element_exists(self.locators.GENDER).click()
        self.element_is_visible(self.locators.MOBILE_NUMBER_FIELD).send_keys(phone_number)
        subjects = self.choose_subjects()
        hobbies = self.choose_hobbies()
        self.element_is_visible(self.locators.CHOOSE_FILE).send_keys(file_path)
        self.scroll_to_element(self.element_exists(self.locators.STATE_DROPDOWN))
        self.element_is_visible(self.locators.STATE_DROPDOWN).click()
        self.element_is_visible(self.locators.STATE_NAME).click()
        self.element_is_visible(self.locators.CITY_DROPDOWN).click()
        self.element_is_visible(self.locators.CITY_NAME).click()
        # zoom - for submit button to be visible
        zoom_level = [0.5, 1]
        self.driver.execute_script(f"document.body.style.zoom = '{zoom_level[0]}';")
        self.scroll_to_element(self.element_exists(self.locators.SUBMIT))
        button = self.element_exists(self.locators.SUBMIT)
        button.send_keys(Keys.RETURN)
        self.driver.execute_script(f"document.body.style.zoom = '{zoom_level[1]}';")
        return [first_name+" "+last_name, email, phone_number, subjects, hobbies]

    def check_filled_registration_form(self):
        filled_data = []
        rows = self.elements_are_exist(self.locators.STUDENT_TABLE_DATA)
        for row in rows:
            filled_data.append(row.text)
        return filled_data

    def choose_hobbies(self, *hobbies):
        hobby_list = []
        if not hobbies:
            hobbies = [1, 3]
        for el in hobbies:
            hobby = self.element_exists(
                (By.CSS_SELECTOR, f'div[class^="custom-control"]>label[for="hobbies-checkbox-{el}"]'))
            self.scroll_to_element(hobby)
            hobby_list.append(hobby.text)
            hobby.click()
        return ', '.join(hobby_list)

    def choose_subjects(self):
        subject_set = generated_subject_set()
        subject_field = self.element_exists(self.locators.SUBJECTS_FIELD)
        self.scroll_to_element(subject_field)
        for subject in subject_set:
            subject_field.send_keys(subject)
            subject_field.send_keys(Keys.RETURN)
        return ", ".join(subject_set)
