import time

from selenium.webdriver.common.by import By


class SearchResults:

    #change it to SearchResultsPage
    def __init__(self, driver):
        self.driver = driver
        self.search_results_bar = "search-result-global-srp-tab-bar__link"
        # google if this variable is only available here!!
        # we can verify this by using - document.getElementsByClassName("search-result-global-srp-tab-bar__link")
        self.product_title = "Galaxy S24 Ultra"
        self.product_price_element = "result-price__money"
        self.product_original_price_element = "search-result-global__result-price__normal-money"
        # when there's a sale there's an original price element
        self.product_details_element = "search-result-global__result-item__content"
        self.product_title_element = "a.search-result-global__result-title__link"

    def get_search_results_bar(self):
        search_results_bar = self.driver.find_elements(By.CLASS_NAME, self.search_results_bar)
        assert len(search_results_bar) != 0, "The current page isn't 'search results', check for changes in the site";

    def get_product_title(self):
        product_title = self.driver.find_elements(By.LINK_TEXT, self.product_title)
        assert product_title is not None, f"Product '{self.product_title}' was not found"
        # EDEN'S ONLY CONTRIBUTION
        # Ask kobi what is cleaner code "is not None" OR "len != 0"

    def get_product_price(self):
        time.sleep(3)
        product_details_dynamic = self.driver.find_elements(By.CLASS_NAME, self.product_details_element)
        item_text = product_details_dynamic[0].text
        parent_element = product_details_dynamic[0]
        item_text_split = item_text.split("\n")
        if self.product_title in item_text_split:
            price = parent_element[1][:8]
            # fix the slicing
            price_element = parent_element.find_element(By.CLASS_NAME, self.product_price_element)
            original_price_element = parent_element.find_element(By.CLASS_NAME, self.product_original_price_element)
            self.price_value = price_element.text
            self.original_price_value = original_price_element.text




        for title in product_details_dynamic:
            # if product_details_dynamic.count("Galaxy S24 Ultra") >= 1:
            parent_element = title.find_element(By.XPATH, "..")
            price_element = parent_element.find_element(By.CLASS_NAME, "result-price__money")
            price_value = price_element.text
            # if title
            print('Price:', price_value)
            break


        # for product_price in product_details_dynamic:
        #     parent_element = product_price.find_element(By.XPATH, "..")
        #     price_element = parent_element.find_element(By.CLASS_NAME, self.product_price_element)
        #     original_price_element = parent_element.find_element(By.CLASS_NAME, self.product_original_price_element)
        #     self.price_value = price_element.text
        #     self.original_price_value = original_price_element.text
        #     break


        # print(self.price_value)
        # print(self.original_price_value)


        # product_price_dynamic = product_details_dynamic.find_element(By.CLASS_NAME, self.product_price_element)
        # product_original_price_dynamic = product_details_dynamic.find_element(By.CLASS_NAME, self.product_original_price_element)
        # print(f"{product_price_dynamic} is price after sale")
        # print(f"{product_original_price_dynamic} is price before sale")
        # # assert product_details_dynamic == self.product_title , f"product "
