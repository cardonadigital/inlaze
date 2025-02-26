from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.driver_manager import DriverManager

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def click_element(self, locator):
        element = self.find_element(locator)
        element.click()

    def wait_until_clickable(self, locator, timeout=10):
        """Wait until an element is clickable and return it."""
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((locator))
        )

    def enter_text(self, locator, text):
        driver = DriverManager.get_driver(self)
        search_box = driver.find_element(*locator)
        search_box.send_keys(text)