from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class LoginTest(unittest.TestCase):

    @classmethod
    def setupClass(cls):
        cls.driver = webdriver.Chrome("C:/Users/zzami/PycharmProjects/AutomationExercise/venv/driver/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_RegisterAndDeleteUser(self):
        self.driver.get("https://automationexercise.com/")
        self.driver.find_element(by=By.XPATH, value="//header[@id='header']/div/div/div/div[2]/div/ul/li[4]/a").click()
        self.driver.find_element(by=By.NAME, value="name").send_keys("testUsername_01")
        self.driver.find_element(by=By.XPATH, value="//section[@id='form']/div/div/div[3]/div/form/input[3]").send_keys(
            "testUsername_01@gmail.com")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")



