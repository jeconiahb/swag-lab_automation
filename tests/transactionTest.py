import unittest
import time
from selenium import webdriver
from pageobject.loginPage.loginHelper import LoginHelper
from pageobject.loginPage.loginConstant import LoginConstant
from pageobject.cartPage.cartHelper import CartHelper
from pageobject.checkoutPage.checkoutHelper import CheckoutHelper

class TransactionTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(LoginConstant.BASE_URL)
        self.driver.maximize_window()
        self.login_helper = LoginHelper(self.driver)
        self.cart_helper = CartHelper(self.driver)
        self.checkout_helper = CheckoutHelper(self.driver)
        # Pre-login with standard user
        self.login_helper.login(LoginConstant.STANDARD_USER, LoginConstant.PASSWORD)

    def tearDown(self):
        self.driver.quit()

    # Positive Transaction Test Cases
    def test_transaction_single_item(self):
        self.cart_helper.clickAddtoCart("Sauce Labs Backpack")
        self.cart_helper.openCart()
        self.checkout_helper.checkout("John", "Doe", "12345")
        self.assertTrue(self.checkout_helper.is_transaction_success())

    def test_transaction_multiple_items(self):
        self.cart_helper.clickAddtoCart("Sauce Labs Backpack")
        self.cart_helper.clickAddtoCart("Sauce Labs Bike Light")
        self.cart_helper.openCart()
        self.checkout_helper.checkout("John", "Doe", "12345")
        self.assertTrue(self.checkout_helper.is_transaction_success())

    def test_navigate_to_cart_without_adding_items(self):
        self.cart_helper.openCart()  
        self.cart_helper.clickContinueShop()  
        self.assertTrue(self.login_helper.is_logged_in())

    # Negative Transaction Test Cases

    def test_transaction_incomplete_checkout_info(self):
        self.cart_helper.clickAddtoCart("Sauce Labs Backpack")
        self.cart_helper.openCart()
        self.checkout_helper.clickCheckout()
        self.checkout_helper.typeFirstName("John")
        self.checkout_helper.clickContinue() # Skip last name and postal code
        self.assertTrue(self.checkout_helper.validateError())
        
    def test_transaction_no_items_in_cart(self):
        self.cart_helper.openCart()
        self.assertTrue(self.cart_helper.is_cart_empty())

    def test_cancel_transaction_during_checkout(self):
        self.cart_helper.clickAddtoCart("Sauce Labs Backpack")
        self.cart_helper.openCart()
        self.checkout_helper.checkout("John", "Doe", "12345")
        self.checkout_helper.clickCancel()   
        self.assertTrue(self.login_helper.is_logged_in())

    # Boundary Transaction Test Cases
    def test_checkout_first_last_name_long(self):
        self.cart_helper.openCart()
        self.checkout_helper.checkout("FirstName" * 10, "LastName" * 10, "12345")
        self.assertTrue(self.checkout_helper.validateError())

    def test_checkout_zip_code_long(self):
        self.cart_helper.openCart()
        self.checkout_helper.checkout("ValidFirstName", "ValidLastName", "1234567890")
        self.assertTrue(self.checkout_helper.validateError())

    def test_checkout_first_last_name_empty(self):
        self.cart_helper.openCart()
        self.checkout_helper.checkout("", "", "12345")
        self.assertTrue(self.checkout_helper.validateError())

if __name__ == "__main__":
    unittest.main()
