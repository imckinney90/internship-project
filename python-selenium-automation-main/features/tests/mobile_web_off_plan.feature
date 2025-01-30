Feature: Verify Titles and Pictures on the "Off Plan" Page for Mobile Web
#@smoke
  Scenario: Verify Titles and Pictures on the "Off Plan" Page
    Given Open the main page
    When Log in with valid credentials for web
    Then Verify the "Off plan" page is displayed
    And Verify each product contains a visible title and picture
