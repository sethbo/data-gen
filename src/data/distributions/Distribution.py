'''
Created on Apr. 20, 2020

@author: scott
'''
from math import floor

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
        self.total = 0
        
    def calculateQuantileFunction(self, value):
        print('implement in sub-class')

    def getMean(self):
        print('implement in sub-class')

    def get_quantile_value(self, index):
        norm_index = (2 * index + 1) / (2 * self.quantity)
        dist_value = self.calculateQuantileFunction(norm_index)
        dist_int = int(dist_value + 0.5)
        self.total += dist_int
        return dist_int

    def get_quantile_values(self):
        return map(self.get_quantile_value, range(self.quantity))

    def get_distribution_values(self):
        self.total = 0
        quantile_values = list(self.get_quantile_values())
        diff = self.relationshipCount - self.total
        diff_quantity = divmod(diff, self.quantity)[1]
        adj_floor = int(floor(diff / self.quantity))
        def adjustment(text_len, index):
            if (index + diff_quantity >= self.quantity):
                return text_len + adj_floor + 1
            else:
                return text_len + adj_floor
        return list(map(adjustment, quantile_values, range(self.quantity)))
