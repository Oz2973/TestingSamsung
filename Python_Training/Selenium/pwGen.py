from time import sleep

from selenium.webdriver.common.by import By

from Python_Training.Selenium.SeleniumBaseExample import SeleniumBaseExample

selenium_base = SeleniumBaseExample()
driver = selenium_base.selenium_start("https://www.calculator.net/password-generator.html")
sleep(5)
# pwLength = driver.find_element(By.CLASS_NAME,"infull")
# pwLength.click()
# pwLength.clear()
# pwLength.send_keys(15)

check_box = driver.find_elements(By.CLASS_NAME,"cbmark")
check_box[1].click()
check_box[4].click()
check_box[5].click()
check_box[6].click()

submitButt = driver.find_element(By.NAME,"submit1")
submitButt.submit()
sleep(5)
output = driver.find_element(By.ID,"resultid")
pw = output.text
print(pw)
start_index = pw.index("Password") +9
stop_index = pw.index("Password Strength") -1
final = pw [start_index:stop_index]
final = final.strip()
print(f"The result is {final}")


print("what")


