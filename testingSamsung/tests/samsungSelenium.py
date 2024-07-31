from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

class samsungSelenium():
    def selenium_start(self, url):
        print("Test start")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(10) # makes the program wait UNTIL X seconds if the element isn't found
        # If the element is found after 1 sec (for eg) it proceeds after 1 second,
        # If we get a timeout = exception
        return driver


    def selenium_end(self, driver):
        driver.close()
        print ("Test end")