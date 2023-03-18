import time

from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC

from data.locators import SearchPageLocators
from pages.base_page import BasePage


class SearchPage(BasePage):

    def __init__(self, driver, wait):
        self.url = "https://stage.tamm.abudhabi/"
        self.locator = SearchPageLocators
        super().__init__(driver, wait)

    def go_to_search_page(self):
        self.go_to_page(self.url)

    def search_on_home_page(self, input_text):
        self.wait.until(EC.element_to_be_clickable(self.locator.SEARCH_INPUT))
        self.driver.find_element(*self.locator.SEARCH_INPUT).click()
        self.driver.find_element(*self.locator.SEARCH_INPUT).send_keys(input_text)
        self.driver.find_element(*self.locator.SEARCH_INPUT).send_keys(Keys.RETURN)

    def get_service_search_results_title(self, input_text):

        xs = input_text
        s = ''.join(xs)

        self.wait.until(EC.presence_of_element_located(self.locator.SERVICE_NAME))
        text_of_title = []

        page_number = 1

        is_search_page = True

        while is_search_page:

            try:
                self.wait.until(EC.presence_of_element_located(self.locator.SERVICE_NAME))
                self.driver.get("https://stage.tamm.abudhabi/en/searchresults?q="+s+"&pageNumber="+str(page_number))

                self.wait.until(EC.presence_of_element_located(self.locator.SERVICE_NAME))
                elements = self.driver.find_elements(*self.locator.SERVICE_NAME)

                for value in elements:
                    cell_value = value.text
                    text_of_title.append(cell_value)

                page_number += 1

            except:
                break

        return text_of_title
