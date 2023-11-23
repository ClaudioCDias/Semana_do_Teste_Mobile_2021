from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import pytest

caps = {}
caps["platformName"] = "Android"
caps["appium:platformVersion"] = "9.0"
caps["browserName"] = ""
caps["appium:appiumVersion"] = "1.22.0"
caps["appium:deviceName"] = "Samsung Galaxy S9 FHD GoogleAPI Emulator"
caps["appium:deviceOrientation"] = "portrait"
caps["appium:app"] = "storage:filename=Calculator_8.4.1 (520193683)_Apkpure.apk"
caps["appium:appPackage"] = "com.google.android.calculator"
caps["appium:appActivity"] = "com.android.calculator2.Calculator"
caps["appium:ensureWebviewsHavePages"] = True
caps["appium:nativeWebScreenshot"] = True
caps["sauce:options"] = {"name": "Appium Desktop Session -- Nov 23, 2023 1:51 PM"}
caps["appium:newCommandTimeout"] = 3600
caps["appium:connectHardwareKeyboard"] = True

# Acionador do script / código
if __name__ == '__main__':

    driver = webdriver.Remote("https://Claudiotest01:284563c6-7cc3-4093-be45-fa150d83f8fc@ondemand.us-west-1"
                              ".saucelabs.com:443/wd/hub", caps)

    el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="8")
    el1.click()
    el2 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="plus")
    el2.click()
    el3 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="5")
    el3.click()
    el4 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="equals")
    el4.click()
    el5 = driver.find_element(by=AppiumBy.ID, value="com.google.android.calculator:id/result_final")
    el5.click()

    driver.quit()
