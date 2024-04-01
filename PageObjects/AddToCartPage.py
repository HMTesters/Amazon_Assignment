import time


class AddToCart_Page:

    def __init__(self,driver):
        self.driver = driver

    def back_to_product_page(self):
        self.driver.back()
        time.sleep(4)



