import unittest
from tax import *

class Testtax(unittest.TestCase):
	"""Test tax"""
	def test_tax(self):
		"""husband=360000, wife=200000"""
		h = 360000
		w = 200000
		self.assertEqual(18000,cal_MPF(h))
		self.assertEqual(10000,cal_MPF(w))
		self.assertEqual(17700, cal_stax(h))
		self.assertEqual(1480, cal_stax(w))
		self.assertEqual(19180, cal_stax(w)+cal_stax(h))
		self.assertEqual(27560, cal_jtax(h, w))

	def test1_tax(self):
		"""husband=0, wife=2000000"""
		h = 0
		w = 2000000
		self.assertEqual(0, cal_MPF(h))
		self.assertEqual(18000, cal_MPF(w))
		self.assertEqual(0, cal_stax(h))
		self.assertEqual(296500, cal_stax(w))
		self.assertEqual(296500, cal_stax(w) + cal_stax(h))
		self.assertEqual(274060, cal_jtax(h, w))

	def test2_tax(self):
		"""single=300000"""
		s = 300000
		self.assertEqual(15000, cal_MPF(s))
		self.assertEqual(9420, cal_stax(s))

	def test3_tax(self):
		"""single=30000000"""
		s = 30000000
		self.assertEqual(18000, cal_MPF(s))
		self.assertEqual(4497300, cal_stax(s))

	def test4_tax(self):
		"""husband=3600000, wife=2000000"""
		h = 3600000
		w = 2000000
		self.assertEqual(18000,cal_MPF(h))
		self.assertEqual(18000,cal_MPF(w))
		self.assertEqual(537300, cal_stax(h))
		self.assertEqual(296500, cal_stax(w))
		self.assertEqual(833800, cal_stax(w)+cal_stax(h))
		self.assertEqual(834600, cal_jtax(h, w))

	def test5_tax(self):
		"""husband=5000000, wife=2000"""
		h = 5000000
		w = 2000
		self.assertEqual(18000,cal_MPF(h))
		self.assertEqual(0,cal_MPF(w))
		self.assertEqual(747300, cal_stax(h))
		self.assertEqual(0, cal_stax(w))
		self.assertEqual(747300, cal_stax(w)+cal_stax(h))
		self.assertEqual(747600, cal_jtax(h, w))

	def test6_tax(self):
		"""husband=240000, wife=440000"""
		h = 240000
		w = 440000
		self.assertEqual(12000,cal_MPF(h))
		self.assertEqual(18000,cal_MPF(w))
		self.assertEqual(3760, cal_stax(h))
		self.assertEqual(31300, cal_stax(w))
		self.assertEqual(35060, cal_stax(w)+cal_stax(h))
		self.assertEqual(47620, cal_jtax(h, w))



if __name__ == '__main__':
	unittest.main()