from selenium.webdriver.common.by import By

from Python_Training.Selenium.SeleniumBaseExample import SeleniumBaseExample


class csseg():
    base = SeleniumBaseExample()
    driver = base.selenium_start("https://www.saucedemo.com/")
    user = driver.find_element(By.CSS_SELECTOR, "input[class='input_error form_input']")
    #     user = driver.find_element(By.CSS_SELECTOR, "input[class*='input_error*']")
    user.click()
    user.send_keys("standard_user")
    pw = driver.find_element(By.CSS_SELECTOR, "input[data-test='password']")
    pw.click()
    pw.send_keys("secret_sauce")

    elements = driver.find_elements(By.CSS_SELECTOR,"input[class='input_error form_input']")
    print(elements[1])

    loginButton = driver.find_element(By.CSS_SELECTOR,"input[class='submit-button btn_action']")
    loginButton.click()


    base.selenium_end(driver)

