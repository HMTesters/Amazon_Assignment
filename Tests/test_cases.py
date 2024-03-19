import pytest
from PageObjects.HomePage import Home_Page
from PageObjects.DealsPage import Deals_Page

@pytest.mark.usefixtures("setUp")
class Test_Amazon:

    def test_all_scenarios(self):

        obj_HomePage = Home_Page(self.driver)
        obj_DealPage = Deals_Page(self.driver)

        obj_HomePage.click_on_todays_deal()
        obj_DealPage.sort_discount_filter_by_high_to_low()
        obj_DealPage.click_on_average_rating_4_and_up()
        obj_DealPage.click_on_prime_deals_checkbox_and_verify_is_it_selected()
        obj_DealPage.click_on_deal_of_the_day_deal_type()
        obj_DealPage.capturing_the_cards_only_for_deal_of_the_day()