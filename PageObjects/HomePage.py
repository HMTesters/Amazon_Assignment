from selenium.webdriver.common.by import By
from Utilities.reusable_methods import is_element_visible

class Home_Page:

    todays_deal_button_xpath = """//a[contains(text(),"Today's Deals")]"""
    todays_deal_header_xpath = """//h1[contains(text(),"Today's Deals")]"""

    def __init__(self,driver):
        self.driver = driver
        self.driver.implicitly_wait(10)


    def click_on_todays_deal(self):
        todays_deal_button = By.XPATH,self.todays_deal_button_xpath
        assert is_element_visible(self.driver,todays_deal_button)
        self.driver.find_element(By.XPATH,self.todays_deal_button_xpath).click()
        todays_deal_header = By.XPATH,self.todays_deal_header_xpath
        assert is_element_visible(self.driver,todays_deal_header)

