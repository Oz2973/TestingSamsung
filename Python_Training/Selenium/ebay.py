import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver

print("Test start")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.get("https://www.ebay.com/")
search = driver.find_element(By.ID,"gh-ac")
time.sleep(3) #3 seconds
search.click()
search.click()
search.send_keys("Man's shoes")
search.send_keys(Keys.ENTER)

number_Of_Results = driver.find_element(By.CLASS_NAME,"srp-controls__control srp-controls__count")
print(number_Of_Results)


print("Test end")
driver.quit()

