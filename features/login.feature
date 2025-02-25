Feature: Logueo usuario
  Scenario: Logueo exitoso de usuario
    Given the user is on the login page
    When the user enters "testuser" as username
    And the user enters "testpass" as password
    And the user clicks the login button
    Then the user should be redirected to the dashboard
  