import unittest as ut

"""
Define the function isEven which returns True, if a given number is even and returns False, if the number is odd.

Define a simple class TestIsEvenMethod derived from unittest.TestCase class.

Hint : Import unittest module and use TestCase utility of it. You may type python3.5 to use the latest version for the exercise
"""
""" Approach 1"""
class TestIsEvenMethod (ut.TestCase):
    def isEven(self,number):
        if number %2 == 0:
            return True
        else :
             return False
    def test_isEven1(self):
        self.assertEqual(self.isEven(5),False,"Should be Odd")


cs1 =TestIsEvenMethod()

print(cs1.test_isEven1())
print("is Given Even Number ",cs1.isEven(5))

""" Approach 2"""
class TestIsEvenMethod2(ut.TestCase):
    def __init__(self,number):
        self.number =number;

    def isEven(self):
        if self.number%2 == 0:
            return True
        else :
            return False

csq =TestIsEvenMethod2(6)
print(csq.isEven())
