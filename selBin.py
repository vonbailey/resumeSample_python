# Python Version: 3.5.3
# Creator: Von Bailey
# Program Name: ProgResume
# Purpose: Performs all selenium functions


#import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import traceback
import Utility
import LogFile


class procPasswords():
    creds=True
    
    def updateFields(self,driver,theLogFile,):
        try:
            em=driver.find_element_by_id('emailAddress')
            p1=driver.find_element_by_id('password1')
            p2=driver.find_element_by_id('password2') 
            return em,p1,p2 
        except:
            LogFile.loggingData.writeLog(True,theLogFile,Utility.GenericSyntax.procCredsError(True,5)+traceback.print_stack())
    
    def updtePassword(self,http,theURL,theLogFile,theDir):
        try:
            # Accessing the forgot password page
            driver=webdriver.Firefox()
            driver.get(http+theURL)
            driver.find_element_by_id('fgotPwd').click()
            x=0
            while(x<4):
                # Entering Test Variables
                y=False
                creds,nhttp=Utility.GenericSyntax.changePwd(True,x)
                drFields= procPasswords.updateFields(True,driver,theLogFile,)
                drFields[0].send_keys(creds[0])
                drFields[1].send_keys(creds[1])
                drFields[2].send_keys(creds[1])
                driver.find_element_by_id('submitEmail').click()
                fN=creds[2].replace(' ','_')
                LogFile.loggingData.writeLog(True,theLogFile,creds[2])
                driver.get_screenshot_as_file(theDir+'\/'+fN+".png")
                validate=driver.find_element_by_id('errormsg')
                # Verifying Test Variable results
                if(x==0):
                    if(validate.get_attribute("value")=="ERROR: Please enter data in required fields labled in red characters."):
                        LogFile.loggingData.writeLog(True,theLogFile,creds[2]+"**PASSED**")
                        y=True
                elif(x==1):
                    if(validate.get_attribute("value")=="Password Not long enough.  Must be 12 characters"):
                        LogFile.loggingData.writeLog(True,theLogFile,creds[2]+"**PASSED**")
                        y=True
                elif(x==2):
                    if(validate.get_attribute("value")=="ERROR: Please enter data in required fields labled in red characters."):
                        LogFile.loggingData.writeLog(True,theLogFile,creds[2]+"**PASSED**")
                        y=True
                elif(x==3):
                    if(validate.get_attribute("value")=="Successfully updated password"):
                        LogFile.loggingData.writeLog(True,theLogFile,creds[2]+"**PASSED**")
                        y=True
                if(y==False):
                    LogFile.loggingData.writeLog(True,theLogFile,creds[2]+"**FAILED**")                  
                x=x+1
                driver.get(nhttp)
            # Closing test
            driver.close()
        except:
            LogFile.loggingData.writeLog(True,theLogFile,Utility.GenericSyntax.procCredsError(True,4)+traceback.print_stack())
    
    def passCreds(self,http,theURL,theLogFile,theDir):
        try:
            cred=Utility.ProgData.getIN(True)
            driver=webdriver.Firefox()
            driver.get(http+theURL)
            x=0 #A flag defining which test is being run
            y=0 #Selecting the login from the 'cred' array
            z=1 #Selecting the password from the 'cred' array
            while(x<5):
                procPasswords.enterCreds(True,x,cred[y],cred[z],theLogFile,driver,http,theURL,theDir)
                x=x+1
                y=y+2
                z=z+2
            driver.close()
        except:
            LogFile.loggingData.writeLog(True,theLogFile,Utility.GenericSyntax.procCredsError(True,0)+traceback.print_stack())                     

    def getCredFields(self,driver,theLogFile):
        try:
            lName=driver.find_element_by_id('loginCred') 
            lPword=driver.find_element_by_id('passwd')
            subMit=driver.find_element_by_id('submit')
            return[lName,lPword,subMit]
        except: 
            LogFile.loggingData.writeLog(True,theLogFile,Utility.GenericSyntax.procCredsError(True,1))      
            
  
    def enterCreds(self,creds,cred1,cred2,theLogFile,driver,http,theURL,theDir):
        try:
            credLabels=Utility.ProgData.getCredlbl(True)
            LogFile.loggingData.writeLog(True,theLogFile,credLabels[creds]+cred1+", "+cred2)
            lgn=procPasswords.getCredFields(True,driver,theLogFile)
            # Performing the test
            lgn[0].click() #Clicking on the login field
            lgn[0].send_keys(cred1) #Filling the login field
            lgn[1].send_keys(cred2) #Filling the password
            lgn[2].click()#Submitting the information
            fN=credLabels[creds].replace(' ','_')
            driver.get_screenshot_as_file(theDir+'\/'+fN+".png")
            # Verifying the results in the logs.
            
            if(creds==0): # Verifying that the correct credentials will work
                if(driver.title==credLabels[5]):
                    LogFile.loggingData.writeLog(True,theLogFile,fN+credLabels[6])
                else:
                    LogFile.loggingData.writeLog(True,theLogFile,fN+credLabels[7])
            else:
                    if(driver.title==credLabels[9]):
                        LogFile.loggingData.writeLog(True,theLogFile,fN+credLabels[6])
                    else:
                        LogFile.loggingData.writeLog(True,theLogFile,fN+credLabels[7])

            driver.get(http+theURL)           
        except:
            LogFile.loggingData.writeLog(True,theLogFile,Utility.GenericSyntax.procCredsError(True,2)+traceback.print_stack()) 
            
class sel_Interaction():   
    goodSearch=True
    def doSearch(self,URL,SC,se,theLogFile,theDir,b): #Brower, URL, Search Criteria, Search Engine, Search Engine ID
        try:
            # Getting the id of the field used for searching in the search engine.
            sfName=Utility.ProgData.searchField(True,int(b),theLogFile)
            # Opening Browser
            if(b=="0"):
                driver=webdriver.Ie()
            elif(b=="1"):
                LogFile.loggingData.writeLog(True,theLogFile,"Chrome is not working at this time.")
                return
                #driver=webdriver.Chrome()
            else:
                driver=webdriver.Firefox()
            # Going to Search Engine,  Maximizing window, submitting search criteria
            driver.get(URL)
            driver.maximize_window()
            # Verifying reached correct search 
            if(driver.title==se):
                LogFile.loggingData.writeLog(True,theLogFile,Utility.GenericSyntax.Success(True,driver.title,0))
            else:
                e=Utility.ErrorSyntax.setValidateSearchEngineError(True,driver.title,se)
                LogFile.loggingData.writeLog(True,theLogFile,Utility.GenericSyntax.Failure(True,e,0))
            theElement = driver.find_element_by_name(sfName)  # Finding the search filed
            theElement.send_keys(SC+Keys.ENTER) # Entering the search criteria
            LogFile.loggingData.writeLog(True,theLogFile,Utility.GenericSyntax.Success(True,SC,3))
            time.sleep(2)
            driver.get_screenshot_as_file(theDir+"\\SearchResults_"+SC+".png")
            theSource=driver.page_source # Getting the URL of the results of the search
            driver.close()
            sel_Interaction.countAspects(True,theSource,0,SC,3,theLogFile,theDir)
            sel_Interaction.countAspects(True,theSource,1,SC,4,theLogFile,theDir)
            return 
        except:
            e=Utility.ErrorSyntax.setBrowserError(True,b)
            LogFile.loggingData.writeLog(True,theLogFile,Utility.GenericSyntax.Failure(True,e,0)+traceback.print_stack())


    def countAspects(self,theSource,tp,sc,x,theLogFile,theDir):
        try:
            # Send url via HTTP and get the HTML for the page.
            LogFile.loggingData.writeLog(True,theLogFile,Utility.GenericSyntax.logTitles(True,x))
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
            e=Utility.ErrorSyntax.countAspectsError(True,theSource)+traceback.print_stack()
            LogFile.loggingData.writeLog(True,theLogFile,e)

class giveURL():
    gURL=True
    def openGivenURl(self,theURL,theLogFile,theDir,http):
        try:
            driver=webdriver.Firefox()
            driver.get(http+theURL)
            theSource=driver.page_source
            driver.close()
            sel_Interaction.countAspects(True,theSource,0,"",3,theLogFile,theDir)
        except:
            e=Utility.ErrorSyntax.givenURLError(True)+traceback.print_stack()
            LogFile.loggingData.writeLog(True,theLogFile,e+theURL)        