from selenium.webdriver.common.by import By


class SearchPageLocators:
    """
       Home Page Locators
    """

    SEARCH_INPUT = (By.XPATH, "//button [@type='button']/following-sibling::input")
    SEARCH_LABEL = (By.XPATH, "//h3[text()='No Results Found']")
    SERVICE_NAME = (By.XPATH, "//*[@id='app']/div/div/div[3]/div/div[2]/div/div[2]/div/div[2]/div[1]/div/div/a/h4")
    PAGINATION_NUMBERS = (By.XPATH, "//*[@id='app']/div/div/div[3]/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div")
    NEXT = (By.XPATH, "//div[@class='ui-lib-pagination__item ui-lib-pagination__item_nav'][@aria-label='Next']")