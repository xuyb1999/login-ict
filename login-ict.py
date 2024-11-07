import time
import os
import getpass
import argparse
import subprocess
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# Create argument parser to get the username and password from command line
parser = argparse.ArgumentParser(description='Login to ICT Gateway')
parser.add_argument('-u', '--user', type=str,
                    help='Specify the username. Defaults to an empty string if not provided.')
parser.add_argument('-p', '--passwd', type=str,
                    help='Specify the password. Defaults to an empty string if not provided.')
args = parser.parse_args()

# Check if our host is already online
try:
    print("[INFO] Test our host's network status ...")
    subprocess.check_output(['ping', '-c', '1', 'www.baidu.com'], timeout=2)
    print("[INFO] Our host is already online. Skip login.")
    exit(0)
except subprocess.TimeoutExpired:
    print("[INFO] Ping timed out. Start to login.")

# Get the real username and password
username = args.user   if args.user   is not None else input("Username: ")
passwd   = args.passwd if args.passwd is not None else getpass.getpass("Password: ")

# Create a Firefox WebDriver instance in headless mode
options = Options()
options.add_argument("--headless")
service = Service(log_path=os.devnull)
driver = webdriver.Firefox(options=options, service=service)

# Open the specified webpage
driver.get('https://gw.ict.ac.cn/index_1.html')

# Find the username input field, password input field, and login button by their IDs
username_input = driver.find_element(By.ID, 'username')
passwd_input   = driver.find_element(By.ID, 'password')
login_btn      = driver.find_element(By.ID, 'login-account')

# Clear the username input field and enter the username
username_input.clear()
username_input.send_keys(username)
# Wait for 0.2 seconds to ensure the input is completed
time.sleep(0.2)

# Clear the password input field and enter the password
passwd_input.clear()
passwd_input.send_keys(passwd)
# Wait for 0.2 seconds to ensure the input is completed
time.sleep(0.2)

# Click the login button
login_btn.click()

# Wait for 0.2 seconds to ensure the page is fully loaded
time.sleep(0.2)
# Print the title of the current page
print(driver.title)

# Test if login is successful
try:
    # When the input passwd is wrong, this element will appear
    content_element = driver.find_element(By.CSS_SELECTOR, "div.component.dialog.confirm.active .content")
    header_element = content_element.find_element(By.CSS_SELECTOR, ".header")
    section_element = content_element.find_element(By.CSS_SELECTOR, ".section")
    print(header_element.text + ": " + section_element.text)
    print("[ERROR] Login failed!")
except NoSuchElementException:
    print("[INFO] Login successful!")

# Close the browser
driver.close()