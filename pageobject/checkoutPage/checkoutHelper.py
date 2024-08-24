from pageobject.checkoutPage.checkoutElement import CheckoutElement
from pageobject.cartPage.cartElement import CartElement
from pageobject.helper.verifHelper import is_element_visible
from pageobject.helper.waitHelper import WaitHelper


class CheckoutHelper:

    def __init__(self, driver):
        self.driver = driver
        self.cartElem = CartElement(driver)
        self.coElem = CheckoutElement(driver)

    def clickCheckout(self):
        is_element_visible(self.driver, self.cartElem.btnCheckout())
        button = self.driver.find_element(*self.cartElem.btnCheckout())
        button.click()
        # WaitHelper.wait(2000)

    def typeFirstName(self, first_name):
        is_element_visible(self.driver, self.coElem.first_name_input())
        first_name_input = self.driver.find_element(*self.coElem.first_name_input())
        first_name_input.send_keys(first_name)
        # WaitHelper.wait(2000)

    def typeLastName(self, last_name):
        is_element_visible(self.driver, self.coElem.last_name_input())
        last_name_input = self.driver.find_element(*self.coElem.last_name_input())
        last_name_input.send_keys(last_name)
        # WaitHelper.wait(2000)

    def typePostal(self, postal_code):
        is_element_visible(self.driver, self.coElem.postal_code_input())
        postal_code_input = self.driver.find_element(*self.coElem.postal_code_input())
        postal_code_input.send_keys(postal_code)
        # WaitHelper.wait(2000)

    def clickContinue(self):
        is_element_visible(self.driver, self.coElem.continue_button())
        continue_button = self.driver.find_element(*self.coElem.continue_button())
        continue_button.click()
        # WaitHelper.wait(2000)

    def clickFinish(self):
        is_element_visible(self.driver, self.coElem.finish_button())
        finish_button = self.driver.find_element(*self.coElem.finish_button())
        finish_button.click()
        # WaitHelper.wait(2000)

    def clickCancel(self):
        is_element_visible(self.driver, self.coElem.cancel_button())
        cancel_button = self.driver.find_element(*self.coElem.cancel_button())
        cancel_button.click()
        # WaitHelper.wait(2000)

    def checkout(self, first_name, last_name, postal_code):
        self.clickCheckout()
        self.typeFirstName(first_name)
        self.typeLastName(last_name)
        self.typePostal(postal_code)
        self.clickContinue()
        self.clickFinish()

    def is_transaction_success(self):
        # Menunggu hingga pesan sukses terlihat dan memeriksa keberadaannya
        success_message_locator = self.coElem.success_message()
        try:
            is_element_visible(self.driver, success_message_locator)
            success_message_text = self.driver.find_element(*success_message_locator).text
            print("Success message text:", success_message_text)  # Debugging line
            return "Thank you for your order!" in success_message_text
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def validateError(self):
        is_element_visible(self.driver, self.coElem.error_message())
        error_message_element = self.driver.find_element(*self.coElem.error_message())
        return error_message_element.is_displayed()