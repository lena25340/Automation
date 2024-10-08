from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    def find_fields(self):
        self._first_name = (By.NAME, "first-name")
        self._last_name = (By.NAME, "last-name")
        self._address = (By.NAME, "address")
        self._email = (By.NAME, "e-mail")
        self._phone = (By.NAME, "phone")
        self._zip_code = (By.NAME, "zip-code")
        self._city = (By.NAME, "city")
        self._country = (By.NAME, "country")
        self._job_position = (By.NAME, "job-position")
        self._company = (By.NAME, "company")
        self._button = (By.TAG_NAME, "button")

    def filling_in_the_field (self):
        self.driver.find_element(*self._first_name).send_keys("Иван")
        self.driver.find_element(*self._last_name).send_keys("Петров")
        self.driver.find_element(*self._address).send_keys("Ленина, 55-3")
        self.driver.find_element(*self._email).send_keys("test@skypro.com")
        self.driver.find_element(*self._phone).send_keys("+7985899998787")
        self.driver.find_element(*self._zip_code).send_keys("")
        self.driver.find_element(*self._city).send_keys("Москва")
        self.driver.find_element(*self._country).send_keys ("Россия")
        self.driver.find_element(*self._job_position).send_keys("QA")
        self.driver.find_element(*self._company).send_keys("SkyPro")

    def click_submit_button(self):
        while True:
            self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
            try:
                WebDriverWait(self.driver, 40, 0.1).until(EC.element_to_be_clickable(self._button)).click()
                break
            except:
                pass