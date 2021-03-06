import unittest
import leapyear

class TestCase(unittest.TestCase):
    def test_input(self):
        self.assertEqual(leapyear.valid_input(1),1)
        self.assertEqual(leapyear.valid_input(4),4)
        self.assertEqual(leapyear.valid_input(300),300)
        self.assertEqual(leapyear.valid_input('h'),None)
        self.assertEqual(leapyear.valid_input(-1),None)
        self.assertEqual(leapyear.valid_input('hello'),None)
    def test_div_400(self):
        self.assertEqual(leapyear.div_400(400),True)
        self.assertEqual(leapyear.div_400(800),True)
        self.assertEqual(leapyear.div_400(0),True)
        self.assertEqual(leapyear.div_400(401),False)
        self.assertEqual(leapyear.div_400(1),False)
    def test_div_100(self):
        self.assertEqual(leapyear.div_100(100),True)
        self.assertEqual(leapyear.div_100(200),True)
        self.assertEqual(leapyear.div_100(0),True)
        self.assertEqual(leapyear.div_100(101),False)
        self.assertEqual(leapyear.div_100(1),False)
    def test_div_4(self):
        self.assertEqual(leapyear.div_4(4),True)
        self.assertEqual(leapyear.div_4(8),True)
        self.assertEqual(leapyear.div_4(0),True)
        self.assertEqual(leapyear.div_4(5),False)
        self.assertEqual(leapyear.div_4(1),False)
    def test_prog(self):
        self.assertEqual(leapyear.leap_year(4),True)
        self.assertEqual(leapyear.leap_year(8),True)
        self.assertEqual(leapyear.leap_year(0),True)
        self.assertEqual(leapyear.leap_year(5),False)
        self.assertEqual(leapyear.leap_year(400),True)
        self.assertEqual(leapyear.leap_year(100),False)
        self.assertEqual(leapyear.leap_year(200),False)
if __name__ == '__main__':
    unittest.main()