from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

def test_calculator_form (driwer):
    driwer = webdriver.Chrome()
    driwer.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    delay_input= driwer.find_element(By.ID, "delay")
    delay_input.clear()
    delay_input.send_keys()

    driwer.find_element(By.XPATH, "//span[text() = '7']"). click()
    driwer.find_element(By.XPATH, "//span[text() = '+']"). click()
    driwer.find_element(By.XPATH, "//span[text() = '8']"). click()
    driwer.find_element(By.XPATH, "//span[text() = '=']"). click()
    
    result_text= WebDriverWait (driwer, 46).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))
    result_text= driwer.find_element(By.CLASS_NAME, "screen").text

    assert result_text == "15"