Feature: Logging
@smoke
Scenario: Successful logging
    Given the user is on the login page
    When the user enters "prueba12@gmail.com" as username
    And the user enters "*Prueba123" as password
    And the user clicks the login button
    Then the user should be redirected to the dashboard

@smoke
Scenario: incorrect email
    Given the user is on the login page
    When the user enters "prueba12" as username
    And the user enters "*Prueba123" as password
    And the user clicks the login button
    Then the user should see an alert with the text: "User not found"

  Scenario: incorrect password
    Given the user is on the login page
    When the user enters "prueba12@gmail.com" as username
    And the user enters "*prueba" as password
    Then the user should see the botton SIGN IN is not clickable


    
  
  