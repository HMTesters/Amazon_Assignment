from selenium.webdriver.common.by import By
import time
from Utilities import data

from selenium.webdriver.support.ui import Select
from Utilities.reusable_methods import is_element_visible

class Product_Page:
    product_title_xpath = "//span[contains(@id,'productTitle')]"
    star_rating_of_the_product_xpath = "//div[contains(@id,'averageCustomerReviews_feature_div')]//div//span//span[contains(@id,'acrPopover')]"
    number_of_reviews_of_the_product_xpath = "//div[contains(@id,'averageCustomerReviews_feature_div')]//div//span/following-sibling::span[contains(@class,'a-declarative')]//a//span"
    price_of_the_product_xpath = "//span[contains(@class,'priceToPay')]//span//span/following-sibling::span"
    replacement_policy_xpath = "//li[@class='a-carousel-card tw-scroll-carousel-element']/div[@id='RETURNS_POLICY']//div/following-sibling::div//span"
    add_product_to_cart_xpath = "//span[contains(@id,'submit.add-to-cart')][contains(@class,'a-spacing-small')]"
    selecting_quantity_one_xpath = "//select[@name='quantity']//option[@value='1']"
    selecting_quantity_two_xpath = "//select[@name='quantity']//option[@value='2']"
    dropdown_button_for_quantity_xpath = "//select[contains(@id,'quantity')]"
    free_delivery_xpath = "//div[@id='mir-layout-DELIVERY_BLOCK']//a[contains(text(),'FREE delivery')]"
    click_dropdown_xpath = "//select[@name='quantity']"
    select_quantity_xpath = "//select[@name='quantity']/option[@value='2']"


    def __init__(self,driver):
        self.driver = driver

    def print_product_details(self):
        product_title = self.driver.find_element(By.XPATH, self.product_title_xpath).text
        star_rating_of_the_product = self.driver.find_element(By.XPATH, self.star_rating_of_the_product_xpath).text
        number_of_reviews_of_the_product = self.driver.find_element(By.XPATH, self.number_of_reviews_of_the_product_xpath).text
        price_of_the_product = self.driver.find_element(By.XPATH, self.price_of_the_product_xpath).text
        print("Title of the product is: " + product_title)
        print("Star rating of the product is: " + star_rating_of_the_product)
        print("Total number of reviews of the product is: " + number_of_reviews_of_the_product)
        print("Price of the product is: " + price_of_the_product)

    def add_product_to_cart(self):

        return_replacement_info = (self.driver.find_element(By.XPATH, self.replacement_policy_xpath)).text
        dropdown_button = self.driver.find_element(By.XPATH,self.dropdown_button_for_quantity_xpath)
        quantity = Select(dropdown_button)
        if "Return" or "Replacement" in return_replacement_info:
            quantity.select_by_value("2")
        else:
            quantity.select_by_value("1")


        add_to_card_button = self.driver.find_element(By.XPATH, self.add_product_to_cart_xpath)
        add_to_card_button.click()
        time.sleep(5)

    def back_to_productSelection_page(self):
        self.driver.back()


    def check_eligibleFor_free_delivery_option(self):
        text = (self.driver.find_element(By.XPATH, self.free_delivery_xpath)).text
        if text == data.expected_free_delivery_text:
            self.click_dropdown_and_select_quantity()

        # assert data.actual_free_delivery_text==data.expected_free_delivery_text
        free_delivery_text = By.XPATH, self.free_delivery_xpath
        assert is_element_visible(self.driver,free_delivery_text)


    def click_dropdown_and_select_quantity(self):
        dropdown = self.driver.find_element(By.XPATH, self.click_dropdown_xpath)
        time.sleep(2)
        discount_options = Select(dropdown)
        discount_options.select_by_value(data.select_quantity)
        time.sleep(2)
        quantity=By.XPATH,self.select_quantity_xpath


        assert quantity==data.select_quantity

    def add_to_cart(self):
        self.driver.find_element(By.XPATH, self.add_product_to_cart_xpath).click()
        time.sleep(4)

