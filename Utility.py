# Python Version: 3.5.3
# Creator: Von Bailey
# Program Name: ProgResume
# This module is for generic classes & functions and all data

import LogFile
import time

class ProgData:
    pData=True
    # Version of the App
    def versioning(self):
        return "3.0"  # Optimized logging process and added saving an image of the search results in the log folder.

    def dateString(self):
        return time.strftime("%H%M%S%m%d%y")
         
    def logDateString(self):
        return time.strftime("%H:%M:%S-%m/%d/%y")

    def Header(self):
            vr=ProgData.versioning(True)
            return" Created with Visual Studios Express 2013\n Python Version: 3.4.3\n Creator: Von Bailey\n Program Name: ProgResume\n Program Log\n Version: "+vr+"\n"

    def webSites(self):
        # Web URLs
        i=["http://www.google.com","http://www.bing.com","http://www.yahoo.com"];
        return i;

    def seacrhCriteria(self):
        # Search Criteria
        i=input("****Please Enter Your Search Criteria****\nEnter 'QUIT' in upper case to quit the program\n>>> ");
        return i;

    def browsers(self):
        # Browsers
        i=["Internet Explorer","Chrome","Firefox"];
        return i;
    
    def imageFiles(self):
        # Image file types
        i=[".jpg",".bmp",".gif",".png","Image Total:"];
        return i
    
    def seMenuOpt(self,i,theLogFile):
        # Menu Options 
        if self:
            try:
                if(i==0):
                    mItem= input("***Pick a Search Engine***\n0= Google\n1= Bing\n2= Yahoo \nQ= Quit Program\n>>> ");
                else:
                    mItem= input("***Pick a Browser***\n0= IE\n1= Chrome\n2= Firefox\nQ= Quit Program\n>>> ");
                return mItem
            except:
                print(ErrorSyntax.setMenuOptionsError())
                y=ErrorSyntax.ers
                LogFile.loggingData.writeLog(y,theLogFile,ErrorSyntax.setMenuOptionsError())

    def searchField(self,sf,theLogFile):
        # Attempting to identify the search field name for the correct search engine.
        try:
            if(sf==0 or sf==1):
                sfName="q" # Google and Bing
            else:
                sfName="p" # Yahoo
            return sfName
        except:
            print (ErrorSyntax.searchFieldError())
            y=ErrorSyntax.ers
            LogFile.loggingData.writeLog(y,theLogFile,ErrorSyntax.searchFieldError())

    def searchEngines(self,se):
        ses = ["Google","Bing","Yahoo"]
        i=ses[se]
        return i
    
    def log_Header(self):
        return "\n Python Version: 3.5.3 \n Creator: Von Bailey \n Program Name: ProgResume"

class Menu():
    mn=True
    def menuItems(self,x,theLogFile):
        try:
            i=ProgData.seMenuOpt(True,x,theLogFile)
            return i
        except:
            print (ErrorSyntax.menuItems(True))
            y=ErrorSyntax.ers
            LogFile.loggingData.writeLog(y,theLogFile,ErrorSyntax.menuItems(True))

    def validate_MenuItem(self,x,theLogFile):
        try:
            c=0
            validate = False
            mChoices=['0','1','2'] # Only valid options
            while c < 3:
                if(x==mChoices[c]):
                    validate=True
                    c=4  # Found it.  
                else:
                    c=c+1 # Still looking
            if(validate==True):
                return x  
            else:
                return False
        except:
            print (ErrorSyntax.menuItems(True))
            y=ErrorSyntax.ers
            LogFile.loggingData.writeLog(y,theLogFile,ErrorSyntax.validate_MenuItem(x))

class GenericSyntax():
    gs=True
    def images(self):
        return " images:"

    def searchCriteria(self):
        return " Instances of the search criteria: "

    def SynRnProg(self,URL,Browser,SC):
        return " Browser URL: "+ URL+" | Selected Browser:  "+Browser+" | Search Criteria:  "+ SC

    def Failure(self,txt,pk):
        if(pk==0):
            return " Failed to reach: "+txt
        elif(pk==1):
            return " Failed to create: "+txt
        elif(pk==2):
            return " Failed to retrieve: "+txt
        else:
            return " Failed to enter: "+txt

    def Success(self,txt,pk):
        if(pk==0):
            return " Successfully reached: "+txt
        elif(pk==1):
            return " Succesfully created: "+txt
        elif(pk==2):
            return " Succesfully retrieved: "+txt
        else:
            return " Succesfully entered: "+txt

    def quitMsg(self):
        return " Exiting the program"

    def quitting(self):
        return "QUIT"

    def quit(self):
        return "Q"

    def false(self):
        return "false"

    def true(self):
        return "true"

    def HTTP(self):
        return "http"

    def logTitles(self,x):
        i = [" ***********************CREATING MENU***********************",
             " ***********************PICKING SEARCH ENGINE***********************",
             " ***********************STARTING APPLICATION***********************", 
             " ***********************COUNTING IMAGES***********************",
             " ***********************COUNTING MATCHING TEXT***********************"];
        return i[x]

class TheURL():
    ul=True
    def get_URL(self,i):
        if(i>2 or i< 0): return str(i) # takes care of bad selection
        urlsList=ProgData.webSites(True)
        return urlsList[i]

class Browsers():
    br=True
    def get_brw(self,i):
        if(i>2 or i< 0): return str(i) # takes care of bad selection
        bwr=ProgData.browsers(True)
        return bwr[i]    

class ErrorSyntax():
    ers=True
    def missingSC(self,sc):
        # Error when nothing on the search results page matches the search criteria
        return "WARNING:  Could not find an instance of the search criteria '"+sc+"' in the search results."

    def validate_MenuItem(self,x):
        # Error validating menu choice
        return "ERROR: validate_MenuItem("+x+")"

    def setValidateSearchEngineError(self,title,se):
        return "ERROR: setValidateSearchEngineError("+title+","+se+")"

    def setMenuOptionsError(self):
        # Error if there is an issue setting the menu options
        return "ERROR:  setMenuOptionsError()"

    def searchFieldError(self):
        # Error if program fails to identify the search filed name
        return  "ERROR:  searchFieldError(Failed to identify the search field name)"

    def menuItems(self):
        # Error if program fails to create one of the menus
        return "ERROR:  doMenu(Failed to create the menu)"

    def menuError(self):
        # Error if the menu has a problem colleting data
        return "ERROR: Failed Main_MenuOptions()"

    def mainError(self):
        # Error if there is an issue after all variables have been set and it's not a menu issue.
        return "ERROR: Failed Main()"
        
    def dataColletion(self):
        # Error collecting data to run the application
        return "ERROR: Failed Main_DataColletion()"

    def setBrowserError(self,b,theName):
        # Error gathering information regarding setting up the browser.
        return "ERROR: Failed setBrowser("+b+","+theName+")"

    def openBrowserError(self,theName):
        # # Error opening the browser.
        return "ERROR: Failed openBrowser(Browser"+theName+")"

    def countAspectsError(self,url):
        # Error counting images in the HTTP request
        return "ERROR:  Failed attempting to find images in countAspects("+url+")"