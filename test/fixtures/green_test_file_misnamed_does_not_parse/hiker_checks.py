# The word test is nowhere in this name, so cyber-dojo.sh never hands it to
# unittest, and it is half written so it does not parse either. Vanishing is
# what it must not do: mypy reads every .py file in the sandbox dir and names
# it, and coverage gives up its whole report over it.
from hiker import answer
import unittest


class HikerChecks(unittest.TestCase):

    def test_the_answer_is_two_digits_long(self):
        self.assertEqual(2, len(str(answer())
