import time

from selenium.webdriver.common.by import By


class ProductSelection_Page:

    all_products_xpath = "//div[contains(@class,'a-section octopus-dlp-asin-title')]/a"
    dropdown_button_xpath = "//span[contains(@class,'a-button-text a-declarative')]"
    review_count_element_xpath = "//li[contains(@class,'no-margin-right')]//div[contains(@class,'a-row')]//span[contains(@class,'a-size-small a-color-tertiary')]"
    dropdown_option_to_select_xpath = 'Avg. Customer Review'
    find_items_prices_xpath = "//span[@class='a-price-whole']"
    sort_option_xpath = 'Price: Low to High'
    sort_items_text_xpath = "//div[contains(@class,'a-section octopus-dlp-asin-title')]//a"
    prices_list = []
    



    def __init__(self,driver):
        self.driver = driver

    def sorting_products_based_on_avg_customer_review(self):
        self.driver.find_element(By.XPATH, self.dropdown_button_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, self.dropdown_option_to_select_xpath).click()
        time.sleep(5)

    def clicking_on_product_with_highest_review_count(self):
        review_count = self.driver.find_elements(By.XPATH,self.review_count_element_xpath)
        time.sleep(3)
        review_list = []
        for review in review_count:
            review_list.append(int((review.text).replace(",","")))

        all_products = self.driver.find_elements(By.XPATH,self.all_products_xpath)

        all_products[review_list.index(max(review_list))].click()


    def sort_items_lowest_price(self):
        self.driver.find_element(By.XPATH, self.dropdown_button_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, self.sort_option_xpath).click()
        time.sleep(5)
        prices = self.driver.find_elements(By.XPATH, self.find_items_prices_xpath)
        time.sleep(4)
        for x in prices:
            self.prices_list.append(int(x.text))
        self.sort_items_text = self.driver.find_elements(By.XPATH, self.sort_items_text_xpath)
        self.sort_items_text[self.prices_list.index(min(self.prices_list))].click()
        time.sleep(5)

