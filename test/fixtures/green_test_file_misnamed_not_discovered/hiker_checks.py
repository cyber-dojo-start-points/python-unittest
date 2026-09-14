# cyber-dojo.sh hands unittest the files matching *test*.py, and the word
# test is nowhere in this name, so these tests never run. Coverage still
# finds the file and reports it as nothing-executed. The assertion is one
# that would fail, so a green says it really did not run rather than that it
# ran and passed.
from hiker import answer
import unittest


class HikerChecks(unittest.TestCase):

    def test_the_answer_is_three_digits_long(self):
        self.assertEqual(3, len(str(answer())))


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
