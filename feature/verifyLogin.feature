Feature: Inspire Login
  Scenario: Login to Inspire Web Site and Verify Valid Login
    Given User Launches the Browser
    When User Opens the Home Page and Clicks Sign In Button
    And User Enters UserName "srinivas.anand1@gmail.com" And Password "Srinivas@12345"
    And User Clicks the Login Submit Button
    Then User Must Successfully Login to His Dashboard Page

  Scenario: Login to Inspire Web Site With Multiple Credentials
    Given User Launches the Browser
    When User Opens the Home Page and Clicks Sign In Button
    And User Enters UserName "<userName>" And Password "<password>>"
    And User Clicks the Login Submit Button
    Then User Must Successfully Login to His Dashboard Page

    Examples:
        | userName | password |
        | srinivas.anand1@gmail.com | password |
        | srinivas.anand1@gmail.com | Srinivas@12345 |
        | srinivas.anand1@gmail.com | Srinivas@123 |