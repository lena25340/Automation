from Shopmain import ShopmainPage
from Shopcontainer import ShopContainer
from Lesson_7.Swag_Labs.AuthPage import AuthPage
import pytest


def test_shop(driver):
    authpage= AuthPage(driver)
    authpage.regisration_fieds()
    shopmain = ShopmainPage(driver)
    shopmain.buy_issue()
    shopmain.click_issue()
    shopmain.info_container()

    container = ShopContainer (driver)
    container.checkout()
    container.info()
    container.price()

    print (f"Итоговая сумма равна ${container.price()}")
    expected_total = "58.29"
    assert expected_total in container.price()