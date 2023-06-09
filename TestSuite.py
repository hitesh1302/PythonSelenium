import unittest

#Import test modules

from LoginTest import LoginTestCases
from SecondPythonTest import Module2TestCases
from ForgotPasswordTest import ForgotPwdTestCases

#Create test suite

test_suite = unittest.TestSuite()

# Add the test cases from each module to the test suite
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(LoginTestCases))
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Module2TestCases))
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(ForgotPwdTestCases))

# Create a test runner and run the test suite
runner = unittest.TextTestRunner()
runner.run(test_suite)
