from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep


# Perform ActionChains use this class given below
from selenium.webdriver.common.action_chains import ActionChains

class Vino:
    url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
    username = 'Admin'
    password = 'admin123'
    username_locator = 'username' # Name
    password_locator = 'password' # Name
    submitButton_locator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    logout_dropdown = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p'
    logout_button = 'Logout' # LINK_TEXT
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    # Method for login
    def login(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        sleep(3)
        self.driver.find_element(by=By.NAME, value=self.username_locator).send_keys(self.username)
        self.driver.find_element(by=By.NAME, value=self.password_locator).send_keys(self.password)
        self.driver.find_element(by=By.XPATH, value=self.submitButton_locator).click()
        print("LOGIN Method Success")
   
    # Method for logout using Action Chains
    def logout(self):
        sleep(3)
        action = ActionChains(self.driver)
        logout_dropdown = self.driver.find_element(by=By.XPATH, value=self.logout_dropdown)
        action.click(on_element=logout_dropdown).perform()
        sleep(5)
        self.driver.find_element(by=By.LINK_TEXT, value=self.logout_button).click()
        print("LOGOUT Method Success")

Vino().login()
Vino().logout()        