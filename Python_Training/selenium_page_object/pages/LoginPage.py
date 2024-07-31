import time

from selenium.webdriver.common.by import By


class LoginPage():
    def __init__(self,driver):
        self.driver = driver
        self.user = "user-name"
        self.pw = "password"
        self.login = "login-button"

    def set_user(self,user_text):
        user_element = self.driver.find_element(By.ID,self.user)
        user_element.click()
        user_element.clear()
        user_element.send_keys(user_text)
        user_element.click()

    def set_pw(self, pw_text):
        pw_element = self.driver.find_element(By.ID,self.pw)
        pw_element.click()
        pw_element.clear()
        pw_element.send_keys(pw_text)


    def click_login(self):
        login_button = self.driver.find_element(By.ID,self.login)
        login_button.click()

    def login_with_user_pw(self,user_text,pw_text):
        print(f"Try to login with user {user_text} and password {pw_text}")
        self.set_user(user_text)
        self.set_pw(pw_text)
        self.click_login()
        time.sleep(3)
