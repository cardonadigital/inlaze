from selenium import webdriver
from behave import *
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from utils.driver_manager import DriverManager

@given("the user is on the login page")
def step_open_login_page(context):
    context.driver = webdriver.Chrome()  # Ensure ChromeDriver is installed
    context.driver.get("https://test-qa.inlaze.com/auth/sign-in")
    context.login_page = LoginPage(context.driver)

@when('the user enters "{username}" as username')
def step_enter_username(context, username):
    context.login_page.enter_username(username)

@when('the user enters "{password}" as password')
def step_enter_password(context, password):
    context.login_page.enter_password(password)

@when("the user clicks the login button")
def step_click_login(context):
    context.login_page.click_login()

@then("the user should be redirected to the dashboard")
def step_verify_dashboard(context):
    time.sleep(2)  # Wait for page load
    assert "Dashboard" in context.driver.title
    context.driver.quit()


@then(u'the user should see an alert with the text: "{text}"')
def step_impl(self, text):
    driver = DriverManager.get_driver(self)
    time.sleep(3) 
    # Esperar hasta que el elemento sea visible (máx. 10 segundos)
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, f"(//div[contains(text(), '{text}')])[last()]"))
    )

    # Hacer el assert
    assert element.is_displayed(), "El elemento no está visible"


@then(u'the user should see the botton SIGN IN is not clickable')
def step_impl(self):
    driver = DriverManager.get_driver(self)
    time.sleep(3) 
    # Esperar hasta que el elemento sea visible (máx. 10 segundos)
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/app-root/app-sign-in/main/section[1]/app-sign-in-form/form/button"))
    )

    # Hacer el assert
    assert not element.is_enabled(), "El elemento no es clickeable"