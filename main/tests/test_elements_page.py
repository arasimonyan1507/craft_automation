from main.pages.elements_page import TextBoxPage


def test_text_box_page(drive):
    page = TextBoxPage(driver=drive, url="https://demoqa.com/text-box")
    page.open()
    input_data = page.fill_all_fields()
    output_data = page.check_filled_forms()
    assert input_data == output_data, "something went wrong"
