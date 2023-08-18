from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import random

sleep_timers = [2, 4, 6]

URL = 'https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&' \
      'location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0'

chrome_driver_path = 'E:\Development\chromedriver.exe'
ser = Service(chrome_driver_path)

driver = webdriver.Chrome(service=ser)
driver.get(url=URL)

sign_href = driver.find_element(By.CSS_SELECTOR, ".btn-secondary-emphasis")
sign_href.click()

time.sleep(random.choice(sleep_timers))
input_pass = driver.find_element(By.CSS_SELECTOR, "#password")
input_pass.send_keys("mlYS@2004")

time.sleep(random.choice(sleep_timers))
input_mail = driver.find_element(By.CSS_SELECTOR, "#username")
input_mail.send_keys("8singhutkarsh8@gmail.com")

time.sleep(random.choice(sleep_timers))
sign_button = driver.find_element(By.CSS_SELECTOR, ".from__button--floating")
sign_button.click()

# time.sleep(30)
# pref_location = driver.find_element(By.CSS_SELECTOR, 'jobs-search-box__text-input')
#
# for i in range(0, 35):
#     pref_location.send_keys(Keys.BACKSPACE)
#
# pref_location.send_keys("India")
# pref_location.send_keys(Keys.ENTER)
# time.sleep(10)
# final_search = driver.find_element(By.XPATH, '//*[@id="global-nav-search"]/div/div[2]/button[1]')
# final_search.click()

# time.sleep(30)
# easy_apply = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[4]/div/div/main/div/section[2]/div/div[2]/'
#                                            'div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/div/div/button/span')
# easy_apply.click()

# time.sleep(20)
# next_click = driver.find_element(By.CSS_SELECTOR, '.artdeco-button__text')
# next_click.click()
#
# time.sleep(20)
# choose = driver.find_element(By.XPATH, '//*[@id="ember498"]')
#
# time.sleep(20)
# next_click1 = driver.find_element(By.XPATH, '//*[@id="ember480"]')

time.sleep(20)
companies = driver.find_elements(By.XPATH, '/html/body/div[5]/div[3]/div[4]/div/div/main/div/section[1]/div/ul/li')

for job in companies:
    print("selected")
    job.click()
    time.sleep(4)

    try:
        easy_apply = driver.find_element(By.CSS_SELECTOR, '.jobs-apply-button--top-card button')
        easy_apply.click()
        time.sleep(5)

        check_button = driver.find_element(By.CSS_SELECTOR, '.artdeco-button--primary span')

        if check_button.text != "Next":
            choose_resume = driver.find_element(By.CSS_SELECTOR, '[aria-label="Choose Resume"]')
            choose_resume.click()
            time.sleep(4)

            submit = driver.find_element(By.CSS_SELECTOR, '.artdeco-button--primary')
            submit.click()
            print("You applied to a Job.")
            time.sleep(5)

            close_button = driver.find_element(By.CSS_SELECTOR, '.artdeco-modal__dismiss')
            close_button.click()
            time.sleep(4)
            continue
        else:
            print("Job skipped, had too many steps.")
            close = driver.find_element(By.CSS_SELECTOR, '.artdeco-modal__dismiss')
            close.click()
            time.sleep(4)

            discard_button = driver.find_element(By.CSS_SELECTOR, '.artdeco-modal__confirm-dialog-btn')
            discard_button.click()
            time.sleep(4)

    except NoSuchElementException:
        print("Job skipped, no application button")
        continue

time.sleep(10*100)
driver.quit()
