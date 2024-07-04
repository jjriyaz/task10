import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

driver_paths = r"C:\Users\DELL\Desktop\New folder\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(driver_paths)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Open Instagram profile page
driver.get("https://www.instagram.com/guviofficial/")

try:
    # Wait for the page to load (adjust the time as needed)
    driver.implicitly_wait(10)

    # Extract follower count
    followers_element = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/div[3]/ul/li[2]/div/button/span/span')
    followers_count = followers_element.text
    print("Followers:", followers_count)

    # Extract following count
    following_element = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/div[3]/ul/li[3]/div/button/span/span')
    following_count = following_element.text
    print("Following:", following_count)

finally:
    # Close the browser
    driver.quit()