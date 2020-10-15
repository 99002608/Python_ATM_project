import unittest
# importing important modules
import random 
import numpy

from ATM_src import Account
# import palindromeCheck

class MyTest(unittest.TestCase):
    def test_my_function(self):
        account = Account(1021);
        self.assertEqual(account.deposit(5000), 5000)
        self.assertEqual(account.deposit(2000), 7000)
        self.assertEqual(account.withdraw(1000), 6000)
        self.assertEqual(account.withdraw(1000), 5000)
        
if __name__ == '__main__':
    unittest.main()
