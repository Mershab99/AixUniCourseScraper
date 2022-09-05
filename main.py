#import requests
#from bs4 import BeautifulSoup
#from requests.exceptions import ConnectionError
from os import environ as env
#from dotenv import load_dotenv
import time
from webcrawler import login, get_course_snapshot

#load_dotenv()

# url = "https://ident.univ-amu.fr/cas/login"

# try:
#    response = requests.get(url)
#    web_content = BeautifulSoup(response.text, "lxml")
# except:
#    pass


if __name__ == '__main__':
    time.sleep(5)
    driver = login(env.get('USER'), env.get('PASS'))
    if driver:
        get_course_snapshot(driver)
