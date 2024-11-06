import time
import os
import getpass
import argparse
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

# Create argument parser to get the username and password from command line
parser = argparse.ArgumentParser(description='Login to ICT Gateway')
parser.add_argument('-u', '--user', type=str,
                    help='Specify the username. Defaults to an empty string if not provided.')
parser.add_argument('-p', '--passwd', type=str,
                    help='Specify the password. Defaults to an empty string if not provided.')
args = parser.parse_args()

# Get the real username and password
username = args.user   if args.user   is not None else input("Username: ")
passwd   = args.passwd if args.passwd is not None else getpass.getpass("Password: ")

# Set up Firefox browser options to run in headless mode (i.e., without displaying the browser interface)
options = Options()
options.add_argument("--headless")

# Create a Firefox WebDriver instance in headless mode
bro = webdriver.Firefox(options=options, service_log_path=os.devnull)

# Open the specified webpage
bro.get('https://gw.ict.ac.cn/index_1.html')

# Find the username input field, password input field, and login button by their IDs
username_input = bro.find_element(By.ID, 'username')
passwd_input   = bro.find_element(By.ID, 'password')
login_btn      = bro.find_element(By.ID, 'login-account')

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

# Wait for 0.2 seconds to ensure the login operation is completed
time.sleep(0.2)
# Print the cookies of the current page
print(bro.get_cookies())

# Wait for 0.2 seconds to ensure the page is fully loaded
time.sleep(0.2)
# Print the title of the current page
print(bro.title)

# Close the browser
bro.close()