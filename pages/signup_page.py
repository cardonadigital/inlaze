from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.driver_manager import DriverManager

class SignupPage(BasePage):
    FULLNAME_FIELD = (By.ID, 'full-name')
    EMAIL_FIELD = (By.ID, 'email')
    PASSWORD_FIELD = (By.XPATH, '(//*[@id="password"])[2]')
    CONFIRM_PASSWORD_FIELD = (By.XPATH, '(//*[@id="confirm-password"])[2]')
    SIGNUP_BUTTON = (By.XPATH, "/html/body/app-root/app-sign-up/main/section[2]/app-sign-up-form/form/button")

    def enter_fullname(self, fullname):
        self.enter_text(self.FULLNAME_FIELD, fullname)

    def enter_email(self, email):
        self.enter_text(self.EMAIL_FIELD, email)

    def enter_password(self, password):
        self.enter_text(self.PASSWORD_FIELD, password)

    def repeat_password(self, password):
        self.enter_text(self.CONFIRM_PASSWORD_FIELD, password)

    def click_signup(self):
        self.wait_until_clickable(self.SIGNUP_BUTTON)
        self.click_element(self.SIGNUP_BUTTON)