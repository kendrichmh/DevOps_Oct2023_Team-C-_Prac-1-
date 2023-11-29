Feature: Sort Categories
    
	Background: Common Steps
		Given   Chrome browser is Launched
		When    Open Toyster page


	Scenario: Sort Categories
		Then MainMenu Sorting
		Then Categories Sorting
		Then SortBy
		And Close browser

	

