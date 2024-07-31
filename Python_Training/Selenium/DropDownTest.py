from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Python_Training.Selenium.SeleniumBaseExample import SeleniumBaseExample

selenium_base = SeleniumBaseExample()
driver = selenium_base.selenium_start("https://www.saucedemo.com/")

username = driver.find_element(By.ID,"user-name")
username.click()
username.send_keys("standard_user")
password = driver.find_element(By.ID,"password")
password.click()
password.send_keys("secret_sauce")
login_key = driver.find_element(By.ID,"login-button")
login_key.click()

sort_Drop_Down = Select(driver.find_element(By.CLASS_NAME,"product_sort_container"))
sort_Drop_Down.select_by_index(1) # The select selects it
# sort_Drop_Down.select_by_value("az") # The name of the value (in inspect)
# sort_Drop_Down.select_by_visible_text("Price (high to low)")
#The string that's visible in the dropdown



SeleniumBaseExample.selenium_end(driver)