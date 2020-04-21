'''
Created on Apr. 16, 2020

@author: scott

Burr distribution for data generation

'''
from math import pow
from data.distributions.utils import beta
from data.distributions.Distribution import Distribution

class Burr(Distribution):
    '''
    classdocs
    '''

    def __init__(self,  quantity, relationshipCount, cParameter, kParameter):
        '''
        Constructor
        
        quantity - the number or quantity of relationships
        relationshipCount - the total number of relationships
        cParameter - the c shape parameter of the Burr distribution
        kParameter - the k shape parameter of the Burr distribution
        lambdaParameter - the scaling parameter of the Burr distribution
        '''
        Distribution.__init__(self, quantity, relationshipCount)
        self.cParameter = cParameter
        self.kParameter = kParameter
        self.lambdaParameter = (self.relationshipCount / self.quantity) / self.kParameter / beta((self.kParameter - 1 / self.cParameter), (1 + 1 / self.cParameter))
        
    def calculateQuantileFunction(self, value):
        return self.lambdaParameter * pow((pow((1 - value), (-1 / self.kParameter)) - 1),  1 / self.cParameter)

    def getMean(self):
        return self.lambdaParameter * self.kParameter * beta(self.kParameter - 1 / self.cParameter, 1 + 1 / self.cParameter)
