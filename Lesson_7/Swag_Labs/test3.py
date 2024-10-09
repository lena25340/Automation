from Lesson_7.Shopmain import ShopmainPage
from Lesson_7.Shopcontainer import Shopcontainer

def test_shop (driver):
    expected_total = "58.29"

    shopmain = ShopmainPage(driver)
    shopmain.regisration_fieds()
    shopmain.buy_issue()
    shopmain.click_issue()
    shopmain.info_container()

    container = Shopcontainer (driver)
    container.checkout()
    container.info()
    container.price()
    assert expected_total in container.price()
    print (f"Итоговая сумма равна ${container.price()}")