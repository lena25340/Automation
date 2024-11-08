from selenium.webdriver.common.by import By
class AuthPage:
    def __init__(self, driver):
        self.browser = driver
        
        self.browser.get("https://fstravel.com/avia")

    def regisration_fieds(self):
        self._name = (By.ID, "email")
        self._pass = (By.ID, "password")
        self._log_button = (By.ID, "login-button")

        self.browser.find_element(*self._name).send_keys("grishina.nat4ly@gmail.con")
        self.browser.find_element(*self._pass).send_keys("UEU9mV8p_")
        self.browser.find_element(*self._log_button).click()
