import time

from selenium.webdriver.common.by import By


class SearchResultsPage:

    def __init__(self, driver, product_title):
        self.driver = driver
        self.product_title = product_title
        self.search_results_bar = "search-result-global-srp-tab-bar__link"
        self.product_price_element = "result-price__money"
        self.product_original_price_element = "search-result-global__result-price__normal-money"
        # if there's a sale there's an original price element
        self.product_details_element = "search-result-global__result-item__content"
        self.product_title_element = "a.search-result-global__result-title__link"

    def get_search_results_bar(self):
        time.sleep(3)
        search_results_bar = self.driver.find_elements(By.CLASS_NAME, self.search_results_bar)
        assert len(search_results_bar) != 0, "The current page isn't 'search results', check for changes in the site";

    def get_product_title(self):
        time.sleep(3)
        product_title = self.driver.find_elements(By.LINK_TEXT, self.product_title)
        assert product_title is not None, f"Product '{product_title}' was not found"

    def get_product_price(self):
        time.sleep(3)
        product_details_dynamic = self.driver.find_elements(By.CLASS_NAME, self.product_details_element)
        item_text = product_details_dynamic[0].text
        item_text_split = item_text.split("\n")

        if len(item_text_split) == 6 :
            currency_type = item_text_split[1][:1]
            price_after_discount = float(item_text_split[1].split("(")[0][1:])
            price_before_discount = float(item_text_split[2][2:].split(")")[0])
            assert price_after_discount < price_before_discount , "Error! price after discount isn't cheaper than before discount"
            price_difference = price_before_discount - price_after_discount
            print(f"The current price for the product is {currency_type}{price_after_discount}, and the discount is {currency_type}{price_difference}")

        elif len(item_text_split) == 5 :
            currency_type = item_text_split[1][:1]
            price_before_discount = float(item_text_split[1][1:-8])
            assert price_before_discount>0 , f"Error! The price before discount isn't positive"
            print(f"The price for the product is {currency_type}{price_before_discount}")

        else :
            assert False ,"Error"
