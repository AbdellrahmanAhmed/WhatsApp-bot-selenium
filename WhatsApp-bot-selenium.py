import sys
import time
import time
from datetime import date, datetime

from selenium import webdriver
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome('C:\Program Files\Google\Chrome\Application\chromedriver.exe')

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

input("Scan the QR code and then press Enter")

name = input('Enter Target Name!')
target0 = '//span[@title="{}"]'
target = target0.format(name)

today = date.today().strftime('%d/%m/%Y')
current_time = datetime.now().strftime("%H:%M:%S")

msgDate = 'TIME'
msgTime = 'DATE'

message = input("Enter The Message!!")
string = message

x_arg = '//*[@id="pane-side"]/div[1]/div/div/div[6]/div/div/div[2]/div[1]/div[1]/span'

try:
    ##Wait
    # group_title = wait.until(EC.presence_of_element_located((By.XPATH, target)))
    group_title = driver.find_element_by_xpath(target)
    group_title.click()
except NoSuchElementException as se:
    print("Name not in Contact List!")
except Exception as e:
    driver.close()
    print(e)
    sys.exit()

inp_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]'

input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))

for i in range(50):
    input_box.send_keys(string + Keys.SHIFT + Keys.ENTER)
    input_box.send_keys(str(i+1) + Keys.SHIFT + Keys.ENTER)
    input_box.send_keys(Keys.SHIFT + Keys.ENTER)
    input_box.send_keys(current_time)
    input_box.send_keys(Keys.SHIFT + Keys.ENTER)
    input_box.send_keys(today)
    input_box.send_keys(Keys.ENTER)
    time.sleep(0.02)


