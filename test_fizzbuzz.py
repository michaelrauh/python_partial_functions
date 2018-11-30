import unittest
import fizzbuzz as subject

class FizzbuzzTest(unittest.TestCase):

    def test_returnOne(self):
        self.assertEqual(subject.fizz_buzz(1), "1")

    def test_returnOtherNum(self):
        self.assertEqual(subject.fizz_buzz(2), "2")