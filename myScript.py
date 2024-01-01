from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from time import sleep

def create_driver() -> webdriver:
    """ Returns the webdriver through which we interact with the browser"""

    service = Service(executable_path="geckodriver.exe")
    driver = webdriver.Firefox(service=service)
    return driver


def enter_credentials(driver: webdriver, username:str, password:str):
    """Takes in username and password and signs the user 
    in to their home page """

    username_field = driver.find_element(By.NAME, "username")
    username_field.send_keys(username)

    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys(password)

    sleep(2) # time delay


def attempt_login(driver:webdriver):
     """CLicks login button"""

     driver.find_element(By.ID, "login").click()
     sleep(2)