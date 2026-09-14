from hiker import answer
import unittest


class TestAnswerSize(unittest.TestCase):

    def test_the_answer_is_three_digits_long(self):
        self.assertEqual(3, len(str(answer())))


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
