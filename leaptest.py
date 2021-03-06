import unittest
import leapyear

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(leapyear.valid_input(1),1)
        self.assertEqual(leapyear.valid_input(4),4)
        self.assertEqual(leapyear.valid_input(300),300)
        self.assertEqual(leapyear.valid_input('h'),None)
        self.assertEqual(leapyear.valid_input(-1),None)
        self.assertEqual(leapyear.valid_input('hello'),None)

if __name__ == '__main__':
    unittest.main()