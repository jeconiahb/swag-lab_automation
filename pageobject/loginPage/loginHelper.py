from pageobject.loginPage.loginElement import LoginElement
from pageobject.helper.verifHelper import is_element_visible
from pageobject.helper.waitHelper import WaitHelper

class LoginHelper:

    def __init__(self, driver):
        self.driver = driver
        self.login_element = LoginElement(driver)  

    def typeUserName(self, username):
        is_element_visible(self.driver, self.login_element.username_field())
        username_field = self.driver.find_element(*self.login_element.username_field())  # Temukan elemen
        username_field.send_keys(username)  
        # WaitHelper.wait(2000)

    def typePassword(self, password):
        is_element_visible(self.driver, self.login_element.password_field())
        password_field = self.driver.find_element(*self.login_element.password_field())  # Temukan elemen
        password_field.send_keys(password)  
        # WaitHelper.wait(2000)

    def clickBtnLogin(self):
        is_element_visible(self.driver, self.login_element.login_button())
        login_button = self.driver.find_element(*self.login_element.login_button())  # Temukan elemen
        login_button.click()  
        # WaitHelper.wait(2000)

    def login(self, username, password):
        self.typeUserName(username)
        self.typePassword(password)
        self.clickBtnLogin()
        

    def is_logged_in(self):
        return "inventory.html" in self.driver.current_url

    def is_login_failed(self):
        return self.driver.find_element(*self.login_element.error_message()).is_displayed()
