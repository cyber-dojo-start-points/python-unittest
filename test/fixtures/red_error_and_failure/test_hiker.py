from hiker import answer, checksum
import unittest


class TestHiker(unittest.TestCase):

    def test_life_the_universe_and_everything(self):
        self.assertEqual(42, answer())

    def test_the_checksum_of_the_answer(self):
        self.assertEqual(0, checksum())


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
