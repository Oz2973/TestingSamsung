from selenium.webdriver.common.by import By

from Python_Training.Selenium.SeleniumBaseExample import SeleniumBaseExample


class appiltools():
    base = SeleniumBaseExample()
    driver = base.selenium_start("https://demo.applitools.com/app.html")
    user = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
    user.click()
    user.send_keys("card")

    print("End test")
