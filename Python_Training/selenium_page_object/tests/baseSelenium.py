from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver

class baseSelenium():
    def selenium_start(self,url):
        print("Test start")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(10) # makes the program wait UNTIL X seconds if the elment isn't found
        # If the element is found after 1 sec (for eg) it proceeds after 1 second,
        # If we get a timeout = exception
        return driver


    def selenium_end(self,driver):
        driver.close()
        print ("Test end")