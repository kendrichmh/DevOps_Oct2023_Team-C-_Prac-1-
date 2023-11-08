Feature: Search for toy in the Website

	Background: Common Steps
		Given   Chrome browser is Launched
		When    Open Toyster page

	Scenario: Check Toyster Title
		Then Verify Toyster Title is present
		And Close browser

	Scenario: Fill  in the search bar  with keyword
		Then Input Toyname "Bluey"
		Then Select Search	
		And View Product 	
	





