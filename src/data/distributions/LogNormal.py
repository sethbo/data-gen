'''
Created on Apr. 16, 2020

@author: scott

Log-normal distribution with quantile function to generate values for data generation

'''
from math import exp, sqrt, log
from data.utils.erf import erf_inverse
from data.distributions.Distribution import Distribution

class LogNormal(Distribution):
    '''
    classdocs
    '''

    def __init__(self,  quantity, relationshipCount, variance):
        '''
        Constructor
        
        quantity - the number or quantity of relationships
        relationshipCount - the total number of relationships
        variance - the vairance of the log-normal distribution
        '''
        Distribution.__init__(self, quantity, relationshipCount)
        self.mean = log(relationshipCount / quantity) - variance / 2
        self.variance = variance
        self.stdev = sqrt(variance)
        
    def calculateQuantileFunction(self, value):
        erf_value = 2 * value - 1
        erfi_value = erf_inverse(erf_value)
        return exp(self.mean + (self.stdev * sqrt(2) * erfi_value))

    def getMean(self):
        return exp(self.mean + self.variance / 2)