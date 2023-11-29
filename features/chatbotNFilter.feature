Feature: Test Chatbot interactability and Check Filter working properly
    Background: Common Steps
        Given Chrome browser is Launched
        When Open Toyster page

    #Hanisah - First test case is to check the chatbot, see if can press the suggested questions
    Scenario: Check Chatbot 
        Then Click Toyster Chatbot
        Then Click Toyster Chatbot Prompt
        And Close browser
    
    #Hanisah - Second test case it to check the product page, see if the filter works properly by selecting multiple different options
    Scenario Outline: File in with multiple dropdown option
        Then Select Product
        Then Select Filter Dropdown
        Then Input multiple "<dropdownOptions>"
        And Close browser
    Examples:
        |dropdownOptions|
        |Roblox|
        |WARHAMMER 40K|
        |Pokémon|