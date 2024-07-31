import unittest

from Python_Training.testingSamsung.pages.HomePage import HomePage
from Python_Training.testingSamsung.tests.globalSamsung import urlSamsung
from Python_Training.testingSamsung.tests.SamsungSelenium import SamsungSelenium

from Python_Training.testingSamsung.pages.SearchResultsPage import SearchResultsPage


class SamsungProductTests(unittest.TestCase):

    def setUp(self):
        base = SamsungSelenium()
        self.driver = base.selenium_start(urlSamsung)
        home_page = HomePage(self.driver)
        home_page.search_Function()
        self.search_results = SearchResultsPage(self.driver)
        self.test_product_successful_search()
        self.test_product_name()

    def test_product_successful_search(self):
        self.search_results.get_search_results_bar()

    def test_product_name(self):
        self.search_results.get_product_title()

    def test_product_price(self):
        self.search_results.get_product_price()

    if __name__ == "__main":
        unittest.main()


        print("Test End")
