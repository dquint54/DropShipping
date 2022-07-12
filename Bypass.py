import pyautogui
from Config import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path=CHROME_DRIVER)
driver.get("https://www.amazon.com")

def Check():
    try:
        element = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.CLASS_NAME, 'a-button-text')))
        return True
        print(element.text)
    except StaleElementReferenceException:
        return False


def Bypass():
    try_another_button = pyautogui.locateCenterOnScreen('button.PNG')
    pyautogui.moveTo(try_another_button)
    pyautogui.click()
    return
