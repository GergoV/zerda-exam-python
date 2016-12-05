import unittest
import third

class TestCounterMethods(unittest.TestCase):

    def test_if_counts_letters(self):
        self.assertEqual(third.count_letter_in_string('Yolo', 'o'), 2)

    def test_if_word_checked(self):
        self.assertEqual(third.count_letter_in_string(1, 'o'), 0)

if __name__ == '__main__':
    unittest.main()
