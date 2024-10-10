class AuthPage:
    def __init__(self, driver):
        self.browser = driver
        
        self.browser.get("https://www.saucedemo.com")

    def login(self):
        self._name = (By.ID, "user-name")
        self._pass = (By.ID, "password")
        self._log_button = (By.ID, "login-button")

        self.browser.find_element(*self._name).send_keys("standard_user")
        self.browser.find_element(*self._pass).send_keys("secret_sauce")
        self.browser.find_element(*self._log_button).click()