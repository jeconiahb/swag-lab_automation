from pageobject.cartPage.cartElement import CartElement
from pageobject.helper.verifHelper import is_element_visible
from pageobject.helper.waitHelper import WaitHelper


class CartHelper:
    def __init__(self, driver):
        self.driver = driver
        self.cartElem = CartElement(driver)

    def clickAddtoCart(self, item_name):
        is_element_visible(self.driver, self.cartElem.btnAddCart(item_name))
        button = self.driver.find_element(*self.cartElem.btnAddCart(item_name)) 
        button.click()    
        # WaitHelper.wait(2000)

    def openCart(self):
        icon = self.cartElem.cartIcon()
        is_element_visible(self.driver, icon)
        icon.click()
        # WaitHelper.wait(2000)

    def clickContinueShop(self):
        is_element_visible(self.driver, self.cartElem.btnContinueShop())
        finish_button = self.driver.find_element(*self.cartElem.btnContinueShop())
        finish_button.click()
        # WaitHelper.wait(2000)

    def is_cart_empty(self):
        return "Your cart is empty" in self.driver.page_source

