from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.driver_manager import DriverManager

class LoginPage(BasePage):
    USERNAME_FIELD = (By.ID, 'email')
    PASSWORD_FIELD = (By.XPATH, '(//*[@id="password"])[2]')
    LOGIN_BUTTON = (By.XPATH, "/html/body/app-root/app-sign-in/main/section[1]/app-sign-in-form/form/button")

    def enter_username(self, username):
        self.enter_text(self.USERNAME_FIELD, username)

    def enter_password(self, password):
        self.enter_text(self.PASSWORD_FIELD, password)

    def click_login(self):
        self.wait_until_clickable(self.LOGIN_BUTTON)
        self.click_element(self.LOGIN_BUTTON)
