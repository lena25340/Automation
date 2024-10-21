from selenium.webdriver.common.by import By

class ShopContainer:
    def __init__(self,browser):
        self.browser = browser 

    def checkout (self):
        self.check = (By.ID,"checkout")
        self.browser.find_element(*self.check).click()
    def info (self):
        self.first_name = (By.ID,"first-name")
        self.browser.find_element(*self.first_name).send_keys("Лена")
        self.last_name = (By.ID,"last-name")
        self.browser.find_element(*self.last_name).send_keys("Гришина ")
        self.postalcode = (By.ID,"postal-code")
        self.browser.find_element(*self.postalcode).send_keys("241020")
        self.continue_button = (By.ID,"continue")      
        self.browser.find_element(*self.continue_button).click() 
    def price(self):
        total_price = self.browser.find_element(By.CSS_SELECTOR,".summary_total_label")
        total = total_price.text.strip().replace("Total: $", "")
        return total
        
      