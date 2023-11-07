Feature: Test Chatbot interactability
    Background: Common Steps
        Given Chrome browser is Launched
        When Open Toyster page
    Scenario: Check Chatbot
        Then Click Toyster Chatbot
        And Close browser
    Scenario: Go Product Page
        Then Select Product
        And Close browser