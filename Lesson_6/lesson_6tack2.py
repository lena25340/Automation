from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 40, 0.1)

driver.get('http://uitestingplayground.com/textinput')

input = driver.find_element(By.CSS_SELECTOR, '#newButtonName')
input.send_keys('SkyPro')
click = driver.find_element(By.CSS_SELECTOR, '#updatingButton').click()
txt = driver.find_element(By.CSS_SELECTOR, '#updatingButton').text
print(txt)

driver.quit