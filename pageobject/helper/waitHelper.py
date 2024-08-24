import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class WaitHelper:
    @staticmethod
    def wait(milliseconds: int = 1000):
        """
        Tunggu selama sejumlah milidetik.

        Args:
        milliseconds: Waktu tunggu dalam milidetik (default: 1000 ms)
        """
        time.sleep(milliseconds / 1000.0)  # Mengonversi milidetik ke detik

    def wait_for_element(driver, locator, timeout=10):
        if not isinstance(locator, tuple) or len(locator) != 2:
            raise ValueError("Locator harus berupa tuple dengan dua elemen: (By.LOCATOR_TYPE, 'locator_value')")

        wait = WebDriverWait(driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))