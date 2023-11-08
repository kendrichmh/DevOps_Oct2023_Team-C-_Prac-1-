Feature: Search for toy in the Website

	Background: Common Steps
		Given   Chrome browser is Launched
		When    Open Toyster page


	Scenario: Fill  in the search bar  with keyword
		Then 	Input Toyname "Bluey"
		Then Select Search
		Then View Product 	
		And Close browser




