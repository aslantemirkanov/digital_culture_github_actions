import unittest
import calculator

class CalcTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(2, 2), 4)
        self.assertEqual(calculator.add(-2, 2), 0)
        self.assertEqual(calculator.add(100, -1000), -900)
        self.assertEqual(calculator.add(0, 0), 0)
        self.assertEqual(calculator.add(1000, -100), 900)
        self.assertEqual(calculator.add(41, 223656235873583258623587), 223656235873583258623628)
        self.assertEqual(calculator.add(223656235873583258623587, 41), 223656235873583258623628)
    def test_sub(self):
        self.assertEqual(calculator.sub(2, 2), 0)
        self.assertEqual(calculator.sub(2, -2), 4)
        self.assertEqual(calculator.sub(0, 2), -2)
        self.assertEqual(calculator.sub(2, 0), 2)
        self.assertEqual(calculator.sub(1000, 500), 500)
        self.assertEqual(calculator.sub(0, 0), 0)
    def test_mul(self):
        self.assertEqual(calculator.mul(2, 2), 4)
        self.assertEqual(calculator.mul(0, 5), 0)
        self.assertEqual(calculator.mul(0, 0), 0)
        self.assertEqual(calculator.mul(-1, 2), -2)
        self.assertEqual(calculator.mul(-1, -2), 2)
        self.assertEqual(calculator.mul(14635473461, 547893278923597), 8018677543146574540159217)
        self.assertEqual(calculator.mul(100000000000, -2), -200000000000)
    def test_div(self):
        self.assertEqual(calculator.div(8, 4), 2)
        self.assertEqual(calculator.div(908, 0), "haha noob")
        self.assertEqual(calculator.div(0, 7678123), 0)
        self.assertEqual(calculator.div(908, -12), -75.66666666666667)
        self.assertEqual(calculator.div(-6101401309898916, -90180293), 67657812)

if __name__ == '__main__':
    unittest.main()

