from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class CalcMain:
    def __init__(self, driver):
       self.driver = driver
       driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def insert_time(self):
        delay_input= self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(45)

    def clicking_buttons(self):
        self.driver .find_element(By.XPATH, "//span[text() = '7']"). click()
        self.driver.find_element(By.XPATH, "//span[text() = '+']"). click()
        self.driver.find_element(By.XPATH, "//span[text() = '8']"). click()
        self.driver.find_element(By.XPATH, "//span[text() = '=']"). click()    

    def wait_button_gettext(self):
        WebDriverWait (self.driver, 46).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))
        return self.driver.find_element(By.CLASS_NAME, "screen").text


    