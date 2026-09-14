from hiker import answer
import unittest


class TestHiker(unittest.TestCase):

    def test_the_answer_is_two_digits_long(self):
        self.assertEqual(2, len(str(answer())))

    def test_life_the_universe_and_everything(self):
        self.assertEqual(42, answer())

    def test_the_answer_is_not_the_question(self):
        self.assertNotEqual('6 * 7', str(answer()))


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
