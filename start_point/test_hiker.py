from hiker import global_answer, Hiker
import unittest


class TestHiker(unittest.TestCase):

    def test_global_function(self):
        self.assertEqual(42, global_answer())

    def test_instance_method(self):
        self.assertEqual(42, Hiker().instance_answer())


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
