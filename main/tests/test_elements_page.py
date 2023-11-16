import random
import time
import pytest
from main.pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablesPage, ButtonsPage, LinksPage, \
    UploadAndDownloadPage, DynamicPropertiesPage


@pytest.mark.skip
class TestTextBoxPage:
    def test_text_box_page(self, drive):
        text_box_page = TextBoxPage(driver=drive, url="https://demoqa.com/text-box")
        text_box_page.open()
        input_data = text_box_page.fill_all_fields()
        output_data = text_box_page.check_filled_forms()
        assert input_data == output_data, "something went wrong"


@pytest.mark.skip
class TestCheckBoxPage:
    def test_check_box_page(self, drive):
        check_box_page = CheckBoxPage(driver=drive, url="https://demoqa.com/checkbox")
        check_box_page.open()
        check_box_page.open_full_list()
        check_box_page.check_random_checkboxes()
        boxes_input = check_box_page.get_list_of_checked_checkboxes()
        boxes_output = check_box_page.get_output_list_of_checkboxes()
        assert boxes_input == boxes_output, "checkboxes_input!==checkboxes_output"


@pytest.mark.skip
class TestRadioButtonPage:
    def test_radio_button_page(self, drive):
        radio_button_page = RadioButtonPage(drive, 'https://demoqa.com/radio-button')
        radio_button_page.open()
        yes_output = radio_button_page.click_on_button_and_check("yes")
        impressive_output = radio_button_page.click_on_button_and_check("impressive")
        no_output = radio_button_page.click_on_button_and_check("no")
        assert yes_output == "yes", "'yes' hasn't been selected successfully"
        assert impressive_output == "impressive", "'Impressive' hasn't been selected successfully"
        # assert no_output == "no", "'no' haven't been selected successfully"


@pytest.mark.skip
class TestWebTablesPage:
    def test_web_tables_page(self, drive):
        web_tables_page = WebTablesPage(drive, "https://demoqa.com/webtables")
        web_tables_page.open()
        new_person = web_tables_page.add_new_person(2)
        list_of_people = web_tables_page.check_new_added_person()
        assert new_person in list_of_people

    def test_search_of_web_tables_page(drive):
        web_tables_page = WebTablesPage(drive, "https://demoqa.com/webtables")
        web_tables_page.open()
        random_keyword_of_person = web_tables_page.add_new_person()[random.randint(0, 5)]
        web_tables_page.search_person(random_keyword_of_person)
        row = web_tables_page.check_search_person()
        assert random_keyword_of_person in row, "person is not found"

    def test_web_table_update_person_info(self, drive):
        web_tables_page = WebTablesPage(drive, "https://demoqa.com/webtables")
        web_tables_page.open()
        new_persons_name = web_tables_page.add_new_person()[0]
        web_tables_page.search_person(new_persons_name)
        updated_data = web_tables_page.update_person()
        row = web_tables_page.check_search_person()
        assert updated_data in row, "data is not updated"

    def test_web_table_delete_person(drive):
        web_tables_page = WebTablesPage(drive, "https://demoqa.com/webtables")
        web_tables_page.open()
        new_person_email = web_tables_page.add_new_person()[3]
        web_tables_page.search_person(new_person_email)
        web_tables_page.delete_person()
        text_after_deleting = web_tables_page.check_person_is_deleted()
        assert text_after_deleting == "No rows found"

    def test_web_tables_change_rows_count(self, drive):
        web_tables_page = WebTablesPage(drive, "https://demoqa.com/webtables")
        web_tables_page.open()
        data = web_tables_page.change_count_of_rows()
        assert data == [5, 10, 20, 25]


@pytest.mark.skip
class TestButtonsPage:
    def test_buttons_page(self, drive):
        buttons_page = ButtonsPage(drive, "https://demoqa.com/buttons")
        buttons_page.open()
        double_message = buttons_page.click_on_different_buttons("double")
        right_message = buttons_page.click_on_different_buttons("right")
        click_message = buttons_page.click_on_different_buttons("click")
        assert double_message == "You have done a double click", "The double click button was not pressed"
        assert right_message == "You have done a right click", "The right click button was not pressed"
        assert click_message == "You have done a dynamic click", "The click button was not pressed"


@pytest.mark.skip
class TestLinksPage:
    def test_simple_link(self, drive):
        links_page = LinksPage(drive, "https://demoqa.com/links")
        links_page.open()
        href_link, current_url = links_page.check_home_link()
        assert href_link == current_url, "Link is broken"

    def test_bad_request_link(self, drive):
        links_page = LinksPage(drive, "https://demoqa.com/links")
        links_page.open()
        request_status_code = links_page.check_bad_request("https://demoqa.com/bad-request")
        assert request_status_code == 400, "Link is working or status code is not equal to 400"


@pytest.mark.skip
class TestUploadAndDownloadPage:

    def test_upload_file(self, drive):
        upload_and_download_page = UploadAndDownloadPage(drive, "https://demoqa.com/upload-download")
        upload_and_download_page.open()
        file_name, uploaded_file_path = upload_and_download_page.upload_file()
        assert file_name in uploaded_file_path

    def test_download_file(self, drive):
        upload_and_download_page = UploadAndDownloadPage(drive, "https://demoqa.com/upload-download")
        upload_and_download_page.open()
        downloaded_file_status = upload_and_download_page.download_file()
        assert downloaded_file_status is True


class TestDynamicProperties:
    def test_dynamic_properties(self, drive):
        dynamic_properties_page = DynamicPropertiesPage(drive, "https://demoqa.com/dynamic-properties")
        dynamic_properties_page.open()
        color_before, color_after = dynamic_properties_page.change_color()
        assert color_before != color_after, "color has not been changed"

    def test_visibility_of_button(self, drive):
        dynamic_properties_page = DynamicPropertiesPage(drive, "https://demoqa.com/dynamic-properties")
        dynamic_properties_page.open()
        visible = dynamic_properties_page.check_visibility_after_5_sec()
        assert visible is True, "element is not visible after 5 seconds"

    def test_element_is_enabled_after_5_sec(self, drive):
        dynamic_properties_page = DynamicPropertiesPage(drive, "https://demoqa.com/dynamic-properties")
        dynamic_properties_page.open()
        clickable = dynamic_properties_page.check_element_is_clickable()
        assert clickable is True, "element is not enabled after 5 seconds"
