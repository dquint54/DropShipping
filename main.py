from selenium import webdriver
from Config.py import login
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


# CHROME_DRIVER = "/Users/Q/PycharmProjects/chromedriver.exe"



if __name__ == '__main__':

    driver = webdriver.Chrome(executable_path=CHROME_DRIVER)
    driver.get("https://www.amazon.com")




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
