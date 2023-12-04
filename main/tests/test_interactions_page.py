import time

import allure
import pytest
from main.pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage, \
    RevertDraggablePage, DraggablePage


@allure.suite("Test Sortable Page")
class TestSortablePage:
    @allure.title("test change list")
    def test_change_list(self, driver_with_add_blocker):
        sortable_page = SortablePage(driver_with_add_blocker, "https://demoqa.com/sortable")
        sortable_page.open()
        before, after = sortable_page.change_list_order()
        assert before != after, "List items are not changed successfully"

    @allure.title("test change grid")
    def test_change_grid(self, driver_with_add_blocker):

        sortable_page = SortablePage(driver_with_add_blocker, "https://demoqa.com/sortable")
        sortable_page.open()
        before, after = sortable_page.change_grid_items()
        assert before != after, "Grid items are not changed successfully"


@allure.suite("Test Selectable Page")
class TestSelectablePage:
    @allure.title("test select from list")
    def test_select_from_list(self, driver_with_add_blocker):
        selectable_page = SelectablePage(driver_with_add_blocker, "https://demoqa.com/selectable")
        selectable_page.open()
        list_items_input, list_items_output = selectable_page.select_from_list()
        grid_items_input, grid_items_output = selectable_page.select_from_grid()
        assert list_items_input == list_items_output, "List items are not selected correctly: Input` {}, Output` {}".format(list_items_input, list_items_output)
        assert grid_items_input == grid_items_output, "Grid items are not selected correctly: Input` {}, Output` {}".format(grid_items_input, grid_items_output)


@allure.suite("Test Resizable Page")
class TestResizablePage:

    @allure.title("test resizable box")
    def test_resizable_box(self, driver_with_add_blocker):
        resizable_page = ResizablePage(driver_with_add_blocker, "https://demoqa.com/resizable")
        resizable_page.open()
        min_box_size, max_box_size = resizable_page.change_resizable_box()
        min_size, max_size = resizable_page.change_resizable()
        assert ('150px', '150px') == min_box_size, "Resizable boxes min size is incorrect: Expected`('150px', '150px'), Actual` {}".format(min_box_size)
        assert ('500px', '300px') == max_box_size, "Resizable boxes max size is incorrect: Expected`('500px', '300px'), Actual` {}".format(max_box_size)
        assert ("20px", "20px") == min_size,"Resizables min size is incorrect: Expected`('500px', '300px'), Actual` {}".format(min_size)


@allure.suite("Test Droppable Page")
class TestDroppablePage:
    @allure.title("test simple tag")
    def test_simple_tag(self, driver_with_add_blocker):
        droppable_page = DroppablePage(driver_with_add_blocker, "https://demoqa.com/droppable")
        droppable_page.open()
        simple_drop_message = droppable_page.simple_drag()
        assert simple_drop_message == "Dropped!", "'Drag me' element is dropped incorrectly: Expected` Dropped!, Actual` {}".format(simple_drop_message)

    @allure.title("test accept tag")
    def test_accept_tag(self, driver_with_add_blocker):
        droppable_page = DroppablePage(driver_with_add_blocker, "https://demoqa.com/droppable")
        droppable_page.open()
        not_acceptable_message = droppable_page.accept_drag("not acceptable")
        acceptable_message = droppable_page.accept_drag()
        assert not_acceptable_message == "Drop here", "Not acceptable element is dropped incorrectly: Expected` Dropped!, Actual` {}".format(not_acceptable_message)
        assert acceptable_message == "Dropped!", "Acceptable element is dropped incorrectly: Expected` Dropped!, Actual` {}".format(acceptable_message)

    @allure.title("test revert draggable")
    def test_revert_draggable(self, driver_with_add_blocker):
        droppable_page = RevertDraggablePage(driver_with_add_blocker, "https://demoqa.com/droppable")
        droppable_page.open()
        will_revert_message, revert_left = droppable_page.will_revert()
        assert will_revert_message == "Dropped!"
        assert revert_left == "0px"
        not_revert_message, not_revert_left = droppable_page.not_revert()
        assert will_revert_message == "Dropped!"
        assert not_revert_left != "0px"


    # def test_propogation_color(self, headless_driver):
    #     droppable_page = RevertPropogationPage(headless_driver, "https://demoqa.com/droppable")
    #     droppable_page.open()
    #     droppable_page.check_color()
    #     time.sleep(5)

@allure.suite("Test Draggable Page")
class TestDraggablePage:
    @allure.title("test simple drag")
    def test_simple_drag(self, headless_driver):
        draggable_page = DraggablePage(headless_driver, "https://demoqa.com/dragabble")
        draggable_page.open()
        pos_before, pos_after = draggable_page.simple_drag()
        assert pos_before != pos_after, "Simple drags position is not changed correctly: Before` {}, After` {}".format(pos_before, pos_after)

    @allure.title("test axis restricted")
    def test_axis_restricted(self, headless_driver):
        draggable_page = DraggablePage(headless_driver, "https://demoqa.com/dragabble")
        draggable_page.open()
        x_left, x_top = draggable_page.x_restricted()
        y_left, y_top = draggable_page.y_restricted()
        assert x_left != "0px" and x_top == "0px", "Restricted X doesn't work correctly"
        assert y_left == "0px" and y_top != "0px", "Restricted Y doesn't work correctly"

    @allure.title("test restricted container")
    def test_restricted_container(self, headless_driver):
        draggable_page = DraggablePage(headless_driver, "https://demoqa.com/dragabble")
        draggable_page.open()
        position = draggable_page.move_contained_box()
        assert position[0] < 496 and position[1] < 107, "Contained box is out of borders: Allowed` [496, 107], Actual` {}".format(position)
