from Lesson_7.Shopmain import ShopmainPage
from Lesson_7.Shopcontainer import Shopcontainer


     def regisration_fieds(self):
        self._name = (By.ID, "user-name")
        self._pass = (By.ID, "password")
        self._log_button = (By.ID, "login-button")
        

        self.browser.find_element(*self._name).send_keys("standard_user")
        self.browser.find_element(*self._pass).send_keys("secret_sauce")
        self.browser.find_element(*self._log_button).click()

    shopmain = ShopmainPage(driver)
    shopmain.regisration_fieds()
    shopmain.buy_issue()
    shopmain.click_issue()
    shopmain.info_container()

    container = ShopContainer (driver)
    container.checkout()
    container.info()
    container.price()
    assert expected_total in container.price()
    print (f"Итоговая сумма равна ${container.price()}")
    expected_total = "58.29"