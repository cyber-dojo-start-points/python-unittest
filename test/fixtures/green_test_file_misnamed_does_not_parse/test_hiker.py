from hiker import answer
import unittest


class TestHiker(unittest.TestCase):

    def test_life_the_universe_and_everything(self):
        self.assertEqual(42, answer())


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
