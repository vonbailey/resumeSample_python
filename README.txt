Created with Eclipse IDE for C/C++ Developers - Version: Neon.3 Release (4.6.3)
Python Version: 3.5.3
Creator: Von Bailey
Program Name: ProgResume
Purpose: Interact with various web browsers and search engines 
         to display ability to creating a program that can interact
         with websites on the internet.

Requirements: 
	1) Windows Environment
	2) Python 3.5.3 installed
	3) Selenium Webdrivers installed (IE, Firefox)
	4) Connection to the internet

NOTE:  All options will leave a log of the test functions  in the directory the application is run in.

Start application by starting the "WebInteraction.py" file in the folder in a dos shell.

1) type 'python WebInteraction.py' and press enter. 
2) A menu will appear offering four different options:
	a) Validate Password Test 
		i) This will open a sign in page on the interent to demonstrate sign in validation
		ii) It will also go through the process of managing a forgotten password process.
	b) Count images on given URL
		i) The user will be given the option of entering a URL.  Once submitted, the application
		will open the URL and give a count of the images of 4 different types on the page.
	c) Count images in search results
		i) The user will select a browser, search engine and search criteria.  From that the
		application will do a search using the users information and return a count of the 
		images of 4 different types of included in the search results. 

CURRENT BUGS:
1) The chrome driver will not go to the designated web page.  It's a chrome issue, continue to search for resolution.  Until resolution discovered, it will message user in console and return.

NEW FEATURE:
Automated "forgot password" test cases have been added.