from selenium.webdriver.common.by import By
from main.pages.base_page import BasePage
from main.selectors.elements_page_locators import TextBoxPageLocators
from main.generator.generator import generated_person


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
        self.scroll_to_element(self.locators.SUBMIT)
        self.find_and_click(self.locators.SUBMIT)
        return full_name, email

    def check_filled_forms(self):
        full_name = self.element_exists(self.locators.SUBMITTED_FULL_NAME).text.split(":")[1]
        email = self.element_exists(self.locators.SUBMITTED_EMAIL).text.split(":")[1]
        # current_address = self.element_exists(self.locators.SUBMITTED_CURRENT_ADDRESS).text.split(":")[1]
        # permanent_address = self.element_exists(self.locators.SUBMITTED_CURRENT_ADDRESS).text.split(":")[1]
        return full_name, email
