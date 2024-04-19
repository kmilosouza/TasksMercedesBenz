from keywords.search_overview import SearchOverviewPage
from keywords.base_test import BaseTest

class TestSearch(BaseTest):

    def test_filter(self):
        """
            Mercedes-benz challenge - DevSkiller

            Test Case: TC12345

            Assumptions:
                - System up and running.

            Test Steps:
                - Navigate to https://shop.mercedes-benz.com/en-au/shop/vehicle/srp/demo
                - Accept cookies & Fill Inform your location form
                - Click to filter
                    - filter by colour - select any colour
                - From the results list, find the most expensive vehicle
                - Save Model Year and VIN for the most expensive vehicle to a file
                - Click to enroll a vehicle.
                - Fill e-mail with wrong information.
                - Assert that error message and errors list are displayed properly.

            Teardown:
                - Quit driver.
        """
        searchPage = SearchOverviewPage(self.driver)
        searchPage.accept_cookies()
        searchPage.fill_select_your_location_form()
        searchPage.click_on_filter()
        searchPage.fill_pre_owned_tab()
        searchPage.get_cars_list_information()
        searchPage.fill_out_contact_detail_info()
        error_msg, error_list = searchPage.check_error_message()
        assert (error_msg,error_list), "No error message captured or missing error list."
        
