from selenium import webdriver
from selenium.webdriver.common.by import By


def test_webpage():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/index.php?route=common/home")
    actual_title=driver.title
    expected="Your Store"
    assert actual_title==expected
    driver.find_element(By.NAME,'search').send_keys("HP")
    driver.find_element(By.XPATH,'(//button)[5]').click()
    assert driver.find_element(By.LINK_TEXT,'HP LP3065').is_displayed()