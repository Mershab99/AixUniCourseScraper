from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def login(username, password):
    time.sleep(5)
    driver = webdriver.Remote(command_executor='http://chromedriver:4444/wd/hub',
                              desired_capabilities=DesiredCapabilities.CHROME)

    login_url = "https://ident.univ-amu.fr/cas/login"
    url1 = "https://pagesinterscol.univ-amu.fr/prod/acc_ip.php"

    driver.get(login_url)

    driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/section/div/div/form/span/section[1]/input').send_keys(username)
    driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/section/div/div/form/span/section[2]/div/input').send_keys(password)

    driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/section/div/div/form/span/div/button').click()
