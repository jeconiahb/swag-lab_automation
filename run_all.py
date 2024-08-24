import unittest
from tests import loginTest, transactionTest

if __name__ == "__main__":
    login_tests = unittest.TestLoader().loadTestsFromModule(loginTest)
    transaction_tests = unittest.TestLoader().loadTestsFromModule(transactionTest)

    test_suite = unittest.TestSuite([login_tests, transaction_tests])
    # test_suite = unittest.TestSuite([transaction_tests])
    unittest.TextTestRunner().run(test_suite)
