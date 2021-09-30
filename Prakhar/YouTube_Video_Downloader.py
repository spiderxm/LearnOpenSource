import validators
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


for i in range(1, 50):
    URL = str(input("Enter the URL"))

    valid = validators.url(URL)
    if valid == True:
        print("Searching...")
        break
    else:
        print("Invalid URL")
        continue


driver = webdriver.PhantomJS("C:/Users/Prakhar Pratyush/Desktop/ChromeDriver/phantomjs.exe")
driver.get("http://en.savefrom.net")
driver.find_element_by_id("sf_url").click()
print("Search Box Clicked...")

try:
   element_present = EC.presence_of_element_located((By.ID,"sf_url"))
   WebDriverWait(driver, 20).until(element_present)
   driver.find_element_by_id("sf_url").send_keys(URL)
except TimeoutError:
    print("failed to load page")

try:
   element_present = EC.presence_of_element_located((By.ID,"sf_submit"))
   WebDriverWait(driver, 20).until(element_present)
   driver.find_element_by_id("sf_submit").click()
except TimeoutError:
    print("failed to submit")

try:
    element_present = EC.presence_of_element_located((By.XPATH,'//*[@class="link-group"]/a'))
    WebDriverWait(driver, 20).until(element_present)
    menu_box = driver.find_elements(By.XPATH, '//*[@class="link-group"]/a')

    for i in range(len(menu_box)):
        time.sleep(1)
        print(menu_box[i].get_property("text"))

except TimeoutError:
    print("Options not loaded yet...")
    exit()
#--------------------------------------------------------------------------------------------------------------------------
menu_box = driver.find_elements(By.XPATH, '//*[@class="link-group"]/a')

list = []
for s in range(len(menu_box)):
    durl = menu_box[s].get_property("href")
    list.append(durl)

print("urls assigned")
# --------------------------------------------------------------------------------------------------------------------------

import os
import re
from requests.exceptions import RequestException

path = "C:/Users/Prakhar Pratyush/Desktop"

choice = int(input("Enter Your Choice Number"))

if choice == 1:
    UrL = str(list[0])
    print(UrL)
elif choice == 2:
    UrL = str(list[1])
else:
    UrL = str(list[2])

receive = requests.get(UrL, stream ="true")
print(receive.status_code)
print(receive.headers)
d = receive.headers["Content-Type"]
n = receive.headers["Date"]
try:
    fname = ''
    if "Content-Type" in receive.headers.keys():
        fname = "video" + "." + d[6:]

    else:
        fname = UrL.split("/")[-1]
    file = fname
    with open(os.path.join(path, file), 'wb') as dm:
        # dm.write(receive.content) for pdf
        for chunk in receive.iter_content(chunk_size=1024):
            dm.write(chunk)
except RequestException as e:
    print(e)

