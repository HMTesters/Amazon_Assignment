from selenium.webdriver.common.by import By
import time

class Home_Page:

    header_xpath = "//div[@id='nav-main']"
    footer_xpath = "//div[@id='navFooter']"
    card_list_header_xpath = "//div[@class = 'a-cardui-header']"
    card_list_footer_xpath = "//div[@class='a-cardui-footer']/a"
    todays_deal_button_xpath = """//a[contains(text(),"Today's Deals")]"""

    def __init__(self,driver):
        self.driver = driver

    def Header_Footer(self):
        print(self.driver.find_element(By.XPATH, self.header_xpath).text)
        time.sleep(2)
        self.driver.save_screenshot("scenario1_Header.png")
        self.driver.execute_script("window.scrollBy(0,6000)", "")
        print(self.driver.find_element(By.XPATH, self.footer_xpath).text)
        time.sleep(2)
        self.driver.save_screenshot("scenario1_Footer.png")

    def card_details(self):
        card_header_keys = self.driver.find_elements(By.XPATH, self.card_list_header_xpath)
        card_footer_values = self.driver.find_elements(By.XPATH, self.card_list_footer_xpath)
        card_header_footer = {k.text: v.get_attribute('href') for k, v in zip(card_header_keys, card_footer_values)}
        print(card_header_footer)
        self.driver.save_screenshot("scenario1_Card_header_Footer.png")
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,-6000)", "")

    def click_on_todays_deal(self):
        self.driver.find_element(By.XPATH,self.todays_deal_button_xpath).click()
