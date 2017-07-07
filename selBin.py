# Python Version: 3.5.3
# Creator: Von Bailey
# Program Name: ProgResume
# Purpose: Performs all selenium functions


#import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
import Utility
import LogFile

class sel_Interaction():   
    goodSearch=True
    def doSearch(self,b,u,sc,se,sen,theLogFile,theDir): #Brower, URL, Search Criteria, Search Engine, Search Engine ID
        try:
            bName=[] # List of Browser names
            bName=Utility.ProgData.browsers(True)
            theName=bName[int(b)]
            sfName=Utility.ProgData.searchField(True,int(sen),theLogFile)
            # Opening Browser
            if(b=="0"):
                driver=webdriver.Ie()
            elif(b=="1"):
                print("Chrome is not working at this time.")
                return
                #driver=webdriver.Chrome()
            else:
                driver=webdriver.Firefox()
            # Going to Search Engine,  Maximizing window, submitting search criteria
            driver.get(u)
            driver.maximize_window()
            # Verifying reached correct search http://marketplace.eclipse.org/marketplace-client-intro?mpc_install=114engine
            if(driver.title==se):
                LogFile.loggingData.writeLog(True,theLogFile,Utility.GenericSyntax.Success(True,driver.title,0))
            else:
                e=Utility.ErrorSyntax.setValidateSearchEngineError(True,driver.title,se)
                LogFile.loggingData.writeLog(True,theLogFile,Utility.GenericSyntax.Failure(True,e,0))
            theElement = driver.find_element(By.NAME, sfName)  # Finding the search filed
            theElement.send_keys(sc+Keys.ENTER) # Entering the search criteria
            LogFile.loggingData.writeLog(True,theLogFile,Utility.GenericSyntax.Success(True,sc,3))
            time.sleep(2)
            driver.get_screenshot_as_file(theDir+"\\SearchResults_"+sc+".png")
            theSource=driver.page_source # Getting the URL of the results of the search
            driver.close()
            sel_Interaction.countAspects(True,theSource,0,sc,3,theLogFile,theDir)
            sel_Interaction.countAspects(True,theSource,1,sc,4,theLogFile,theDir)
            return 
        except:
            e=Utility.ErrorSyntax.setBrowserError(True,b,theName)
            LogFile.loggingData.writeLog(True,theLogFile,Utility.GenericSyntax.Failure(True,e,0))


    def countAspects(self,theSource,tp,sc,x,theLogFile,theDir):
        try:
            # Send url via HTTP and get the HTML for the page.
            LogFile.loggingData.writeLog(True,theLogFile,Utility.GenericSyntax.logTitles(True,x))
            #pgData=str(Utility.getHTTP.retrievePageData(True,url))
            if(tp==0):
                # Check the HTML for references to the following:  imageFiles()
                img=0
                imgTotal=0
                i=[]
                i=Utility.ProgData.imageFiles(True)
                while(img<4):
                    cnt=theSource.count(i[img])
                    LogFile.loggingData.writeLog(True,theLogFile,i[img] + Utility.GenericSyntax.images(True) + str(cnt))
                    img=img+1
                    imgTotal=imgTotal+cnt
                LogFile.loggingData.writeLog(True,theLogFile,i[img] + str(imgTotal))
            else:
                cnt=theSource.count(sc)
                LogFile.loggingData.writeLog(True,theLogFile,Utility.GenericSyntax.searchCriteria(True) + sc + " = "+str(cnt))
                if(cnt<1):
                    LogFile.loggingData.writeLog(True,theLogFile,Utility.ErrorSyntax.missingSC(True,sc))
        except:
            e=Utility.ErrorSyntax.countAspectsError(True,theSource)
            LogFile.loggingData.writeLog(True,theLogFile,e)
