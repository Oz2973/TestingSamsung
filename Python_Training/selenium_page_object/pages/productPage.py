from selenium.webdriver.common.by import By


class productPage():
    def __init__(self,driver):
        self.driver = driver
        self.price = "inventory_item_price"

    def get_product_price(self):
        prices = self.driver.find_elements(By.CLASS_NAME, self.price)
        price_text = prices[0].text
        print(f"price found the value is {price_text}")
        assert price_text == "$29.99", "The price is not $29.99"
        return price_text


