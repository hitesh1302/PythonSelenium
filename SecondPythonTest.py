from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Create a Service object with the path to the ChromeDriver executable

#service = Service('C:\\BrowserDriver\\chromedriver_win32\\chromedriver.exe')
service = Service('C:\\BrowserDriver\\chromedriver_win32\\geckodriver.exe')
#service = Service('C:\\BrowserDriver\\edgedriver_win64\\msedgedriver.exe')

# Start the WebDriver with the Service object

#driver = webdriver.Chrome(service=service)
driver = webdriver.Firefox(service=service)
#driver = webdriver.Edge(service=service)
class PlanningModuleCases(unittest.TestCase):
   def test_PlanningTab(self):
    driver.get('https://org0.artifex-pwa.integration.edition1.nl/login')
    driver.maximize_window()
    email = driver.find_element(By.ID, "email")
    email.send_keys("edition1.artifex+admin1@gmail.com")
    password = driver.find_element(By.ID, "password")
    password.send_keys("Pa$$W0rd")
    btn = driver.find_element(By.CLASS_NAME, "ant-btn")
    btn.click()



