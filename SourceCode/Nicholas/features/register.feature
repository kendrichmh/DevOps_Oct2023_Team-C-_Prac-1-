Feature: Verify User Account Creation

    Background: Common Steps
        Given Chrome browser is Launched
        When Open Toyster Register Account page

    Scenario Outline: Validate Successful Form Submission
        Then Input multiple "<firstName>" and "<lastName>" and "<email>" and "<password>"
        And Click Create
        Then Navigate to My Account Page
        Then Verify Account is Created
        And Close browser

    Examples:
        | firstName | lastName  | email                                   | password                           |
        | BLANK     | Doe       | john_doe0@gmail.com                     | abcd1234                           |
        | May       | BLANK     | may_goh0@outlook.com                    | p@ssword                           |
        | BLANK     | BLANK     | noname0@icloud.com                      | blahBlah                           |
        | Harry     | Soh       | h4rry.s0h0@testmail.com                 | aVeryyyLoooongPasswordddd          |
        | Alice     | Low       | aliceinwonderland0@long.long.email.com  | pass1234!@#$%                      |


    Scenario Outline: Validate Invalid Form Submission
        Then Input multiple "<firstName>", "<lastName>", "<email>" and "<password>"
        And Click Create
        Then Navigate to My Account Page
        Then Verify Account is not Created
        And Close browser

    Examples:
        | firstName | lastName  | email                                   | password                           |
        | John      | Doe       | BLANK                                   | abcd1234                           |
        | May       | Goh       | may_goh0@outlook.com                    | BLANK                              |
        | Harry     | Soh       | invalid_mail.com                        | aValidPassword                     |
        | Alice     | Low       | invalid_mail2.com                       | BLANK                              |
        | Existing  | Email     | aliceinwonderland0@long.long.email.com  | aVeryyyLoooongPasswordddd          |