import os
import traceback
import webbrowser

from appium.webdriver.common.mobileby import MobileBy
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def main():
    # 1. Replace <<cloud name>> with your perfecto cloud name (e.g. demo is the cloudName of demo.perfectomobile.com).
    cloudName = "trial"

    capabilities = {
        # 2. Replace <<security token>> with your perfecto security token.
        'securityToken' : "eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI2ZDM2NmJiNS01NDAyLTQ4MmMtYTVhOC1kODZhODk4MDYyZjIifQ.eyJpYXQiOjE2MzMwMDc1OTAsImp0aSI6IjNmZGRmNzQzLTQ3MzYtNDU3ZC1iOTZjLTQwNjQ4ZWY1Y2ExZCIsImlzcyI6Imh0dHBzOi8vYXV0aDMucGVyZmVjdG9tb2JpbGUuY29tL2F1dGgvcmVhbG1zL3RyaWFsLXBlcmZlY3RvbW9iaWxlLWNvbSIsImF1ZCI6Imh0dHBzOi8vYXV0aDMucGVyZmVjdG9tb2JpbGUuY29tL2F1dGgvcmVhbG1zL3RyaWFsLXBlcmZlY3RvbW9iaWxlLWNvbSIsInN1YiI6IjNkOGNkNzQ5LTZmMjctNDg3Ny05NDUzLTA4NTBkM2U1NGFkNiIsInR5cCI6Ik9mZmxpbmUiLCJhenAiOiJvZmZsaW5lLXRva2VuLWdlbmVyYXRvciIsIm5vbmNlIjoiZTllNTlhMWYtOWExZi00OTdlLThkZTItMTI5NjIzMTdmZjY2Iiwic2Vzc2lvbl9zdGF0ZSI6IjNmMDg0Mzk2LTEzM2UtNDNkMS1iMDdmLTlmYWNkZDg4ZjMwYyIsInNjb3BlIjoib3BlbmlkIG9mZmxpbmVfYWNjZXNzIHByb2ZpbGUgZW1haWwifQ.SSCOxFx4d6Pxxa3xD4P1SAu5C9L0tYy72MCMQdmRxLY",

        # 3. Set device capabilities.
        'platformName': 'Android',
        'platformVersion': '10',
        'manufacturer': 'Samsung',
        'model': 'Galaxy A40',

        # 4. Set Perfecto Media repository path of App under test.
        'app': 'PRIVATE:1633010368319_ExpenseAppVer1.0.apk',

        # 5. Set the unique identifier of your app - this is highly recommended
        # 'appPackage': 'YOUR.APP.APPPACKAGE',

        # Set other capabilities.
        'enableAppiumBehavior': True, # Enable new architecture of Appium
        'autoLaunch': True, # Whether to have Appium install and launch the app automatically.
        'autoInstrument': True, # To work with hybrid applications, install the iOS/Android application as instrumented.
        # 'fullReset': false, # Reset app state by uninstalling app
        'takesScreenshot': False,
        'screenshotOnError': True,
        'openDeviceTimeout': 5
    }
    # Initialize the Appium driver
    driver = webdriver.Remote('https://' + cloudName + '.perfectomobile.com/nexperience/perfectomobile/wd/hub', capabilities)
    # set implicit wait time
    driver.implicitly_wait(5)

    error = None
    wait = WebDriverWait(driver, 30)

    testStart(driver, "Native Python Android Sample")
    
    ##
    #############################
    ### Your test starts here. If you test a different app, you need to modify the test steps accordingly. ###
    #############################
    ##
    
    
    ##
    #############################
    ### Your test ends here. ###
    #############################
    ##
    
    testEnd(driver, error)
    reportURL = driver.capabilities.get('testGridReportUrl') + "&onboardingJourney=automated&onboardingDevice=nativeApp"

    # Quits the driver
    driver.quit()

    print("\nOpen this link to continue with the guide: " + reportURL + "\n")

    # Launch browser with the Report URL
    webbrowser.open(reportURL)

################################################################################
# HELPER FUNCTIONS
################################################################################

def testStart(driver, testName):
    driver.execute_script("mobile:test:start", {"name": testName})

def testEnd(driver, error):
    params = {
        "success": False if error != None else True,
        "failureDescription": error
    }
    driver.execute_script("mobile:test:end", params)

def stepStart(driver, stepName):
    driver.execute_script("mobile:step:start", {"name": stepName})

def stepEnd(driver):
    driver.execute_script("mobile:step:end")

def stepAssert(driver, message):
    driver.execute_script("mobile:status:assert", {
        "status": False, "message": message})

################################################################################
# MAIN ENTRY POINT
################################################################################

if __name__ == '__main__':
    main()
