from selenium.webdriver.common.by import By

class Home_Page:

    todays_deal_button_xpath = """//a[contains(text(),"Today's Deals")]"""

    def __init__(self,driver):
        self.driver = driver

    def click_on_todays_deal(self):
        self.driver.find_element(By.XPATH,self.todays_deal_button_xpath).click()
