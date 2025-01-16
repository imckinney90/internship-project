Feature: Verify Titles and Pictures on the "Off Plan" Page

  Scenario: Verify Titles and Pictures on the "Off Plan" Page
    Given Open the main page
    And Log in with valid credentials
    When Navigate to the "Off plan" page via the left-side menu
    Then Verify the "Off plan" page is displayed
    And Verify each product contains a visible title and picture

