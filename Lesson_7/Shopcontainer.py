from selenium import webdriver
from selenium.webdriver.common.by import By


def test_shop_form(driver):
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    add_to_cart_buttons = [
        (By.ID, "add-to-cart-sauce-labs-backpack"),
        (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"),
        (By.ID, "add-to-cart-sauce-labs-onesie")
    ]
    for button in add_to_cart_buttons:
        driver.find_element(*button).click()

    driver.find_element(By.ID, "shopping_cart_container").click()
    driver.find_element(By.ID, "checkout").click()

    driver.find_element(By.ID, "first-name").send_keys("Лена")
    driver.find_element(By.ID, "last-name"). send_keys("Гришина ")
    driver.find_element(By.ID, "postal-code"). send_keys("241020")
    driver.find_element(By.ID, "continue").click()

    total_price = driver.find_element(By.CLASS_NAME, "summary_total_label")
    total = total_price.text.strip().replace("Total: $", "")
    expected_total = "58.29"
    assert total == expected_total
    print(f"Итоговая сумма равна $ {total}")

        
        