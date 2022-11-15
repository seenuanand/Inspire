Feature: Verify Inspire Home Page

  Scenario: Inspire Logo Present in Home Page
    Given Launch Chrome Browser
    When Open Inspire Home Page
    Then Verify the Title of the Page
    And CLose The Browser