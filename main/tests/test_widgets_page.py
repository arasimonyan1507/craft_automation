from main.pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage, SlidersPage, ProgressBarPage, \
    TabsPage, ToolTipsPage, MenuPage, SelectMenuPage
import allure
import pytest


@allure.suite("Test Accordian")
class TestAccordianPage:
    @allure.title("test accordian page")
    def test_accordian_page(self, drive):
        accordian_page = AccordianPage(drive, "https://demoqa.com/accordian")
        accordian_page.open()
        first_title, first_content = accordian_page.check_accordian("first")
        second_title, second_content = accordian_page.check_accordian("second")
        third_title, third_content = accordian_page.check_accordian("third")
        assert first_title == "What is Lorem Ipsum?", "First accordions title is incorrect"
        assert len(first_content) > 0, "First accordions name is incorrect"
        assert second_title == "Where does it come from?", "Second accordions title is incorrect"
        assert len(second_content) > 0, "Second accordions name is incorrect"
        assert third_title == "Why do we use it?", "Third accordions title is incorrect"
        assert len(third_content) > 0, "Third accordions name is incorrect"


@allure.suite("Test Auto Complete")
class TestAutoCompletePage:
    @allure.title("test multiple complete input")
    def test_multiple_complete_input(self, drive):
        auto_complete_page = AutoCompletePage(drive, "https://demoqa.com/auto-complete")
        auto_complete_page.open()
        input_of_colors, output_of_colors = auto_complete_page.check_multiple_complete_input()
        assert input_of_colors == output_of_colors, "Multiple colors are not selected correctly"

    @allure.title("test single complete input")
    def test_single_complete_input(self, drive):
        auto_complete_page = AutoCompletePage(drive, "https://demoqa.com/auto-complete")
        auto_complete_page.open()
        color_input, color_output = auto_complete_page.check_single_complete_input()
        assert color_input == color_input, "Single color is not selected correctly"

    @allure.title("test delete all colors button")
    def test_delete_all_colors_button(self, drive):
        auto_complete_page = AutoCompletePage(drive, "https://demoqa.com/auto-complete")
        auto_complete_page.open()
        colors_are_deleted = auto_complete_page.check_delete_all_colors_button()
        assert colors_are_deleted == True, "Colors are not deleted successfully"

    @allure.title("test delete exact color")
    def test_delete_exact_color(self, drive):
        auto_complete_page = AutoCompletePage(drive, "https://demoqa.com/auto-complete")
        auto_complete_page.open()
        count_before_deleting, count_after_deleting = auto_complete_page.check_delete_exact_color_button()

# class TestDatePickerPage:
#     def test_select_date(self, driver_with_add_blocker):
#         date_picker_page = DatePickerPage(driver_with_add_blocker, "https://demoqa.com/date-picker")
#         date_picker_page.open()
#         date_picker_page.open_select_date()
#         m_input, m_name = date_picker_page.select_date_month()
#         m_output = date_picker_page.check_selected_date_month()
#         y_input = date_picker_page.select_date_year()
#         y_output = date_picker_page.check_selected_date_year()
#         d_input = date_picker_page.select_date_day()
#         d_output = date_picker_page.check_selected_date_day()
#         selected_date = date_picker_page.get_selected_date()
#         assert m_name == m_output, "Month selection failed: Input{}, Output{}".format(m_name, m_output)
#         assert y_input == y_output, "Year selection failed: Input{}, Output{}".format(y_input, y_output)
#         assert d_input == d_output,  "Day selection failed: Input{}, Output{}".format(d_input, d_output)
#         assert all(el in selected_date for el in [d_input, m_input, y_input]), "Selection failed {}".format(selected_date)


@allure.suite("Test Date Picker Page")
class TestDatePickerPage:
    @allure.title("test select date")
    def test_select_date(self, driver_with_add_blocker):
        date_picker_page = DatePickerPage(driver_with_add_blocker, "https://demoqa.com/date-picker")
        date_picker_page.open()
        date_before_selecting, date_after_selecting = date_picker_page.select_date()
        assert date_before_selecting != date_after_selecting, "Date selection failed: Before{}, After{}".format(
            date_before_selecting, date_after_selecting)

    @allure.title("test select date and time")
    def test_select_date_and_time(self, driver_with_add_blocker):
        date_picker_page = DatePickerPage(driver_with_add_blocker, "https://demoqa.com/date-picker")
        date_picker_page.open()
        date_before_selecting, date_after_selecting = date_picker_page.select_date_and_time()
        assert date_before_selecting != date_after_selecting, "Date selection failed: Before{}, After{}".format(
            date_before_selecting, date_after_selecting)


@allure.suite("Test Sliders Page")
class TestSlidersPage:
    @allure.title("test sliders")
    def test_sliders(self, driver_with_add_blocker):
        sliders_page = SlidersPage(driver_with_add_blocker, "https://demoqa.com/slider")
        sliders_page.open()
        value_before, value_after = sliders_page.change_slider()
        assert value_before != value_after, "Slider works incorrectly: Before` {}, After` {}".format(value_before,
                                                                                                     value_after)


@allure.suite("Test Progress Bar Page")
class TestProgressBarPage:
    @allure.title("test progress bar")
    def test_progress_bar(self, driver_with_add_blocker):
        progress_bar_page = ProgressBarPage(driver_with_add_blocker, "https://demoqa.com/progress-bar")
        progress_bar_page.open()
        before_starting, after_starting = progress_bar_page.change_progress_bar()
        assert before_starting < after_starting, "Progress has not been changed: Before` {}, After` {}".format(
            before_starting, after_starting)


@allure.suite("Test Tabs Page")
class TestTabsPage:
    @allure.title("test tabs")
    def test_tabs(self, driver_with_add_blocker):
        tabs_page = TabsPage(driver_with_add_blocker, "https://demoqa.com/tabs")
        tabs_page.open()
        tab_2, context_2 = tabs_page.check_tabs()
        tab_3, context_3 = tabs_page.check_tabs("Use")
        assert len(context_2) > 50, "Content of {} tab is inccorect".format(tab_2)
        assert len(context_3) > 50, "Content of {} tab is inccorect".format(tab_3)


@allure.suite("Test Tool Tips Page")
class TestToolTipsPage:
    @allure.title("test hover text")
    def test_hover_text(self, drive):
        tool_tips_page = ToolTipsPage(drive, 'https://demoqa.com/tool-tips')
        tool_tips_page.open()
        button_text, input_field_text, word_text, integer_text = tool_tips_page.get_hover_texts()
        assert button_text == 'You hovered over the Button', "Button hover text is incorrect: Expected` {}, Actual` {}".format('You hovered over the Button', button_text)
        assert input_field_text == 'You hovered over the text field', "Input hover text is incorrect: Expected` {}, Actual` {}".format('You hovered over the text field', input_field_text)
        assert word_text == 'You hovered over the Contrary', "Word hover text is incorrect: Expected` {}, Actual` {}".format('You hovered over the Contrary', word_text)
        assert integer_text == 'You hovered over the 1.10.32', "Word hover text is incorrect: Expected` {}, Actual` {}".format('You hovered over the 1.10.32', integer_text)

    # def test_hover_texts(self, driver_with_add_blocker):
    #     tool_tips_page = ToolTipsPage(driver_with_add_blocker, 'https://demoqa.com/tool-tips')
    #     tool_tips_page.open()
    #     button_actual_text, button_expected_text = tool_tips_page.check_hover_texts("button")
    #     word_actual_text, word_expected_text = tool_tips_page.check_hover_texts("word")
    #     int_actual_text, int_expected_text = tool_tips_page.check_hover_texts("int")
    #     assert button_actual_text == button_expected_text, "Button hover text is incorrect: Expected` {}, Actual` {}".format(
    #         button_expected_text, button_actual_text)
    #     assert word_actual_text == word_expected_text, "Word hover text is incorrect: Expected` {}, Actual` {}".format(
    #         word_expected_text, word_actual_text)
    #     assert int_actual_text == int_expected_text, "Int hover text is incorrect: Expected` {}, Actual` {}".format(
    #         int_expected_text, int_actual_text)


class TestMenuPage:
    @allure.title("test menu titles")
    def test_menu_titles(self, drive):
        menu_page = MenuPage(drive, "https://demoqa.com/menu#")
        menu_page.open()
        titles = menu_page.check_menu_titles()
        assert titles == ['Main Item 1', 'Main Item 2', 'Sub Item', 'Sub Item', 'SUB SUB LIST »', 'Sub Sub Item 1', 'Sub Sub Item 2', 'Main Item 3'], "Menu titles are incorrect: Expected` {}, Actual` {}".format(['Main Item 1', 'Main Item 2', 'Sub Item', 'Sub Item', 'SUB SUB LIST »', 'Sub Sub Item 1', 'Sub Sub Item 2', 'Main Item 3'], titles)


@allure.suite("Test Select Menu Page")
class TestSelectMenuPage:
    @allure.title("test select menu")
    def test_select_menu(self, driver_with_add_blocker):
        select_menu_page = SelectMenuPage(driver_with_add_blocker, "https://demoqa.com/select-menu")
        select_menu_page.open()
        input_value, output_value = select_menu_page.select_value()
        input_one_value, output_one_value = select_menu_page.select_one()
        # select_menu_page.select_old_style_value()
        colors_input, colors_output = select_menu_page.select_multiselect_dropdown()
        values_are_deleted = select_menu_page.delete_multivalues()
        select_menu_page.standard_select()
        assert input_value == output_value, "Value is not selected correctly: Input` {}, Output` {}".format(input_value, output_value)
        assert input_one_value == output_one_value, "One value is not selected correctly: Input` {}, Output` {}".format(input_one_value, output_one_value)
        assert colors_input == colors_output, "Colors are not selected correctly:Input` {}, Output` {}".format(colors_input, colors_output)
        assert values_are_deleted == True, "Values are not deleted successfully"
