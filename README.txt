Created with Visual Studios Express 2013
Python Version: 3.4.3150.1013
Creator: Von Bailey
Program Name: ProgResume
Purpose: Interact with various web browsers and search engines 
         to display ability to creating a program that can interact
         with websites on the internet.

Requirements: 
	1) Windows Environment
	2) Python 3.4.3 installed
	3) Selenium Webdrivers installed (IE, Chrome, Firefox)

Start application by starting the "WebInteraction.py" file in the folder in a dos shell.
1) A menu will appear.  Make a selection.
2) A second menu will appear.  Make a selection.
3) Enter search criteria.

The browser will start, access the search engine selected and submit the search criteria.  

The application will: 
	1) Count the images in the search results.
	2) Count how many times the search criteria appears in the search results.
	3) Take a snapshot of the webpage displayed by the browser.
	4) Create log and directory in the directory in which the application is started
		i.e. if the application is started in "C:\%user%\Desktop", the log will be in that directory.
	5) Store all relevant actions in a log file.
	6) Save snapshot from #3 and save it in the log directory.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++	
CURRENT BUGS:
1) The chrome driver will not go to the designated web page.  It's a chrome issue, continue to search for resolution.
Until resolution discovered, it will message user in console and return.

2) RESOLVED: There is something wrong with a logging issue in the selBin on line 44.  For some reason it creates an error.
Discover why it's erroring out and resolve.***SOLUTION - Add booleen True at to recognize self in defs.***

3) RESOLVED: The process errors out after it gets to the webpage.  It does not continue to count the images.  Find out where the error is and resolve.  
	***SOLUTION - Was searching URL instead of page source.  Changed value to pages source and it works now.***
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++	
CURRENT DEVELOPMENT:
1) COMPLETE:  Create another menu that calls the current program and include it as an option.  In the new menu add the following:
	a) The ability to count the images on any given page.
	b) Validate Passwords
2) Create functionality to perform 1a
	The user should be able to enter any webpage and get a count of all images that appear on the page.
3) Create functionality to perform 1b
	a) A password page is necessary, defining the correct attributes of a good password and login
	b) The test should check for the length of both the password and login
	c) The test should verify that the password has a numeric, alpha and special character in it.
	d) The test should verify that the login is an email address
	e) The test should verfity that any error messages that should appear are displayed. 
