import unittest
import rpn

class TestBasics(unittest.TestCase):
	def test_add(self):
		result_add = rpn.calculate('1 1 +')
		self.assertEqual(2, result_add)

    def test_exp(self):
        result_exp = rpn.calculate('2 3 ^')
        self.assertEqual(8, result_exp)
