import unittest
from bot import get_longest_word, get_word_length, get_shortest_word


class BotTestCase(unittest.TestCase):
    sentence = "The cow jumped over the moon."

    def test_longest_word_and_len(self):
        expected_longest_word = "jumped"
        expected_longest_word_len = 6
        longest_word = str(get_longest_word(self.sentence)).lower()
        longest_word_len = get_word_length(longest_word)
        """Checks if word is the expected one"""
        self.assertEqual(longest_word, expected_longest_word)
        """Checks if word length is the expected one"""
        self.assertEqual(longest_word_len, expected_longest_word_len)

    def test_shortest_word_and_len(self):
        expected_shortest_word = "the"
        expected_shortest_word_len = 3
        shortest_word = str(get_shortest_word(self.sentence)).lower()
        shortest_word_len = get_word_length(shortest_word)
        """Checks if word is the expected one"""
        self.assertEqual(shortest_word, expected_shortest_word)
        """Checks if word length is the expected one"""
        self.assertEqual(shortest_word_len, expected_shortest_word_len)

    def test_get_word_len(self):
        word = "moon"
        expected_length = 4
        word_length = get_word_length(word)
        self.assertEqual(word_length, expected_length)

