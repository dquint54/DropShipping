from selenium import webdriver
from Bypass import *
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC






if __name__ == '__main__':

    outcome = Check()
    if outcome == True:
        Bypass()
    else:
        print('no bypass needed')




        button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "Sign in securely")))
        button.click()






