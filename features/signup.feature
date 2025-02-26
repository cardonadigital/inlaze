Feature: SignUp
Scenario: Successful signup
    Given the user is on the signup page
    When fill out the following information: fullname:"Prueba 1", email:"prueba@gmail.com", password:"*Prueba123"
    Then the user should see the following message: "Successful registration!"

Scenario: empty fields
    Given the user is on the signup page
    When fill out the following information: fullname:"Prueba 1", password:"*Prueba123"
    Then the user should see the botton SIGN UP is not clickable

Scenario: invalid email
    Given the user is on the signup page
    When fill out the following information: fullname:"Prueba 1", email:"prueba", password:"*Prueba123"
    Then the user should see the botton SIGN UP is not clickable

