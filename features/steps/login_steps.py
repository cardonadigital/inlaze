from selenium import webdriver
from behave import *
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
import time

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
