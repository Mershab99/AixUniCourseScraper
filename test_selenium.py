from selenium import webdriver
import time

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

time.sleep(5)

try:
    driver = webdriver.Remote(command_executor='http://chromedriver:4444/wd/hub',
                              desired_capabilities=DesiredCapabilities.CHROME)

    time.sleep(10)
    driver.get("www.google.ca")
    print("******************* TEST SUCCESSFUL *********************")
    driver.close()
except:
    driver.close()
