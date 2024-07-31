from time import sleep

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver

print("Test start")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url = ("https://www.nike.com/")
driver.get(url)
driver.maximize_window()

sleep(3)
men_button = driver.find_element(By.LINK_TEXT, "Men")
men_button.click()

driver.close()
print("Test end")