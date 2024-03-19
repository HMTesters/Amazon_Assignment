from selenium.webdriver.common.by import By
from Utilities.reusable_methods import is_element_visible,use_implicit_wait

class Home_Page:

    todays_deal_button_xpath = """//a[contains(text(),"Today's Deals")]"""
    todays_deal_header_xpath = """//h1[contains(text(),"Today's Deals")]"""

    def __init__(self,driver):
        self.driver = driver
        use_implicit_wait(self.driver,10)


    def click_on_todays_deal(self):
        self.driver.find_element(By.XPATH,self.todays_deal_button_xpath).click()
        todays_deal_header = By.XPATH,self.todays_deal_header_xpath
        assert is_element_visible(self.driver,todays_deal_header)

