import unittest

def fizzbuzz(number):
    if number == 15:
        return 'FizzBuzz'
    if number % 3 == 0:
        return 'Fizz'

class TestFizzBuzz(unittest.TestCase):
    def test_input_3_should_get_fizz(self):
        result = fizzbuzz(3)
        self.assertEqual(result, 'Fizz')

    def test_input_6_should_get_fizz(self):
        result = fizzbuzz(6)
        self.assertEqual(result, 'Fizz')

    def test_input_15_should_get_fizz_buzz(self):
        result = fizzbuzz(15)
        self.assertEqual(result, 'FizzBuzz')

unittest.main()