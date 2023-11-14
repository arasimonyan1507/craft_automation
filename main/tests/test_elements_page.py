import random
import time
import pytest
from main.pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablesPage


@pytest.mark.skip
def test_text_box_page(drive):
    text_box_page = TextBoxPage(driver=drive, url="https://demoqa.com/text-box")
    text_box_page.open()
    input_data = text_box_page.fill_all_fields()
    output_data = text_box_page.check_filled_forms()
    assert input_data == output_data, "something went wrong"


@pytest.mark.skip
def test_check_box_page(drive):
    check_box_page = CheckBoxPage(driver=drive, url="https://demoqa.com/checkbox")
    check_box_page.open()
    check_box_page.open_full_list()
    check_box_page.check_random_checkboxes()
    boxes_input = check_box_page.get_list_of_checked_checkboxes()
    boxes_output = check_box_page.get_output_list_of_checkboxes()
    assert boxes_input == boxes_output, "checkboxes_input!==checkboxes_output"


@pytest.mark.skip
def test_radio_button_page(drive):
    radio_button_page = RadioButtonPage(drive, 'https://demoqa.com/radio-button')
    radio_button_page.open()
    yes_output = radio_button_page.click_on_button_and_check("yes")
    impressive_output = radio_button_page.click_on_button_and_check("impressive")
    no_output = radio_button_page.click_on_button_and_check("no")
    assert yes_output == "yes", "'yes' hasn't been selected successfully"
    assert impressive_output == "impressive", "'Impressive' hasn't been selected successfully"
    # assert no_output == "no", "'no' haven't been selected successfully"


@pytest.mark.skip
def test_web_tables_page(drive):
    web_tables_page = WebTablesPage(drive, "https://demoqa.com/webtables")
    web_tables_page.open()
    new_person = web_tables_page.add_new_person(2)
    list_of_people = web_tables_page.check_new_added_person()
    assert new_person in list_of_people


@pytest.mark.skip
def test_search_of_web_tables_page(drive):
    web_tables_page = WebTablesPage(drive, "https://demoqa.com/webtables")
    web_tables_page.open()
    random_keyword_of_person = web_tables_page.add_new_person()[random.randint(0, 5)]
    web_tables_page.search_person(random_keyword_of_person)
    row = web_tables_page.check_search_person()
    assert random_keyword_of_person in row, "person is not found"


@pytest.mark.skip
def test_web_table_update_person_info(drive):
    web_tables_page = WebTablesPage(drive, "https://demoqa.com/webtables")
    web_tables_page.open()
    new_persons_name = web_tables_page.add_new_person()[0]
    web_tables_page.search_person(new_persons_name)
    updated_data = web_tables_page.update_person()
    row = web_tables_page.check_search_person()
    assert updated_data in row, "data is not updated"


@pytest.mark.skip
def test_web_table_delete_person(drive):
    web_tables_page = WebTablesPage(drive, "https://demoqa.com/webtables")
    web_tables_page.open()
    new_person_email = web_tables_page.add_new_person()[3]
    web_tables_page.search_person(new_person_email)
    web_tables_page.delete_person()
    text_after_deleting = web_tables_page.check_person_is_deleted()
    assert text_after_deleting == "No rows found"


@pytest.mark.skip
def test_web_tables_change_rows_count(drive):
    web_tables_page = WebTablesPage(drive, "https://demoqa.com/webtables")
    web_tables_page.open()
    data = web_tables_page.change_count_of_rows()
    assert data == [5, 10, 20, 25]







