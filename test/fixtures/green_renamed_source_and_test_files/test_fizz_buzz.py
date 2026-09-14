from fizz_buzz import fizz_buzz
import unittest


class TestFizzBuzz(unittest.TestCase):

    def test_life_the_universe_and_everything(self):
        self.assertEqual(42, fizz_buzz())


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
