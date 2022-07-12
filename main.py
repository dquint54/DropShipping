from Bypass import *
from selenium.webdriver.common.by import By

if __name__ == '__main__':


    if Check():
        Bypass()
    else:
        print("No Bypass needed")





    button = driver.find_element(By.CSS_SELECTOR, 'Sign in securely')
    button.click()


driver.quit()





