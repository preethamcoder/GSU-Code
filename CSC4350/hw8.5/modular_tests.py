import unittest
from messy_function import *

class TestMessy(unittest.TestCase):
	def test_val(self):
		test_sub = -1
		res = check_val(test_sub)
		self.assertEqual(res, 0)

	def test_val2(self):
		tst_sub = 12
		res = check_val(tst_sub)
		self.assertEqual(res, 12)

	def test_bin_str(self):
		tst_sub = 128
		res = num_to_bin_str(tst_sub)
		self.assertEqual(res, "1111111")

	def test_bin_str2(self):
		tst_sub = 8
		res = num_to_bin_str(tst_sub)
		self.assertEqual(res, "111")

	def test_full(self):
		test_sub = 128
		res = function_that_is_too_long(test_sub)
		self.assertEqual(res, 4)

	def test_full2(self):
		test_sub = 10
		res = function_that_is_too_long(test_sub)
		self.assertEqual(res, 2)

if __name__ == '__main__':
	unittest.main()

