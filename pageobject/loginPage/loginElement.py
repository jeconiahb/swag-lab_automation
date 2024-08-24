from selenium.webdriver.common.by import By

class LoginElement:
    def __init__(self, driver):
        self.driver = driver

    def username_field(self):
        return (By.ID, "user-name")

    def password_field(self):
        return (By.ID, "password")

    def login_button(self):
        return (By.ID, "login-button")

    def error_message(self):
        return (By.XPATH, "//h3[@data-test='error']")
