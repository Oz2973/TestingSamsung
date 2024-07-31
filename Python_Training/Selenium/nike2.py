from selenium.webdriver.common.by import By

from Python_Training.Selenium.SeleniumBaseExample import SeleniumBaseExample

selenium_base = SeleniumBaseExample()
driver = selenium_base.selenium_start("https://www.nike.com/")

man_button = driver.find_element(By.LINK_TEXT, "Men")
man_button.click()

selenium_base.selenium_end(driver)
