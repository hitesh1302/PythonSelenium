from selenium import  webdriver
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

class ForgotPwdTestCases(unittest.TestCase):
    def test_ForgotPwdLink(self):
        driver.get("https://org0.artifex-pwa.integration.edition1.nl/login")
        driver.maximize_window()
        driver.find_element(By.LINK_TEXT, "Wachtwoord vergeten?").click()

    def test_BacktoLogin(self):
        driver.get("https://org0.artifex-pwa.integration.edition1.nl/login")
        driver.maximize_window()
        driver.find_element(By.LINK_TEXT, "Wachtwoord vergeten?").click()
        driver.find_element(By.LINK_TEXT, "Inloggen").click()

    def test_ResetPassword(self):
        driver.get("https://org0.artifex-pwa.integration.edition1.nl/login")
        driver.maximize_window()
        driver.find_element(By.LINK_TEXT, "Wachtwoord vergeten?").click()
        driver.find_element(By.ID, "email").send_keys("salt.willson@yopmail.com")
        driver.find_element(By.CLASS_NAME, "ant-btn").click()

    def test_EmptyFieldVal(self):
        driver.get("https://org0.artifex-pwa.integration.edition1.nl/login")
        driver.maximize_window()
        driver.find_element(By.LINK_TEXT, "Wachtwoord vergeten?").click()
        driver.find_element(By.CLASS_NAME, "ant-btn").click()
        validation_msg_element = driver.find_element(By.ID, "email_help")
        actual_validation_message = validation_msg_element.text
        expected_validation_message = "Vul uw e-mailadres in!"
        # Compare the actual and expected validation messages
        assert actual_validation_message == expected_validation_message, f"Validation message is incorrect. Actual: '{actual_validation_message}', Expected: '{expected_validation_message}'"

    def test_IncorrectEmailAdd(self):
        driver.get("https://org0.artifex-pwa.integration.edition1.nl/login")
        driver.maximize_window()
        driver.find_element(By.LINK_TEXT, "Wachtwoord vergeten?").click()
        driver.find_element(By.ID, "email").send_keys("salt.willson@yop")
        driver.find_element(By.CLASS_NAME, "ant-btn").click()
        validation_msg_element = driver.find_element(By.ID, "email_help")
        Actual_validation_message = validation_msg_element.text
        expected_validation_message = "De invoer is geen geldig e-mailadres!"
        assert Actual_validation_message == expected_validation_message, f"validation message is incrrect."







if __name__ == "__main__":
    unittest.main()


