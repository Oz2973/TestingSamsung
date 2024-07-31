# homework
#https://www.demoblaze.com/
#find and output "contact"
# 1.       Go to https://www.demoblaze.com/
# #2.       Make sure the text over contact is “Contacts”
# 3.       Click on it if the text is as expected


# do it By LINKTEXT

from selenium.webdriver.common.by import By

from Python_Training.Selenium.SeleniumBaseExample import SeleniumBaseExample

selenium_base = SeleniumBaseExample()
driver = selenium_base.selenium_start("https://www.demoblaze.com/")

link_button = driver.find_element(By.PARTIAL_LINK_TEXT, "Contact")
if (link_button.text == "Contact"):
    print("Contact")
    link_button.click()
else:
    print("Link text isn't identical to Contact")


selenium_base.selenium_end(driver)


