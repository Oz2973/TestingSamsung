from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

f_City = "Jerusalem"
t_City = "Acre"

print("Test start")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.egged.co.il/HomePage.aspx")
from_Ad = driver.find_element(By.ID, "from")
to_Ad = driver.find_element(By.ID, "to")

from_Ad.click()
from_Ad.send_keys(f_City)
driver.find_element(By.CLASS_NAME, "title").click()  # && driver.find_element(By.title,f_City)

to_Ad.click()
to_Ad.send_keys(t_City)
driver.find_element(By.CLASS_NAME, "title").click()  # && driver.find_element(By.title,t_City)

driver.find_element(By.ID, "getDirections").click()

print("Test End")
