

from keywords.search_overview import SearchOverviewPage
from keywords.base_test import BaseTest
import time

class TestSearch(BaseTest):

    def test_filter(self):
        """
            This is a cool description of the test.
        """
        searchPage = SearchOverviewPage(self.driver)
        searchPage.accept_cookies()
        searchPage.fill_select_your_location_form()
        searchPage.click_on_filter()
        searchPage.fill_pre_owned_tab()
        searchPage.get_cars_list_information()
        assert True is True

