import time
import pytest
from main.pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage


@pytest.mark.skip
def test_text_box_page(drive):
    page = TextBoxPage(driver=drive, url="https://demoqa.com/text-box")
    page.open()
    input_data = page.fill_all_fields()
    output_data = page.check_filled_forms()
    assert input_data == output_data, "something went wrong"

@pytest.mark.skip
def test_check_box_page(drive):
    page = CheckBoxPage(driver=drive, url="https://demoqa.com/checkbox")
    page.open()
    page.open_full_list()
    page.check_random_checkboxes()
    boxes_input = page.get_list_of_checked_checkboxes()
    boxes_output = page.get_output_list_of_checkboxes()
    assert boxes_input == boxes_output, "checkboxes_input!==checkboxes_output"


@pytest.mark.skip
def test_radio_button_page(drive):
    page = RadioButtonPage(drive, 'https://demoqa.com/radio-button')
    page.open()
    yes_output = page.click_on_button_and_check("yes")
    impressive_output = page.click_on_button_and_check("impressive")
    no_output = page.click_on_button_and_check("no")
    assert yes_output == "yes", "'yes' hasn't been selected successfully"
    assert impressive_output == "impressive", "'Impressive' hasn't been selected successfully"
    # assert no_output == "no", "'no' haven't been selected successfully"
