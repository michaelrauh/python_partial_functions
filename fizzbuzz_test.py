import unittest
import fizzbuzz as subject

class FizzbuzzTest(unittest.TestCase):

    def test_returnOne(self):
        self.assertEqual(subject.fizz_buzz(1), "1")

    def test_returnOtherNum(self):
        self.assertEqual(subject.fizz_buzz(2), "2")

    def test_returnFizz(self):
        self.assertEqual(subject.fizz_buzz(3), "Fizz")

    def test_returnBuzz(self):
        self.assertEqual(subject.fizz_buzz(5), "Buzz")

    def test_returnFizzBuzz(self):
        self.assertEqual(subject.fizz_buzz(15), "FizzBuzz")