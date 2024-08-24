import unittest
from selenium import webdriver
from pageobject.loginPage.loginHelper import LoginHelper
from pageobject.loginPage.loginConstant import LoginConstant

class LoginTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(LoginConstant.BASE_URL)
        self.driver.maximize_window()
        self.login_helper = LoginHelper(self.driver)


    def tearDown(self):
        self.driver.quit()

    # Positive Login Test Cases
    def test_login_positive_standard_user(self):
        self.login_helper.login(LoginConstant.STANDARD_USER, LoginConstant.PASSWORD)
        self.assertTrue(self.login_helper.is_logged_in())

    def test_login_positive_problem_user(self):
        self.login_helper.login(LoginConstant.PROBLEM_USER, LoginConstant.PASSWORD)
        self.assertTrue(self.login_helper.is_logged_in())

    def test_login_positive_performance_glitch_user(self):
        self.login_helper.login(LoginConstant.PERFORMANCE_GLITCH_USER, LoginConstant.PASSWORD)
        self.assertTrue(self.login_helper.is_logged_in())
    
    # Negative Login Test Cases
    def test_login_negative_invalid_username(self):
        self.login_helper.login(LoginConstant.INVALID_USER, LoginConstant.PASSWORD)
        self.assertTrue(self.login_helper.is_login_failed())

    def test_login_negative_invalid_password(self):
        self.login_helper.login(LoginConstant.STANDARD_USER, LoginConstant.INVALID_PASSWORD)
        self.assertTrue(self.login_helper.is_login_failed())

    def test_login_negative_empty_username(self):
        self.login_helper.login("", LoginConstant.PASSWORD)
        self.assertTrue(self.login_helper.is_login_failed())

    def test_login_negative_empty_password(self):
        self.login_helper.login(LoginConstant.STANDARD_USER, "")
        self.assertTrue(self.login_helper.is_login_failed())

    def test_login_negative_empty_credentials(self):
        self.login_helper.clickBtnLogin()
        self.assertTrue(self.login_helper.is_login_failed())

    def test_login_case_insensitive(self):
        self.login_helper.login("STANDARD_USER", "SECRET_sAUCE")
        self.assertTrue(self.login_helper.is_login_failed())

    # Boundary Login Test Cases
    def test_login_username_long(self):
        self.login_helper.login("u" * 100, "secret_sauce")
        self.assertTrue(self.login_helper.is_login_failed(), "Error message should be displayed for long username")

    def test_login_password_long(self):
        self.login_helper.login("standard_user", "p" * 100)
        self.assertTrue(self.login_helper.is_login_failed(), "Error message should be displayed for long password")

    def test_login_username_password_short(self):
        self.login_helper.login("u", "p")
        self.assertTrue(self.login_helper.is_login_failed(), "Error message should be displayed for short username and password")

if __name__ == "__main__":
    unittest.main()
