# Feature: Removing items from Cart
Feature: Verify Toyster Website is able to remove the items to cart 

# Common Steps (pre-requisite)
    Background: Common Steps 
        Given Chrome browser is Launched 
        When Open Toyster page
        Then Verify Toyster title is present
        Then Click on category

# Scenario 2: Remove from cart
    Scenario: Remove items from cart

        #Items need to be added before testing (pre-requisite)
        Then Click on item
        Then Click on add to cart
        Then Click on cart
        Then Verify items are in cart
        
        #Removes Items from here
        Then Click on remove 
        Then Verify items are not in cart
        And Close Browser
