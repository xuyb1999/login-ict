import time
import os
import subprocess
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# Check if our host is already offline
try:
    print("[INFO] Test our host's network status ...")
    subprocess.check_output(['ping', '-c', '1', 'www.baidu.com'], timeout=2)
    print("[INFO] Start to logout.")
except subprocess.TimeoutExpired:
    print("[INFO] Our host is already offline. Skip logout.")
    exit(0)

# Create a Firefox WebDriver instance in headless mode
options = Options()
options.add_argument("--headless")
service = Service(log_path=os.devnull)
driver = webdriver.Firefox(options=options, service=service)

# Open the specified webpage
driver.get('https://gw.ict.ac.cn/srun_portal_success?ac_id=1&theme=pro')

# Find the logout button by its ID
logout_btn = driver.find_element(By.ID, 'logout')

# Click the logout button
logout_btn.click()

# Wait for 1 second to ensure the logout is completed
time.sleep(1)

# Click the confirm button in the logout confirmation dialog
try:
    # When we click the previous logout button, this element will appear
    content_element = driver.find_element(By.CSS_SELECTOR, "div.component.dialog.confirm.active .content")
    confirm_btn = content_element.find_element(By.CSS_SELECTOR, ".component.dialog.confirm .btn-confirm")
    confirm_btn.click()
    print("[INFO] Logout successful!")
except NoSuchElementException:
    print("[ERROR] Cannot find the logout confirmation dialog.")

# Close the WebDriver instance
driver.close()