# Feature: Adding items from Cart
Feature: Verify Toyster Website is able to add the items to cart 

# Common Steps (pre-requisite)
    Background: Common Steps 
        Given Chrome browser is Launched 
        When Open Toyster page
        Then Verify Toyster title is present
        Then Click on category

# Scenario 1: Add to cart
    Scenario: Add items to cart
        Then Click on item
        Then Click on add to cart
        Then Click on cart
        Then Verify items are in cart
        And Close Browser

