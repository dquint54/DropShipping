from selenium import webdriver
from Bypass import *
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC






if __name__ == '__main__':


    if Check():
        Bypass()
    else:
        print("No Bypass needed")





    button = driver.find_element(By.CSS_SELECTOR, 'Sign in securely')
    button.click()


driver.quit()





