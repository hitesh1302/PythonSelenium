from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import unittest


# Create a Service object with the path to the ChromeDriver executable

#service = Service('C:\\BrowserDriver\\chromedriver_win32\\chromedriver.exe')
service = Service('C:\\BrowserDriver\\chromedriver_win32\\geckodriver.exe')
#service = Service('C:\\BrowserDriver\\edgedriver_win64\\msedgedriver.exe')

# Start the WebDriver with the Service object

#driver = webdriver.Chrome(service=service)
driver = webdriver.Firefox(service=service)
#driver = webdriver.Edge(service=service)
class LoginTestCases(unittest.TestCase):
    def test_ValidCredentials(self):
        driver.get('https://org0.artifex-pwa.integration.edition1.nl/login')
        driver.maximize_window()
        email = driver.find_element(By.ID, "email")
        email.send_keys("edition1.artifex+admin1@gmail.com")
        password = driver.find_element(By.ID, "password")
        password.send_keys("Pa$$W0rd")
        btn = driver.find_element(By.CLASS_NAME, "ant-btn")
        btn.click()

    def test_InvalidCredentails(self):
        driver.get('https://org0.artifex-pwa.integration.edition1.nl/login')
        driver.maximize_window()
        email = driver.find_element(By.ID, "email")
        email.send_keys("edition1.artifex+admin@gmail.com")
        password = driver.find_element(By.ID, "password")
        password.send_keys("Pa$$W0r")
        btn = driver.find_element(By.CLASS_NAME, "ant-btn")
        btn.click()
        """validation_message_element = driver.find_element(By.CLASS_NAME, "ant-notification-notice-description")
                actual_validation_message = validation_message_element.text
                expected_validation_message = "Kan niet inloggen met opgegeven gegevens."
                assert actual_validation_message == expected_validation_message, f"Validation message is incorrect" 
                """

    def test_EmptyFields(self):
        driver.get('https://org0.artifex-pwa.integration.edition1.nl/login')
        driver.maximize_window()
        btn = driver.find_element(By.CLASS_NAME, "ant-btn")
        btn.click()
        email_validation_msg_element = driver.find_element(By.ID, "email_help")
        email_actual_validation_message = email_validation_msg_element.text
        email_expected_validation_msg = "Vul uw e-mailadres in!"
        pwd_validation_msg_element =driver.find_element(By.ID, "password_help")
        pwd_actual_validation_message = pwd_validation_msg_element.text
        pwd_expected_validation_msg ="Vul uw wachtwoord in!"
        #Compare actual validation message with the expected validation message
        assert email_actual_validation_message == email_expected_validation_msg, f"Email validation message is incorrect"
        assert pwd_actual_validation_message == pwd_expected_validation_msg, f"Password validation message is incorrect"

    def test_EmptyPassword(self):
        driver.get('https://org0.artifex-pwa.integration.edition1.nl/login')
        driver.maximize_window()
        email_element = driver.find_element(By.ID, "email")
        email_element.send_keys("edition1.artifex+admin1@gmail.com")
        btn = driver.find_element(By.CLASS_NAME, "ant-btn")
        btn.click()
        pwd_validation_msg_element = driver.find_element(By.ID, "password_help")
        pwd_actual_validation_message = pwd_validation_msg_element.text
        pwd_expected_validation_msg = "Vul uw wachtwoord in!"
        # Compare actual validation message with the expected validation message
        assert pwd_actual_validation_message == pwd_expected_validation_msg, f"Password validation message is incorrect"

    def test_EmptyEmail(self):
        driver.get('https://org0.artifex-pwa.integration.edition1.nl/login')
        driver.maximize_window()
        pwd_element = driver.find_element(By.ID, "password")
        pwd_element.send_keys("Pa$$W0rd")
        btn = driver.find_element(By.CLASS_NAME, "ant-btn")
        btn.click()
        email_validation_msg_element = driver.find_element(By.ID, "email_help")
        email_actual_validation_message = email_validation_msg_element.text
        email_expected_validation_msg = "Vul uw e-mailadres in!"
        # Compare actual validation message with the expected validation message
        assert email_actual_validation_message == email_expected_validation_msg, f"Email validation message is incorrect"









