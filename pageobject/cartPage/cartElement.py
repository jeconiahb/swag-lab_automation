from selenium.webdriver.common.by import By

class CartElement:
    def __init__(self, driver):
        self.driver = driver

    def btnAddCart(self, item_name):
        return (By.XPATH, f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button")
    
    def cartIcon(self):
        return self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")

    def btnCheckout(self):
        return (By.ID, "checkout")

    def btnContinueShop(self):
        return (By.ID, "continue-shopping")