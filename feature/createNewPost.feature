Feature: Create New Post
  Scenario: Login to Inspire and Submit a New Post to the Community
    Given User Launches Chrome Browser
    When User Clicks the Login Button in the Home Page
    And User Enters Valid User Name "srinivas.anand1@gmail.com" and Password "Srinivas@12345"
    And User Click the Login Button
    And User Must Successfully Login to His Dashboard Page
    And User Selects Community Blood Pressure
    And User Clicks Create Post Button
    And User Will add all the mandatory Post Details and Submits Post
    Then New Post is Successfully Created Verified and logout of the application