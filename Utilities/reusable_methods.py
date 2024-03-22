from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def is_element_visible(driver,locator):
    try:
        element = WebDriverWait(driver,10).until(EC.visibility_of_element_located(locator))
        return bool(element)
    except Exception as Error:
        print(Error)

