import time
from selenium import webdriver

def test_one():
    driver=webdriver.Chrome()
    driver.get("https://www.tutorialspoint.com/selenium/practice/webtables.php")
    driver.maximize_window()
    time.sleep(3)
    driver.quit()
def test_two():
    driver=webdriver.Chrome()
    driver.get("https://artoftesting.com/samplesiteforselenium#")
    driver.maximize_window()
    time.sleep(3)
    driver.quit()
def test_three():
    driver=webdriver.Chrome()
    driver.get("https://practice.expandtesting.com/checkboxes")
    driver.maximize_window()
    time.sleep(3)
    driver.quit()
def test_four():
    driver=webdriver.Chrome()
    driver.get("http://www.deadlinkcity.com/")
    driver.maximize_window()
    time.sleep(3)
    driver.quit()










