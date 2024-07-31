import unittest

class pyTestExample(unittest.TestCase):

    def test_1(self):
        pw = "igndysikgm"
        print("into test 1")
        assert len(pw) == 10 ,"The length of pw is not as expected"
        # prints only errors, not success TC


    def test_2(self):
        print("into test 2")
        assert 1 == 2 , "1 is not 1 as expected"


    def test_summary(self):
        num1 = 1
        num2 = 2
        sum = num1+num2
        assert sum == 2, "The summary of num1 and num2 is not as expected"