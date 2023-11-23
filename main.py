from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


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

    # def testar_somar_dois_numeros():

     driver = webdriver.Remote("https://Claudiotest01:284563c6-7cc3-4093-be45-fa150d83f8fc@ondemand.us-west-1"
                              ".saucelabs.com:443/wd/hub", caps)

     resultado_esperado = '13'

     btn8 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="8")
     btn8.click()
     btn_somar = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="plus")
     btn_somar.click()
     btn5 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="5")
     btn5.click()
     btn_igual = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="equals")
     btn_igual.click()
     btn_resultado_final = driver.find_element(by=AppiumBy.ID, value="com.google.android.calculator:id/result_final")
     print(f'resultado final = {btn_resultado_final.text} \n resultado esperado = {resultado_esperado}')

     assert btn_resultado_final.text == resultado_esperado

     driver.quit()