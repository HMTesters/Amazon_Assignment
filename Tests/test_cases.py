import pytest
from PageObjects.LoginPage import Login_Page
from PageObjects.HomePage import Home_Page
from PageObjects.DealsPage import Deals_Page
from PageObjects.ProductPage import Product_Page
from PageObjects.ProductSelectionPage import ProductSelection_Page


@pytest.mark.usefixtures("setUp")
class Test_Amazon:

    def test_all_scenarios(self):

        obj_LoginPage = Login_Page(self.driver)
        obj_HomePage = Home_Page(self.driver)

        obj_LoginPage.click_on_signing_button()
        obj_LoginPage.enter_email_address_text()
        obj_LoginPage.click_on_continue_button()
        obj_LoginPage.enter_password_text()
        obj_LoginPage.click_on_signin_button_on_homepage()
        obj_HomePage.Header_Footer()
        obj_HomePage.card_details()
        obj_DealPage = Deals_Page(self.driver)

        obj_HomePage.click_on_todays_deal()
        obj_DealPage.sort_discount_filter_by_high_to_low()
        obj_DealPage.click_on_average_rating_4_and_up()
        obj_DealPage.click_on_prime_deals_checkbox_and_verify_is_it_selected()
        obj_DealPage.click_on_deal_of_the_day_deal_type()
        obj_DealPage.capturing_the_cards_only_for_deal_of_the_day()

        obj_ProductPage = Product_Page(self.driver)
        obj_ProductSelectionPage = ProductSelection_Page(self.driver)

        obj_DealPage.click_on_mobile_and_accessories()
        obj_DealPage.sort_discount_filter_by_high_to_low()
        obj_DealPage.click_on_average_rating_4_and_up()
        obj_DealPage.click_on_prime_deals_checkbox_and_verify_is_it_selected()
        obj_DealPage.click_on_deal_of_the_day_deal_type()
        obj_DealPage.click_on_card_with_highest_discount_percentage()
        obj_ProductSelectionPage.sorting_products_based_on_avg_customer_review()
        obj_ProductSelectionPage.clicking_on_product_with_highest_review_count()

        obj_ProductPage.print_product_details()
        obj_ProductPage.add_product_to_cart()

