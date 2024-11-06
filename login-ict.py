import time
import os
import getpass
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

username = input("Username: ")
passwd   = getpass.getpass("Password: ")

options = Options()
options.add_argument("--headless")

bro = webdriver.Firefox(options=options, service_log_path=os.devnull)
bro.get('https://gw.ict.ac.cn/index_1.html')

username_input = bro.find_element(By.ID, 'username')
passwd_input   = bro.find_element(By.ID, 'password')
login_btn      = bro.find_element(By.ID, 'login-account')

username_input.clear()
username_input.send_keys(username)
time.sleep(0.2)

passwd_input.clear()
passwd_input.send_keys(passwd)
time.sleep(0.2)

login_btn.click()

time.sleep(0.2)
print(bro.get_cookies())

time.sleep(0.2)
print(bro.title)

bro.close()
