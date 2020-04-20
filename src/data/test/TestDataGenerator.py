'''
Created on Apr. 16, 2020

@author: scott
'''

import unittest
from data.utils.erf import erf_inverse
from data.distributions.LogNormal import LogNormal
from DataGenerator import TextSeries

class Test(unittest.TestCase):

    '''
    test erf-inverse function
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

    '''
    test Log-normal distribution
    '''
    def testLogNormal(self):
        dist = LogNormal(1000, 100000, 1)
        self.assertAlmostEqual(100, dist.getMean(), 10)
        quantile_values = dist.get_distribution_values()
        self.assertEqual(1000, len(quantile_values))
        self.assertEqual(100000, sum(quantile_values))

        dist = LogNormal(10000, 1000000, 1)
        self.assertAlmostEqual(100, dist.getMean(), 10)
        quantile_values = dist.get_distribution_values()
        self.assertEqual(10000, len(quantile_values))
        self.assertEqual(1000000, sum(quantile_values))

        dist = LogNormal(100000, 10000000, 1)
        self.assertAlmostEqual(100, dist.getMean(), 10)
        quantile_values = dist.get_distribution_values()
        self.assertEqual(100000, len(quantile_values))
        self.assertEqual(10000000, sum(quantile_values))

        dist = LogNormal(100, 10000, 0.5)
        self.assertAlmostEqual(100, dist.getMean(), 10)
        quantile_values = dist.get_distribution_values()
        self.assertEqual(100, len(quantile_values))
        self.assertEqual(10000, sum(quantile_values))

        dist = LogNormal(1000, 100000, 0.5)
        self.assertAlmostEqual(100, dist.getMean(), 10)
        quantile_values = dist.get_distribution_values()
        self.assertEqual(1000, len(quantile_values))
        self.assertEqual(100000, sum(quantile_values))
        
        dist = LogNormal(10000, 1000000, 0.5)
        self.assertAlmostEqual(100, dist.getMean(), 10)
        quantile_values = dist.get_distribution_values()
        self.assertEqual(10000, len(quantile_values))
        self.assertEqual(1000000, sum(quantile_values))
        
        dist = LogNormal(100, 10000, 1.5)
        self.assertAlmostEqual(100, dist.getMean(), 10)
        quantile_values = dist.get_distribution_values()
        self.assertEqual(100, len(quantile_values))
        self.assertEqual(10000, sum(quantile_values))

        dist = LogNormal(1000, 100000, 1.5)
        self.assertAlmostEqual(100, dist.getMean(), 10)
        quantile_values = dist.get_distribution_values()
        self.assertEqual(1000, len(quantile_values))
        self.assertEqual(100000, sum(quantile_values))
        
        dist = LogNormal(10000, 1000000, 1.5)
        self.assertAlmostEqual(100, dist.getMean(), 10)
        quantile_values = dist.get_distribution_values()
        self.assertEqual(10000, len(quantile_values))
        self.assertEqual(1000000, sum(quantile_values))

    '''
    test text series generation
    '''
    def testTextSeries(self):
        series = TextSeries(10, 2000, 1)
        text_lens = map(lambda x: len(x), series.text_generator())
        list_text_lens = list(text_lens)
        self.assertEqual([38, 58, 78, 99, 123, 154, 194, 254, 358, 644], list_text_lens)
        self.assertEqual(2000, sum(list_text_lens))

        series = TextSeries(100, 30000, 1)
        text_lens = map(lambda x: len(x), series.text_generator())
        list_text_lens = list(text_lens)
        self.assertEqual(
            [18, 25, 30, 34, 37, 41, 44, 47, 50, 53, 56, 59, 62, 64, 67, 70, 73, 75, 78, 81, 84, 87, 89, 92, 95, 98, 101, 104, 107, 110, 113, 116, 120, 123, 126, 129, 133, 136, 140, 143, 147, 151, 155, 158, 162, 167, 171, 175, 179, 184, 188, 193, 198, 203, 208, 213, 218, 224, 230, 235, 241, 248, 254, 261, 268, 275, 283, 290, 299, 307, 316, 325, 335, 345, 356, 367, 379, 391, 405, 419, 434, 450, 467, 486, 506, 528, 552, 579, 608, 641, 679, 722, 772, 831, 905, 996, 1119, 1297, 1599, 2396],
            list_text_lens
        )
        self.assertEqual(30000, sum(list_text_lens))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
