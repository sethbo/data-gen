'''
Created on Apr. 16, 2020

@author: scott
'''

import unittest
from data.utils.erf import erf_inverse
from data.distributions.LogNormal import LogNormal

class Test(unittest.TestCase):

    '''
    https://keisan.casio.com/exec/system/1180573448 is the oracle
    '''
    def testErfInverse(self):
        self.assertEqual(0, erf_inverse(0))
        self.assertAlmostEqual(0.08885599049425768, erf_inverse(0.1), 16)
        self.assertAlmostEqual(0.4769362762044699,  erf_inverse(0.5), 15)
        self.assertAlmostEqual(1.1630871536766741,  erf_inverse(0.9), 15)
        self.assertAlmostEqual(1.8213863677184497,  erf_inverse(0.99), 15)
        self.assertAlmostEqual(2.3267537655135247,  erf_inverse(0.999), 15)
        self.assertAlmostEqual(3.4589107372795000,  erf_inverse(0.999999), 11)
        self.assertAlmostEqual(4.32000538491345,    erf_inverse(0.999999999), 8)
        self.assertAlmostEqual(5.042029745639,      erf_inverse(0.999999999999), 5)
        self.assertAlmostEqual(5.675846347,         erf_inverse(0.999999999999999), 3)
        with self.assertRaises(ArithmeticError): 
            erf_inverse(0.999999999999999999)

    def testLogNormal(self):
        dist = LogNormal(1000, 100000, 1)
        quantile_values = dist.getQuantileValues()
        self.assertEqual(1000, len(quantile_values))
        self.assertEqual(99785, sum(quantile_values))

        dist = LogNormal(10000, 1000000, 1)
        quantile_values = dist.getQuantileValues()
        self.assertEqual(10000, len(quantile_values))
        self.assertEqual(999671, sum(quantile_values))

        dist = LogNormal(100000, 10000000, 1)
        quantile_values = dist.getQuantileValues()
        self.assertEqual(100000, len(quantile_values))
        self.assertEqual(9999519, sum(quantile_values))

        dist = LogNormal(1000, 100000, 0.5)
        quantile_values = dist.getQuantileValues()
        self.assertEqual(1000, len(quantile_values))
        self.assertEqual(88227, sum(quantile_values))
        
        dist = LogNormal(10000, 1000000, 0.5)
        quantile_values = dist.getQuantileValues()
        self.assertEqual(10000, len(quantile_values))
        self.assertEqual(88227, sum(quantile_values))
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()