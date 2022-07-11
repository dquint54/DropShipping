from selenium import webdriver
from Config import *
from Bypass import *
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC






if __name__ == '__main__':

    # driver = webdriver.Chrome(executable_path=CHROME_DRIVER)
    # driver.get("https://www.amazon.com")
    # time.sleep(5)

    Check()



    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "nav-action-inner")))


    driver.quit()



