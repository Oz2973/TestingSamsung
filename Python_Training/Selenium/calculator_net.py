from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver

print("Test start")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url = ("https://www.calculator.net/")
driver.get(url)
bmi_button = driver.find_element(By.PARTIAL_LINK_TEXT, "BMI")
bmi_button.click()

# sleep(3)
calorie_button = driver.find_element(By.LINK_TEXT, "Calorie")
calorie_text = calorie_button.text
calorie_button.click()
print(calorie_text)


driver.maximize_window()
driver.close()
print("Test end")