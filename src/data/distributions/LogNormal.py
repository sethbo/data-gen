'''
Created on Apr. 16, 2020

@author: scott
'''
from math import exp, sqrt, log
from data.utils.erf import erf_inverse

class Distribution(object):
    '''
    classdocs
    '''

    def __init__(self, quantity, relationshipCount):
        '''
        Constructor
        '''
        self.quantity = quantity
        self.relationshipCount = relationshipCount
        
    def calculateQuantileFunction(self, value):
        print('implement in sub-class')
    
    def getQuantileValues(self):
        # TODO - can we use map here?
        values = list()
        for index in range(self.quantity):
            # Normalize an index into values for each note where 0 < v_i < 1
            norm_index = (2 * index + 1) / (2 * self.quantity)
            dist_value = self.calculateQuantileFunction(norm_index)
            values.append(int(dist_value + 0.5))
    
        return values

class LogNormal(Distribution):
    '''
    classdocs
    '''

    def __init__(self, quantity, relationshipCount, stdev):
        '''
        Constructor
        '''
        Distribution.__init__(self, quantity, relationshipCount)
        self.stdev = stdev
        # mean of log normal distribution is derived from the mean of the distribution and the log normal standard deviation
        self.mean = log(self.relationshipCount / self.quantity) - self.stdev / 2
        
    def calculateQuantileFunction(self, value):
        erf_value = 2 * value - 1
        return exp(self.mean + (self.stdev * sqrt(2) * erf_inverse(erf_value)))

