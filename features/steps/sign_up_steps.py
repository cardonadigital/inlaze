from selenium import webdriver
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from pages.signup_page import SignupPage
from utils.driver_manager import DriverManager


@given(u'the user is on the signup page')
def step_impl(context):
    context.driver = webdriver.Chrome()  # Ensure ChromeDriver is installed
    context.driver.get("https://test-qa.inlaze.com/auth/sign-up")
    context.signup_page = SignupPage(context.driver)


@when(u'fill out the following information: fullname:"{fullname}", email:"{email}", password:"{password}"')
def step_impl(context, fullname, email, password):
    print(fullname, email, password)
    context.signup_page.enter_fullname(fullname)
    context.signup_page.enter_email(email)
    context.signup_page.enter_password(password)
    context.signup_page.repeat_password(password)
    context.signup_page.click_signup()

@when(u'fill out the following information: fullname:"{fullname}", password:"{password}"')
def step_impl(context, fullname, password):
    print(fullname, password)
    context.signup_page.enter_fullname(fullname)
    context.signup_page.enter_password(password)
    context.signup_page.repeat_password(password)



@then(u'the user should see the following message: "{text}"')
def step_impl(self, text):
    driver = DriverManager.get_driver(self)
    time.sleep(3) 
    # Esperar hasta que el elemento sea visible (máx. 10 segundos)
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, f"(//div[contains(text(), '{text}')])[last()]"))
    )

    # Hacer el assert
    assert element.is_displayed(), "El elemento no está visible"


@then(u'the user should see the botton SIGN UP is not clickable')
def step_impl(self):
    driver = DriverManager.get_driver(self)
    time.sleep(3) 
    # Esperar hasta que el elemento sea visible (máx. 10 segundos)
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/app-root/app-sign-up/main/section[2]/app-sign-up-form/form/button"))
    )

    # Hacer el assert
    assert not element.is_enabled(), "El elemento no es clickeable"