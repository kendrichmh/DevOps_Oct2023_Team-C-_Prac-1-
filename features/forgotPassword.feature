Feature: Login to the Toyster Website

  Background:
    Given Chrome browser is Launched
    When Open Toyster page
    When they click the login link
    Then they should be redirected to the login page

  Scenario: Get Email to Update Password
    When Click Forgot Password
    And Enter email "elliot.ngwk@gmail.com" to reset Password
    And Click Submit
    Then see We've sent you an email with a link to update your password

