import random
import time
import re
import pytest
from selenium.webdriver.common.by import By
from main.pages.base_page import BasePage
from main.selectors.iteractions_page_locators import SortablePageLocators, SelectablePageLocators, \
    ResizablePageLocators, DroppablePageLocators, RevertDraggablePageLocators, PreventPropogationPageLocators, \
    DraggablePageLocators
from webcolors import rgb_to_name

class SortablePage(BasePage):
    locators = SortablePageLocators()

    def get_sortable_items(self, elements):
        list_of_elements = self.elements_are_exist(elements)
        return [item.text for item in list_of_elements]

    def change_list_order(self):
        list_tab = self.element_is_visible(self.locators.TAB_LIST)
        list_tab.click()
        list_items_before = self.get_sortable_items(self.locators.LIST_ITEMS)
        change_elements_with_each_other = random.sample(self.elements_are_exist(self.locators.LIST_ITEMS), 2)
        el_1 = change_elements_with_each_other[0]
        el_2 = change_elements_with_each_other[1]
        self.drag_and_drop_to_element(el_1, el_2)
        list_items_after = self.get_sortable_items(self.locators.LIST_ITEMS)
        return list_items_before, list_items_after

    def change_grid_items(self):
        grid_tab = self.element_is_visible(self.locators.TAB_GRID)
        grid_tab.click()
        grid_items_before = self.get_sortable_items(self.locators.GRID_ITEMS)
        elements_to_change = random.sample(self.elements_are_exist(self.locators.GRID_ITEMS), 2)
        el_1 = elements_to_change[0]
        el_2 = elements_to_change[1]
        self.drag_and_drop_to_element(el_1, el_2)
        grid_items_after = self.get_sortable_items(self.locators.GRID_ITEMS)
        return grid_items_before, grid_items_after


class SelectablePage(SortablePage):
    locators = SelectablePageLocators()

    def select_from_list(self):
        list_tab = self.element_is_visible(self.locators.TAB_LIST)
        list_tab.click()
        list_items = self.elements_are_exist(self.locators.LIST_ITEMS)
        random_items = random.sample(list_items, random.randint(1, len(list_items)))
        items_to_select = []
        for item in random_items:
            items_to_select.append(item.text)
            self.scroll_to_element(item)
            item.click()
        selected_items = self.get_sortable_items(self.locators.LIST_SELECTED_ITEMS)
        return items_to_select, selected_items

    def select_from_grid(self):
        grid_tab = self.element_is_visible(self.locators.TAB_GRID)
        grid_tab.click()
        grid_items = self.elements_are_exist(self.locators.GRID_ITEMS)
        random_items = random.sample(grid_items, random.randint(1, len(grid_items)))
        items_to_select = []
        for item in random_items:
            items_to_select.append(item.text)
            self.scroll_to_element(item)
            item.click()
        selected_items = self.get_sortable_items(self.locators.GRID_SELECTED_ITEMS)
        return items_to_select, selected_items


@pytest.mark.skip
class ResizablePage(BasePage):
    locators = ResizablePageLocators()


    def get_size(self, element):
        size = element.get_attribute("style")
        return size


    def get_px_from_width_and_height(self, size: str):
        width = size.split(";")[0].split(':')[1].replace(' ', '')
        height = size.split(";")[1].split(':')[1].replace(' ', '')
        return width, height

    def change_resizable_box(self):
        self.element_is_visible(self.locators.RESIZABLE_BOX)
        self.drag_and_drop_by_offset(self.element_exists(self.locators.RESIZABLE_BOX_HANDLE), 300, 100)
        max_size = self.get_px_from_width_and_height(self.get_size(self.element_exists(self.locators.RESIZABLE_BOX)))
        self.drag_and_drop_by_offset(self.element_exists(self.locators.RESIZABLE_BOX_HANDLE), -350, -150)
        min_size = self.get_px_from_width_and_height(self.get_size(self.element_exists(self.locators.RESIZABLE_BOX)))
        return min_size, max_size

    def change_resizable(self):
        self.scroll_to_element(self.element_is_visible(self.locators.RESIZABLE))
        self.drag_and_drop_by_offset(self.element_exists(self.locators.RESIZABLE_HANDLE), -180, -180)
        min_size = self.get_px_from_width_and_height(self.get_size(self.element_exists(self.locators.RESIZABLE)))
        self.drag_and_drop_by_offset(self.element_exists(self.locators.RESIZABLE_HANDLE), 500, 500)
        max_size = self.get_px_from_width_and_height(self.get_size(self.element_exists(self.locators.RESIZABLE)))
        return min_size, max_size


class DroppablePage(BasePage):
    locators = DroppablePageLocators()

    def simple_drag(self):
        tab = self.element_is_visible(self.locators.SIMPLE_TAB)
        tab.click()
        drag_me = self.element_is_visible(self.locators.SIMPLE_DRAG_ME)
        drop_zone = self.element_is_visible(self.locators.SIMPLE_DROP_ZONE)
        self.drag_and_drop_to_element(drag_me, drop_zone)
        return drop_zone.text

    def accept_drag(self, status="acceptable"):
        tab = self.element_is_visible(self.locators.ACCEPT_TAG)
        tab.click()
        to_drag = {"acceptable": (By.ID, "acceptable"),
                   "not acceptable": (By.CSS_SELECTOR, "#notAcceptable")}
        drag_me = self.element_is_visible(to_drag[status])
        drop_zone = self.element_is_visible(self.locators.ACCEPT_DROP_ZONE)
        self.drag_and_drop_to_element(drag_me, drop_zone)
        return drop_zone.text


class RevertDraggablePage(BasePage):
    locators = RevertDraggablePageLocators()

    def will_revert(self):
        tab = self.element_is_visible(self.locators.REVERT_DRAGGABLE_TAB)
        tab.click()
        will_revert = self.element_is_visible(self.locators.WILL_REVERT)
        drop = self.element_is_visible(self.locators.REVERTABLE_DROP)
        self.drag_and_drop_to_element(will_revert, drop)
        time.sleep(1)
        left = will_revert.value_of_css_property("left")
        return drop.text, left

    def not_revert(self):
        tab = self.element_is_visible(self.locators.REVERT_DRAGGABLE_TAB)
        tab.click()
        not_revert = self.element_is_visible(self.locators.NOT_REVERT)
        drop = self.element_is_visible(self.locators.REVERTABLE_DROP)
        self.drag_and_drop_to_element(not_revert, drop)
        time.sleep(1)
        left = not_revert.value_of_css_property("left")
        return drop.text, left


# class RevertPropogationPage(BasePage):
#     locators = PreventPropogationPageLocators()
#
#     def check_color(self):
#         tab = self.element_is_visible(self.locators.PROPOGATION_TAB)
#         tab.click()
#         drop_box = self.element_is_visible(self.locators.NOT_GREEDY)
#         self.drag_and_drop_to_element(self.element_is_visible(self.locators.DRAG_ME),drop_box)



class DraggablePage(BasePage):
    locators = DraggablePageLocators()

    def drag_and_get_position(self, el_to_drag, x, y):
        el = self.element_is_visible(el_to_drag)
        position_before = el.get_attribute("style")
        self.drag_and_drop_by_offset(el, x, y)
        position_after = el.get_attribute("style")
        return position_before, position_after

    def get_left_and_top(self, el_to_drag, x, y):
        el = self.element_is_visible(el_to_drag)
        self.drag_and_drop_by_offset(el, x, y)
        position = el.get_attribute("style")
        left = position.split(";")[1].split(":")[1].replace(" ", '')
        top = position.split(";")[2].split(":")[1].replace(" ", '')
        return left, top

    def simple_drag(self):
        tab = self.element_is_visible(self.locators.SIMPLE_TAB)
        tab.click()
        return self.drag_and_get_position(self.locators.SIMPLE_DRAG_ME, random.randint(1, 100), random.randint(1, 100))

    def x_restricted(self):
        tab = self.element_is_visible(self.locators.AXIS_TAB)
        tab.click()
        random_int = random.uniform(-50, 0) if random.choice([True, False]) else random.uniform(1, 50)
        return self.get_left_and_top(self.locators.RESTRICTED_X, random_int, 0)

    def y_restricted(self):
        tab = self.element_is_visible(self.locators.AXIS_TAB)
        tab.click()
        random_int = random.uniform(-50, 0) if random.choice([True, False]) else random.uniform(1, 50)
        return self.get_left_and_top(self.locators.RESTRICTED_Y, 0, random_int)

    def get_list_of_positions(self, el_locator):
        el = self.element_is_visible(el_locator)
        position = el.get_attribute("style")
        position_list = [float(val) for val in re.findall(r'-?\d+(?:\.\d+)?', position)]
        return position_list

    def move_contained_box(self):
        self.element_is_visible(self.locators.RESTRICTED_CONTAINER_TAB).click()
        box = self.element_is_visible(self.locators.CONTAINED_BOX)
        self.drag_and_drop_by_offset(box, random.randint(10, 550), random.randint(10, 200))
        return self.get_list_of_positions(self.locators.CONTAINED_BOX)



