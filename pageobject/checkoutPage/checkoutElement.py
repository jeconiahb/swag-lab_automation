from selenium.webdriver.common.by import By

class CheckoutElement:
    def __init__(self, driver):
        self.driver = driver

    def first_name_input(self):
        return (By.ID, "first-name")

    def last_name_input(self):
        return (By.ID, "last-name")

    def postal_code_input(self):
        return (By.ID, "postal-code")

    def continue_button(self):
        return (By.ID, "continue")

    def finish_button(self):
        return (By.ID, "finish")
    
    def cancel_button(self):
        return (By.ID, "cancel")

    def success_message(self):
        return (By.CLASS_NAME, "complete-header")

    def error_message(self):
        return (By.XPATH, "//h3[@data-test='error']")