import random

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        try:
            self.driver.get(self.url)
        except Exception as error:
            print("here is the error")
            print(error)
            raise TypeError

    def element_is_visible(self, selector, timeout=20):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(selector))

    def elements_are_visible(self, selector, timeout=10):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(selector))

    def element_is_clickable(self, selector, timeout=10):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(selector))

    def element_exists(self, selector, timeout=10):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(selector))

    def elements_are_exist(self, selector, timeout=10):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(selector))

    def find_and_click(self, selector):
        self.driver.find_element(selector[0],selector[1]).click()

    def scroll_to_element(self, selector):
        # self.driver.find_element(selector).send_keys(Keys.PAGE_DOWN)
        self.driver.execute_script("arguments[0].scrollIntoView();", selector)

    def element_is_invisible(self, selector, timeout=10):
        return wait(self.driver, timeout).until(EC.invisibility_of_element(selector))

    def action_double_click(self, element):
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    def action_right_click(self, element):
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()

    def action_click_on_element(self,element):
        action = ActionChains(self.driver)
        action.click(element)
        action.perform()

    def remove_footer(self, footer_locator):
        self.driver.execute_script(f"document.querySelector({footer_locator}).style.display='none';")

    def switch_to_tab_or_window(self, tab_or_window_index):
        self.driver.switch_to.window(self.driver.window_handles[tab_or_window_index])

    def switch_to_frame(self, frame_to_switch):
        self.driver.switch_to.frame(frame_to_switch)

    def double_click(self, locator):
        action = ActionChains(self.driver)
        action.double_click(locator)
        action.perform()

    def select_by_text(self, element, text):
        select = Select(self.element_exists(element))
        select.select_by_visible_text(text)

    def move_slider(self, element, x, y):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, x, y)
        action.perform()

    def hover_on_element(self,element):
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()



