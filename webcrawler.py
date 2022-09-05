from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException


def login(username, password):
    driver = webdriver.Remote(command_executor='http://chromedriver:4444/wd/hub',
                              desired_capabilities=DesiredCapabilities.CHROME)

    login_url = "https://ident.univ-amu.fr/cas/login"

    try:
        driver.get(login_url)

        driver.find_element(By.XPATH,
                            '/html/body/div[2]/main/div/div/section/div/div/form/span/section[1]/input').send_keys(
            username)
        driver.find_element(By.XPATH,
                            '/html/body/div[2]/main/div/div/section/div/div/form/span/section[2]/div/input').send_keys(
            password)

        driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/section/div/div/form/span/div/button').click()
        print('*************** LOGIN SUCCESSFULLY *******************')
        return driver
    except:
        return None


def get_course_snapshot(driver):
    url1 = "https://pagesinterscol.univ-amu.fr/prod/acc_ip.php"

    driver.get(url1)
    time.sleep(1)
    try:
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[1]/form[1]/input').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[1]/form[2]/input').click()
        print("*** WE IN BOYS ***")

        # Continue 1
        driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/p/input').click()

        # Continue 2
        driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/p[2]/input').click()

        driver.find_element(By.XPATH,
                            '/html/body/div[1]/div[4]/form/dl/dd/dl/dd[2]/dl/dd/dl/dt[2]/span/span/a/img').click()

        driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/form/dl/dd/dl/dd[2]/dl/dd/dl/dt[2]/input').click()

        driver.find_element(By.XPATH,
                            '/html/body/div[1]/div[4]/form/dl/dd/dl/dd[2]/dl/dd/dl/dd[1]/dl/dd/dl/dt[1]/input').click()

        #Next step
        driver.find_element(By.XPATH,
                            '/html/body/div[1]/div[4]/form/dl/dd/dl/dd[2]/dl/dd/dl/dd[1]/dl/dd/dl/dt[1]/span/span/a/img').click()

        driver.find_element(By.XPATH,
                            '/html/body/div[1]/div[4]/form/dl/dd/dl/dd[2]/dl/dd/dl/dd[1]/dl/dd/dl/dd[1]/dl/dd/dl/dt[3]/input').click()

        # Continue 3
        driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/p/input').click()
        return driver

    except NoSuchElementException as e:
        return print(e)
