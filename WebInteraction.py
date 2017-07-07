# Python Version: 3.5.3
# Creator: Von Bailey
# Program Name: ProgResume
# Purpose: Interact with various web browsers and search engines 
#          to display ability to creating a program that can interact
#          with websites on the internet.

import Utility
import selBin
import os
import LogFile


class startMe():
    menu=True
    def doMenu2(self,ms,theLogFile,theDir):
        if self:
            try:
                # Creating menus and acccepting Menu selection
                if(ms==0): #Display the first menu for getting the search engine used
                    y=Utility.Menu.menuItems(True,0,theLogFile)
                elif(ms==1):#Display the second menu for getting the browser used
                    y=Utility.Menu.menuItems(True,1,theLogFile)
                # Validating that the menu options entered are valid
                x=Utility.Menu.validate_MenuItem(True,y,theLogFile)
                # If the user chooses to quit at this time.  Exit the application
                if(y.upper()==Utility.GenericSyntax.quit(True) or x==False):
                    LogFile.loggingData.writeLog(True, theLogFile,Utility.ErrorSyntax.validate_MenuItem(True,y))
                    os._exit(0)
                # Log the menu selection made
                LogFile.loggingData.writeLog(True,theLogFile,Utility.GenericSyntax.Success(True,"Menu Item: ",1)+str(ms))
                # Return menu selection made
                return y
            except:
                print(Utility.ErrorSyntax.menuError(True),theDir)
                LogFile.loggingData.writeLog(True,theLogFile,Utility.ErrorSyntax.menuError(True))
                os._exit(0)

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
                print(Utility.ErrorSyntax.dataColletion(True))
                LogFile.loggingData.writeLog(True,theLogFile,Utility.ErrorSyntax.dataColletion(True))
                os._exit(0)

    def Main(self,URL,SC,brow,u,theLogFile,theDir):
        if self:
            try:
                # Running program
                if(len(URL) <3 or len(SC) < 3 or len(brow) < 3): 
                    eList=[]
                    eList=Utility.ErrorSyntax.mainError(True)
                    print(eList[0]+URL+eList[1]+SC+eList[2]+brow)
                    LogFile.loggingData.writeLog(True,theLogFile,eList[0]+URL+eList[1]+SC+eList[2]+brow)
                    return Utility.GenericSyntax.false(True)
                else:
                    goodData=Utility.GenericSyntax.SynRnProg(True,URL,brow,SC)
                    LogFile.loggingData.writeLog(True,theLogFile,goodData)
                # Opening Browser and processing search results
                    y=selBin.sel_Interaction.goodSearch
                    selBin.sel_Interaction.doSearch(y,b,URL,SC,brow,u,theLogFile,theDir)
            except:
                e=Utility.ErrorSyntax.mainError(True)
                LogFile.loggingData.writeLog(True,theLogFile,e)

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

mi=0 # Getting the values to define the Search Engine and browser.
while (mi<2):  
    m1=startMe.doMenu2(y,mi,theLogFile,theDir)
    if(mi==0):
        u=m1 # assigning Search Engine
    else:
        b=m1 # assigning browser
    mi=mi+1

LogFile.loggingData.writeLog(x,theLogFile,Utility.GenericSyntax.logTitles(True,1))
se=Utility.ProgData.searchEngines(True,int(u))  # Assigning search engine
dc=[];dc=startMe.doDataCollection(True,u,theLogFile,theDir) # getting theURL and the Search Criteria
###########################
#RUNNING THE APPLICATION
LogFile.loggingData.writeLog(True,theLogFile,Utility.GenericSyntax.logTitles(True,2))
startMe.Main(y,dc[0],dc[1],se,u,theLogFile,theDir)

# Exiting program
LogFile.loggingData.writeLog(x,theLogFile,Utility.GenericSyntax.quitMsg(True),)

