import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
        self.products_container_element = "search-result-global__result__panel"

    def get_search_results_bar(self):
        time.sleep(3)
        search_results_bar = self.driver.find_elements(By.CLASS_NAME, self.search_results_bar)
        assert len(search_results_bar) != 0, "The current page isn't 'search results', check for changes in the site";

    def get_product_title(self):
        time.sleep(3)
        product_title = self.driver.find_elements(By.LINK_TEXT, self.product_title)
        assert product_title is not None, f"Product '{product_title}' was not found"

    def get_product_price(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, self.products_container_element))
            )
        except TimeoutException:
            raise TimeoutException("Failed to locate the container in time")

        product_details_dynamic = self.driver.find_elements(By.CLASS_NAME, self.product_details_element)
        for item_in_array in product_details_dynamic:
            item_text = item_in_array.text
            item_text_split = item_text.split("\n")
            for j in item_text_split:
                if self.product_title == j:
                    if len(item_text_split) == 6 :
                        currency_type = item_text_split[1][:1]
                        price_after_discount = float(item_text_split[1].split("(")[0][1:])
                        price_before_discount = float(item_text_split[2][2:].split(")")[0])
                        assert price_after_discount < price_before_discount , "Error! price after discount isn't cheaper than before discount"
                        price_difference = price_before_discount - price_after_discount
                        print(f"The current price for the product is {currency_type}{price_after_discount}, and the discount is {currency_type}{price_difference}")
                        return

                    elif len(item_text_split) == 5 :
                        currency_type = item_text_split[1][:1]
                        price_before_discount = float(item_text_split[1][1:-8])
                        assert price_before_discount > 0 , f"Error! The price before discount isn't positive"
                        print(f"The price for the product is {currency_type}{price_before_discount}")
                        return

                    else :
                        assert True,"Error"
                        return
