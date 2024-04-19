from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import Select

class SearchOverviewPage:

    def __init__(self, driver):
        self.driver = driver

    def accept_cookies(self):
        '''
            This method only clicks to accept cookies.
        '''
        invisible = WebDriverWait(self.driver, 20).until(
                EC.invisibility_of_element_located (
                    (By.XPATH,"//div[@class='dcp-loader dcp-loader--hide']")
                )
            )
        if invisible != True:
            self.driver.execute_script("document.getElementsByClassName('dcp-loader')[0].remove()")
            invisible = WebDriverWait(self.driver, 10).until(
                    EC.invisibility_of_element_located (
                        (By.XPATH,"//div[@class='dcp-loader dcp-loader--hide']")
                    )
            )
        if invisible:
            shadow_root = self.driver.find_element(
                By.CSS_SELECTOR, '[settings-id="Kvbnw4-6_"]'
            ).shadow_root
            second_shadow_root = shadow_root.find_element(
                By.CSS_SELECTOR, '[data-test="handle-accept-all-button"]'
            ).shadow_root   
            accept_button = second_shadow_root.find_element(
                By.CLASS_NAME, "button"
            )
            action = ActionChains(self.driver)
  
            # click the item
            action.move_to_element(accept_button).click().perform()
            

        
    def fill_select_your_location_form(self):
        '''
            This is only to fill the initial form.
        
        '''
        element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located (
                    (By.XPATH,"//label[normalize-space()='* Your state']//following::select[1]")
                )
            )
        element.click()
        
        field1 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//option[normalize-space()='New South Wales']")
            )
        )
        field1.click()

        field2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '[aria-labelledby="postal-code-hint"]')
            )
        )
        field2.send_keys("2831")
        
        field3 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Private']")
            )
        )
        field3.click()

        continue_btn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Continue']")
            )
        )
        continue_btn.click()

    def click_on_filter(self):
        invisible = WebDriverWait(self.driver, 20).until(
                    EC.invisibility_of_element_located (
                        (By.XPATH, "//button[contains(@data-test-id,'state-selected-modal__close')]")
                    )
            )
        if invisible:
            filter = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located(
                    (By.XPATH,"//div[@class='sidebar']//span[@class='filter-toggle']")
                )
            )
            filter.click()

    def fill_pre_owned_tab(self):
        self.click_pre_owned()
        self.fill_colour()

    def click_pre_owned(self):
        element = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located(
                    (By.XPATH,"//span[normalize-space()='Pre-Owned']")
                )
            )
        element.click()

        invisible = WebDriverWait(self.driver, 20).until(
                EC.invisibility_of_element_located (
                    (By.XPATH,"//div[@class='dcp-loader dcp-loader--hide']")
                )
            )
        if invisible != True:
            self.driver.execute_script("document.getElementsByClassName('dcp-loader')[0].remove()")


    def fill_colour(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        attempt = 0
        while attempt < 3:
            visible = WebDriverWait(self.driver, 20).until(
                    EC.visibility_of_element_located (
                        (By.XPATH,"//div[contains(@class,'dcp-cars-filter-widget')]/div[contains(@class,'fab-filter')]//following::p[text()='Colour']")
                    )
            )
            if visible != False:
                colour = WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located(
                    (By.XPATH,"//div[contains(@class,'dcp-cars-filter-widget')]/div[contains(@class,'fab-filter')]//following::p[text()='Colour']")
                    )
                )
                action = ActionChains(self.driver)
                action.move_to_element(colour).click().perform()
                break
            attempt+=1

        
        colour_dropdown = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH,"//span[normalize-space()='Colour']")
            )
        )
        colour_dropdown.click()
        
        
        colour = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
            (By.XPATH,"//a[normalize-space()='BRILLANTBLUE metallic']")
            )
        )
        colour.click()
            
    def get_cars_list_information(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollTop);")
        invisible = WebDriverWait(self.driver, 20).until(
                EC.invisibility_of_element_located (
                    (By.XPATH,"//div[@class='dcp-loader dcp-loader--hide']")
                )
            )
        if invisible:
            result_list = self.driver.find_elements(
                By.XPATH, "//div[@class='dcp-cars-srp__results dcp-cars-srp-results']"
            )
            for car in result_list:
                details = car.text
                car_price = details.split("\n")

            final_car_price_list = []
            for price in car_price:
                if price.startswith("A$"):
                    aux_price = price.split("$")[1].replace(",",".")
                    final_car_price_list.append(float(aux_price[0:5]))
            
            most_expensive = max(final_car_price_list)
            index = final_car_price_list.index(most_expensive)
            
            details_most_expensive = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located (
                    (By.XPATH,"//div[@class='dcp-cars-srp-results__tile'][{}]".format(index+1))
                )
            )
            details_most_expensive.click()

            details_list = self.driver.find_elements(
                By.XPATH, "//ul[@class='dcp-vehicle-details-category__list dcp-vehicle-details-list']"
            )
            save_to_file = []
            for detail in details_list:
                all_details =detail.text
            save_to_file.append(all_details.split("\n"))
            print (save_to_file)