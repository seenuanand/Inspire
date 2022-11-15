Feature: Create And Delete New Post
  Scenario: Login to Inspire Site And Create a New Post And Delete the Newly Created Post
    Given User Launches the Chrome Browser
    When User Opens the Home Page In Chrome and Clicks Sign In Button
    And User Enters UserName "srinivas.anand1@gmail.com" And Password "Srinivas@12345" In Chrome
    And User Clicks the Login Submit Button In Chrome
    And User Must Successfully Login to His Dashboard Page In Chrome
    And User Selects Community Blood Pressure In Chrome
    And User Clicks Create Post Button In Chrome
    And User Will Add All the mandatory Post Details and Submits Post In Chrome
    And New Post is Successfully Created Verified
    Then Delete the Newly Created Post and Logout
