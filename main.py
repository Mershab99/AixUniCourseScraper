from os import environ as env
import time
from webcrawler import login, get_course_snapshot
from discord import send_message

first = True

content = ""
if __name__ == '__main__':
    time.sleep(5)
    driver = login(env.get('USER'), env.get('PASS'))
    driver = get_course_snapshot(driver)

    while True:
        if driver:
            driver.refresh()
            prev_content = content
            new_content = driver.page_source
            if not first and content == new_content:
                content = new_content
                print('UPDATE DISCORD NOTIFICATION')
                send_message('<@758424249832046612> A new change has been made to the course website, '
                                                                 'check it out here: '
                                                                 'https://pagesinterscol.univ-amu.fr/prod/acc_ip.php')
            if first:
                send_message('<@758424249832046612> The course crawler bot is now active')
                first = False

            time.sleep(10)
