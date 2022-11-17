Feature: Browse Communities
  Scenario: Login to Inspire and Browse the Communities And Search for available Name
    Given User Launches Chrome Browser
    When User Clicks the Login Button in the Home Page
    And User Enters Valid User Name "srinivas.anand1@gmail.com" and Password "Srinivas@12345"
    And User Click the Login Button
    And User Must Successfully Login to His Dashboard Page
    And User Selects the Browse Community Link from Discover Inspire
    And User Should Successfully Navigate to Find Your Comminity Page
    And User Clears the Search Text and Search community by Name "Joint Pain"
    Then User Should See the Community Results  for Joint Pain and User Logs Out

  Scenario: Login to Inspire and Browse the Communities And Search for Non-available Name
    Given User Launches Chrome Browser
    When User Clicks the Login Button in the Home Page
    And User Enters Valid User Name "srinivas.anand1@gmail.com" and Password "Srinivas@12345"
    And User Click the Login Button
    And User Must Successfully Login to His Dashboard Page
    And User Selects the Browse Community Link from Discover Inspire
    And User Should Successfully Navigate to Find Your Comminity Page
    And User Clears the Search Text and Search community by Name "ASDFLKJMNNA"
    Then User Should See the No  Search Result for "ASDFLKJMNNA" and User Logs Out

  Scenario: Login to Inspire and Browse the Communities And Search By Category
    Given User Launches Chrome Browser
    When User Clicks the Login Button in the Home Page
    And User Enters Valid User Name "srinivas.anand1@gmail.com" and Password "Srinivas@12345"
    And User Click the Login Button
    And User Must Successfully Login to His Dashboard Page
    And User Selects the Browse Community Link from Discover Inspire
    And User Should Successfully Navigate to Find Your Comminity Page
    And User Selects The Browse By Category Tab
    Then Verify That User Should See the Results in Alphabetic Assending Order And User Logs out

  Scenario Outline: Login to Inspire and Browse the Communities And Search for Multiple available Name
    Given User Launches Chrome Browser
    When User Clicks the Login Button in the Home Page
    And User Enters Valid User Name "srinivas.anand1@gmail.com" and Password "Srinivas@12345"
    And User Click the Login Button
    And User Must Successfully Login to His Dashboard Page
    And User Selects the Browse Community Link from Discover Inspire
    And User Should Successfully Navigate to Find Your Comminity Page
    And User Clears the Search Text and Search community by Name "<DiseaseName>"
    Then User Should See the Community Results  for Joint Pain and User Logs Out

    Examples:
    | DiseaseName |
    | Joint Pain |
    | Blood Diseases |
    | Allergies |
    | Eating Disorders |
    | Yoga and Meditation |
