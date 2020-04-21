'''
Generate Lorem ipsum text based on the log-normal distribution for a given number of notes and total characters.
 
Created on Apr. 15, 2020

@author: scott
'''
import lorem

from data.distributions.LogNormal import LogNormal
from data.distributions.Burr import Burr

class TextSeries(object):
    def __init__(self, num_notes, num_characters, logn_variance):
        self.num_notes = num_notes
        self.num_characters = num_characters
        self.logn_variance = logn_variance
        self.distribution = LogNormal(num_notes, num_characters, logn_variance)
        self.distribution_values = self.distribution.get_distribution_values()
        self.total_length = 0
        self.index = 0
    
    def text_generator(self):
        while self.index < self.num_notes:
            text = lorem.text()
            text_len = self.distribution_values[self.index]
            while (len(text) < text_len): 
                text = text + " " + lorem.text()
            yield text[0:text_len]
            self.index += 1

dist = Burr(100, 200, 3, 1)
rows = dist.get_distribution_rows()
print(list(rows))
print(dist.getMean())