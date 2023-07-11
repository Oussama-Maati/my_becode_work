import os
import unittest

import method


class TestAdditionTest(unittest.TestCase):

    def test_(self):
        self.assertEqual(2, method.addition(1, 1))

    def test_2(self):
        self.assertEqual(5, method.addition(2, 3))

    def test_4(self):
        self.assertEqual(7, method.addition(5, 2))

    def test_5(self):
        self.assertEqual(5, method.addition(2, 3))

    def test_6(self):
        self.assertEqual(24, method.addition(20, 4))

    def test_7(self):
        self.assertEqual(200, method.addition(200, 0))

    def test_8(self):
        self.assertEqual(234233, method.addition(2999, 231234))

    def test_9(self):
        self.assertEqual(0, method.addition(0, 0))


class TestSubtraction(unittest.TestCase):
    def test_1(self):
        self.assertEqual(0, method.subtraction(1, 1))

    def test_2(self):
        self.assertEqual(-1, method.subtraction(2, 3))

    def test_4(self):
        self.assertEqual(3, method.subtraction(5, 2))

    def test_5(self):
        self.assertEqual(-1, method.subtraction(2, 3))

    def test_6(self):
        self.assertEqual(16, method.subtraction(20, 4))

    def test_7(self):
        self.assertEqual(200, method.subtraction(200, 0))

    def test_8(self):
        self.assertEqual(-228235, method.subtraction(2999, 231234))

    def test_9(self):
        self.assertEqual(0, method.subtraction(0, 0))


class TestDivide(unittest.TestCase):
    def test_1(self):
        self.assertEqual(1, method.divide(1, 1))

    def test_2(self):
        self.assertEqual(0.6666666666666666, method.divide(2, 3))

    def test_4(self):
        self.assertEqual(2.5, method.divide(5, 2))

    def test_5(self):
        self.assertEqual(0.6666666666666666, method.divide(2, 3))

    def test_6(self):
        self.assertEqual(5.0, method.divide(20, 4))

    def test_7(self):
        self.assertEqual("You can't divide by zero!", method.divide(200, 0))

    def test_8(self):
        self.assertEqual(0.012969546001020611, method.divide(2999, 231234))

    def test_9(self):
        self.assertEqual("You can't divide by zero!", method.divide(0, 0))


class TestFile(unittest.TestCase):
    def test_file_creation(self):
        method.create_test_file()
        assert os.path.exists("test.txt") == True

    def test_file_content(self):
        method.create_test_file()
        with open("test.txt", 'r') as file:
            file_content = file.read()
            assert file_content == 'this is a text'

    def test_file_deletion(self):
        method.create_test_file()
        method.delete_test_file()
        assert os.path.exists("test.txt") == False


if __name__ == '__main__':
    unittest.main()
