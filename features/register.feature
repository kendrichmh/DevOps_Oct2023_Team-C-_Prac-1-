Feature: Verify User Account Creation

Background: Common Steps
    Given Chrome browser is Launched
    When Open Toyster page
    Then Navigate to Register Account page

Scenario Outline: Validate Successful Form Submission
    Then Input multiple "<firstName>", "<lastName>", "<email>" and "<password>"
    And Click Create
    Then Navigate to My Account Page
    Then Verify Account is Created
    Then Close browser

Examples:
    | firstName | lastName  | email                                  | password                           |
    |           | Doe       | john_doe@gmail.com                     | abcd1234                           |
    | May       |           | may_goh@outlook.com                    | p@ssword                           |
    |           |           | noname@icloud.com                      | blahBlah                           |
    | Harry     | Soh       | h4rry.s0h@testmail.com                 | aVeryyyLoooongPasswordddd          |
    | Alice     | Low       | aliceinwonderland@long.long.email.com  | pass1234!@#$%                      |


Scenario Outline: Validate Invalid Form Submission
    Then Input multiple "<firstName>", "<lastName>", "<email>" and "<password>"
    And Click Create
    Then Navigate to My Account Page
    Then Verify Account is not Created
    Then Close browser

Examples:
    | firstName | lastName  | email                                  | password                           |
    | John      | Doe       |                                        | abcd1234                           |
    | May       | Goh       | may_goh@outlook.com                    |                                    |
    | Harry     | Soh       | invalid_mail.com                       | aValidPassword                     |
    | Alice     | Low       | invalid_mail2.com                      |                                    |
    | Existing  | Email     | aliceinwonderland@long.long.email.com  | aVeryyyLoooongPasswordddd          |