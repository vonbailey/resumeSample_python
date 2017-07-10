# Python Version: 3.5.3
# Creator: Von Bailey
# Program Name: ProgResume
# Purpose: Performs all logging aspects of the program
import Utility
import os
import logging


class loggingData():
    log_it=True
    def writeLog(self,theLogFile,theLogEntry):
        if self:
            logging.basicConfig(filename=theLogFile,level=logging.INFO)
            logging.info(theLogEntry)
            print("\n"+Utility.ProgData.logDateString(True)+":  "+theLogEntry)

    def dirName(self):
        if self:
            hDirectory=os.path.dirname(os.path.realpath("WebInteraction.py"))
            theFileString=Utility.ProgData.dateString(True)
            theDir=hDirectory+"\Log_"+theFileString
            os.mkdir(theDir)
            return [theDir,theFileString]

    def fileName(self,theDir,theFileString):
        if self:
            theLogFile = theDir+"\LogFile_"+theFileString+".log"
            return theLogFile
