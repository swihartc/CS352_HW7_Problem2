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
if __name__ == '__main__':
    unittest.main()