# Python Version: 3.5.3
# Creator: Von Bailey
# Program Name: ProgResume
# Purpose: Interact with various web browsers and search engines 
#          to display ability to creating a program that can interact
#          with websites on the internet.

import traceback
import Utility
import selBin
import os
import LogFile


class leaving():
    def getOUT(self,theLogFile):
        if self:
            LogFile.loggingData.writeLog(self,theLogFile,Utility.GenericSyntax.quitMsg(True),)
            os._exit(0)

class startMe():
    menu=True
            
    def doMenu2(self,ms,theLogFile,theDir):
        if self:
            try:
                # Creating menus and acccepting Menu selection
                if(ms==0): #Display the first menu for getting the search engine used
                    y=Utility.Menu.menuItems(True,1,theLogFile)
                else:#Display the second menu for getting the browser used
                    y=Utility.Menu.menuItems(True,2,theLogFile)
                # Validating that the menu options entered are valid
                x=Utility.Menu.validate_MenuItem(True,y,theLogFile)
                # If the user chooses to quit at this time.  Exit the application
                if(y.upper()==Utility.GenericSyntax.quit(True) or x==False):
                    if(x==False):
                        LogFile.loggingData.writeLog(True,theLogFile,Utility.GenericSyntax.Failure(True, y, 3))
                    leaving.getOUT(True,theLogFile)
                # Log the menu selection made
                LogFile.loggingData.writeLog(True,theLogFile,Utility.GenericSyntax.Success(True,"Menu Item: ",1)+str(ms))
                # Return menu selection made
                return y
            except:
                print(Utility.ErrorSyntax.menuError(True),theDir+traceback.print_stack())
                leaving.getOUT(True,theLogFile)

    def doDataCollection(self,u,theLogFile,theDir):
        if self:
            try:
                # Verifying data collection
                gotSC=str(Utility.ProgData.seacrhCriteria(True)) # Getting the search criteria
                LogFile.loggingData.writeLog(True,theLogFile,Utility.GenericSyntax.Success(True," Search Criteria: "+gotSC,2))
                if(gotSC.upper()==Utility.GenericSyntax.quitting(True)):
                    LogFile.loggingData.writeLog(True,theLogFile,Utility.ErrorSyntax.dataColletion(gotSC))
                    os._exit(0)
                gotURL= Utility.TheURL.get_URL(True,int(u)) # Getting the URL
                LogFile.loggingData.writeLog(True,theLogFile,Utility.GenericSyntax.Success(True," URL: "+gotURL,2))
                return [gotURL, gotSC]
            except:
                print(Utility.ErrorSyntax.dataColletion(True)+traceback.print_stack())
                leaving.getOUT(True,theLogFile)

    def doSearchEngine(self,URL,SC,brow,se,theLogFile,theDir,b1):
        if self:
            try:
                # Running program
                if(len(URL) <3 or len(SC) < 3 or len(brow) < 3): 
                    eList=[]# If any of the critiera is missing list error and return
                    eList=Utility.ErrorSyntax.mainError(True)
                    LogFile.loggingData.writeLog(True,theLogFile,eList[0]+URL+eList[1]+SC+eList[2]+brow)
                    return Utility.GenericSyntax.false(True)
                else:
                # Display selections in console
                    goodData=Utility.GenericSyntax.SynRnProg(True,URL,brow,SC)
                    LogFile.loggingData.writeLog(True,theLogFile,goodData[0])
                    c=input(goodData[1])
                    c=c.upper()
                    if(c!="Y"):
                        leaving.getOUT(True,theLogFile)
                # Opening Browser and processing search results
                    y=selBin.sel_Interaction.goodSearch
                    selBin.sel_Interaction.doSearch(y,URL,SC,se,theLogFile,theDir,b1)
            except:
                e=Utility.ErrorSyntax.mainError(True)+traceback.print_stack()
                LogFile.loggingData.writeLog(True,theLogFile,e)

def main():
    try:
        mmError=Utility.ErrorSyntax.mainMenuError(True)
        try:
            # Creating log file and directory
            dirComp=[]
            x=LogFile.loggingData.log_it
            y=startMe.menu
            dirComp=LogFile.loggingData.dirName(x)
            theDir=dirComp[0]
            theLogFile=LogFile.loggingData.fileName(x,theDir, dirComp[1])
            LogFile.loggingData.writeLog(True,theLogFile,Utility.ProgData.log_Header(True))
            #Adding header to log
            LogFile.loggingData.writeLog(x,theLogFile,Utility.GenericSyntax.logTitles(True,0))
        except:
            print(mmError[0]+traceback.print_stack())
        # Doing the menus
        
        mo=Utility.Menu.menuItems(True,0,theLogFile)
        if(mo=="0"): # Verifying login credentials.
            try:
                aURL=Utility.TheURL.getUrlValues(True)
                http=aURL[3]
                theDom=aURL[4]
                selBin.procPasswords.passCreds(True, http, theDom, theLogFile,theDir)
                selBin.procPasswords.updtePassword(True, http, theDom, theLogFile,theDir);
                leaving.getOUT(True,theLogFile)
            except:
                LogFile.loggingData.writeLog(True,theLogFile,mmError[1]+traceback.print_stack())
        elif(mo=="1"): # Counting instances of given criteria on a given web site.
            try:
                urlVars=Utility.TheURL.getUrlValues(True)
                extensions=Utility.TheURL.imageExtensions(True)
                #Collect the URL
                aURL=input(urlVars[0])
                #Validate the URL
                extCheck=Utility.TheURL.validateURL(True,aURL,extensions)
                if(extCheck==False):
                    LogFile.loggingData.writeLog(True,theLogFile,Utility.GenericSyntax.Failure(True, urlVars[1]+aURL, 0))
                    leaving.getOUT(True,theLogFile)
                LogFile.loggingData.writeLog(True,theLogFile,urlVars[2]+aURL)
                #Go to the URL and count the images
                selBin.giveURL.openGivenURl(True,aURL,theLogFile,theDir,urlVars[3])
                leaving.getOUT(True,theLogFile)
            except:
                LogFile.loggingData.writeLog(True,theLogFile,mmError[2]+traceback.print_stack())
        elif(mo=="2"): # Counting instances of given criteria of given search criteria in various search engines
            try:
                mi=0 # Setting up menus and gather menu options.
                while (mi<2):  
                    m1=startMe.doMenu2(y,mi,theLogFile,theDir)
                    if(mi==0):
                        s=m1 # assigning Search Engine
                    else:
                        b=m1 # assigning browser
                    mi=mi+1
                LogFile.loggingData.writeLog(x,theLogFile,Utility.GenericSyntax.logTitles(True,1))
                # Assigning search engine
                se=Utility.ProgData.searchEngines(True,int(s)) #This identifies the character used by teh search enging
                br=Utility.ProgData.browsers(True,int(b)) 
                # getting theURL and the Search Criteria
                dc=[];dc=startMe.doDataCollection(True,s,theLogFile,theDir) 
                LogFile.loggingData.writeLog(True,theLogFile,Utility.GenericSyntax.logTitles(True,2))
                startMe.doSearchEngine(y,dc[0],dc[1],br,se,theLogFile,theDir,int(s)) #true, URL, Search Criteria,browser,search engine,log file, directory
                leaving.getOUT(True,theLogFile)
            except:
                LogFile.loggingData.writeLog(True,theLogFile,mmError[3]+traceback.print_stack())
        elif(mo.upper()=='Q'):
            leaving.getOUT(True,theLogFile)
        else:
            LogFile.loggingData.writeLog(True,theLogFile,"Invalid selection: "+mo)
            leaving.getOUT(True,theLogFile)
    except:
        print("ERROR: Main Menu Failed to start!")
    
main()



