from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Python_Training.Selenium.SeleniumBaseExample import SeleniumBaseExample

selenium_base = SeleniumBaseExample()
driver = selenium_base.selenium_start("https://advantageonlineshopping.com/#/")
# driver.implicitly_wait(10)
sleep(20)
contactUS = driver.find_element(By.LINK_TEXT ,"CONTACT US")
contactUS.click()
sleep(2)

# category_Drop_Down = Select(driver.find_element(By.CLASS_NAME,"ng-pristine.ng-untouched.ng-valid ng-scope"))
# category_Drop_Down.select_by_index(3)

category_Drop_Down = Select(driver.find_element(By.NAME ,"categoryListboxContactUs"))
category_Drop_Down.select_by_index(3)
sleep(2)

product_Drop_Down = Select(driver.find_element(By.NAME ,"productListboxContactUs"))
product_Drop_Down.select_by_index(2)
sleep(2)


email = driver.find_element(By.NAME, "emailContactUs")
email.click()
email.send_keys("ozwork7@gmail.com")
sleep(2)

subject = driver.find_element(By.NAME, "subjectTextareaContactUs")
subject.click()
subject.send_keys("asdasdasdasd lol")
sleep(2)




send = driver.find_element(By.ID,"send_btn")
send.click()
sleep(2)

SeleniumBaseExample.selenium_end(driver)
