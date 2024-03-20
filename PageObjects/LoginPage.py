from selenium.webdriver.common.by import By
import time


class Login_Page:
    signing_button_on_homepage_xpath = "//span[@id='nav-link-accountList-nav-line-1']"
    email_mobile_phone_number_box_xpath = "//input[@name='email']"
    continue_button_xpath = "//input[@id = 'continue']"
    password_box_xpath = "//input[@name='password']"
    signing_button_xpath = "//input[@id='signInSubmit']"

    def __init__(self, driver):
        self.driver = driver

    def click_on_signin_button_on_homepage(self):
        self.driver.find_element(By.XPATH, self.signing_button_on_homepage_xpath).click()

    def enter_email_address_text(self):
        self.driver.find_element(By.XPATH, self.email_mobile_phone_number_box_xpath).clear()
        time.sleep(10)

    def click_on_continue_button(self):
        self.driver.find_element(By.XPATH, self.continue_button_xpath).click()

    def enter_password_text(self):
        self.driver.find_element(By.XPATH, self.password_box_xpath).clear()
        time.sleep(10)

    def click_on_signing_button(self):
        self.driver.find_element(By.XPATH, self.signing_button_xpath).click()
        time.sleep(10)
        self.driver.save_screenshot('scenario1_Login_Successful.png')
