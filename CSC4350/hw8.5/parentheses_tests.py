import unittest
from parentheses import parentheses_to_remove

class TestParen(unittest.TestCase):
	def test_parentheses(self):
		test_sub = "(()(assa(())))"
		res = parentheses_to_remove(test_sub)
		self.assertEqual(res, 0)

	def test_parenteses2(self):
		tst_sub = "((()))({}}}}}}()"
		res = parentheses_to_remove(tst_sub)
		self.assertEqual(res, 1)

if __name__ == '__main__':
	unittest.main()

