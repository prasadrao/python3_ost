from coconuts import *
import unittest

class SouthAsian(coconut):
    name = "SouthAsian"
    weight = 3.0

class American(coconut):
    name = "American"
    weight = 3.5

class MiddleEastern(coconut):
    name = "MiddleEastern"
    weight = 2.5
class Srilankan(coconut):
    name = "Srilankan"
    weight = 3.0

class Test(unittest.TestCase):

    def setUp(self):
        self.inv_sample = Inventory()
        self.inv_sample.add_coconut(SouthAsian)
        self.inv_sample.add_coconut(SouthAsian)
        self.inv_sample.add_coconut(American)
        self.inv_sample.add_coconut(American)
        self.inv_sample.add_coconut(American)
        self.inv_sample.add_coconut(MiddleEastern)

    def test_inventory_add(self):
        self.assertRaises(TypeError, lambda x: self.inv_sample.add_coconut("Coke"), "Accepting non coconut type")

    def test_inventory_weights(self):
        self.assertRaises(ValueError, lambda x: self.inv_sample.add_coconut(Srilankan), "Accepting coconut type which is having same weight" )

    def test_inventory_tot_weight(self):
        calc_wt = 2*SouthAsian.weight + MiddleEastern.weight +  3*American.weight
        self.assertEqual(calc_wt, self.inv_sample.total_weight(), "Total weight did not match")

if __name__ == "__main__":
    unittest.main()
