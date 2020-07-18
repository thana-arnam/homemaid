import unittest
from unittest.mock import patch
import random_number

class TestPrintRandomNumber(unittest.TestCase):
    @patch('random_number.random.randint')
    def test_func_should_call_randint_with_1_and_10(self, mock):
        random_number.print_random_number()
        mock.assert_called_once_with(1, 10)

    @patch('random_number.random.randint')
    def test_get_3_should_return_three(self, mock):
        mock.return_value = 3
        result = random_number.print_random_number()
        self.assertEqual(result, 'three')

    @patch('random_number.random.randint')
    def test_get_5_should_return_three(self, mock):
        mock.return_value = 5
        result = random_number.print_random_number()
        self.assertEqual(result, 'five')

# Commnent this when we run pytest
# unittest.main()