from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def is_element_visible(driver, locator, should_be_visible=True, timeout=10):
    """
    Memeriksa apakah elemen terlihat atau tidak terlihat di halaman.

    Args:
    driver: WebDriver instance
    locator: Tuple yang berisi strategi pencarian (By.LOCATOR_TYPE) dan nilai locator ('locator_value')
    should_be_visible: Apakah elemen harus terlihat (True) atau tidak terlihat (False)
    timeout: Waktu tunggu maksimum dalam detik (default: 10)

    Returns:
    True jika elemen sesuai dengan kriteria visibilitas, False jika tidak
    """
    wait = WebDriverWait(driver, timeout)
    
    if should_be_visible:
        try:
            # Menunggu hingga elemen terlihat
            wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False
    else:
        try:
            # Menunggu hingga elemen tidak terlihat
            wait.until(EC.invisibility_of_element_located(locator))
            return True
        except:
            return False
