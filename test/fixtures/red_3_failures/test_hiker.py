from hiker import answer
import unittest


class TestHiker(unittest.TestCase):

    def test_life_the_universe_and_everything(self):
        self.assertEqual(42, answer())

    def test_the_answer_is_three_digits_long(self):
        self.assertEqual(3, len(str(answer())))

    def test_the_answer_is_the_question(self):
        self.assertEqual('6 * 7', str(answer()))


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
