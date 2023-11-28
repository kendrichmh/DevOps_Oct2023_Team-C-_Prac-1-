Feature: Login to the Toyster Website

  Background:
    Given Chrome browser is Launched
    When Open Toyster page
    When they click the login link
    Then they should be redirected to the login page

  Scenario: Successful login with valid credentials
    When the user enters valid credentials username "elliot.ngwk@gmail.com" and password "!N9Bh5sSjXyKsLM"
    And clicks the Sign In Button
    Then see My Account Page

  Scenario: Unsuccessful login with invalid credentials
    When the user enters invalid credentials username "user1234@gmail.com" and password "passwordincorrect"
    And clicks the Sign In Button
    Then they should see an error message
