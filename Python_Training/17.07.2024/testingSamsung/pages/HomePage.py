from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.product = "Galaxy S24 Ultra"
        self.search_icon = "nv00-gnb__utility-btn.gnb__search-btn-js"
        self.search_submit = "gnb-search__input-btn--search"
        self.search_bar = "gnb-search__input"
        # ask Kobi if this belongs here or belongs in globalSamsung

    def search_Function(self):
        search_icon = self.driver.find_element(By.CLASS_NAME, self.search_icon)
        search_submit = self.driver.find_element(By.CLASS_NAME, self.search_submit)
        search_icon.click()
        search_bar = self.driver.find_element(By.CLASS_NAME, self.search_bar)
        search_bar.send_keys(self.product)
        search_submit.click()