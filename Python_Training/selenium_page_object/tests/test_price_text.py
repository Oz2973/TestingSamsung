import unittest

from Python_Training import loginPage
from Python_Training import productPage
from Python_Training import baseSelenium
from Python_Training import url, user_text, pw_text


class test_first_price_text(unittest.TestCase):

    def test_first_price_text(self):
        base = baseSelenium()

        driver = base.selenium_start(-)
        login_page = loginPage(driver)
        product_page = productPage(driver)

        login_page.login_with_user_pw(user_text,pw_text)
        price_text = product_page.get_product_price()

        base.selenium_end(driver)


