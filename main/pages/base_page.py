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
        self.driver.get(self.url)

    def element_is_visible(self, selector, timeout=20):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(selector))

    def elements_are_visible(self,selector,timeout=10):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(selector))

    def element_is_clickable(self, selector, timeout=10):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(selector))

    def element_exists(self, selector, timeout=10):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(selector))

    def elements_are_exist(self,selector,timeout=10):
        return wait(self.driver,timeout).until(EC.presence_of_all_elements_located(selector))

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

