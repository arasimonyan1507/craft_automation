import time

import allure
import pytest
from main.pages.forms_page import PracticeFormPage


@allure.suite("Test Practice Form Page")
class TestPracticeFormPage:
    @allure.title("test practice form page")
    def test_practice_form_page(self, driver_with_add_blocker):
        practice_form_page = PracticeFormPage(driver_with_add_blocker, "https://demoqa.com/automation-practice-form")
        practice_form_page.open()
        input_data = practice_form_page.fill_student_registration_form()
        output_data = practice_form_page.check_filled_registration_form()
        for el in input_data:
            assert el in output_data, "something went wrong during filling the student registration data"
