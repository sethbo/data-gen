'''
Generate Lorem ipsum text based on the log-normal distribution for a given number of notes and total characters.
 
Created on Apr. 15, 2020

@author: scott
'''

from math import exp, sqrt
from data.utils.erf import erf_inverse
from data.distributions.LogNormal import LogNormal

num_notes = 1000
num_characters = 100000
logn_mean = 6
logn_stdev = 1

'''
From normalized value generate length of text from quantile function of log-normal distribution
Make text with Lorem ipsum generator
'''

d = LogNormal(num_notes, num_characters, logn_stdev)
total_length = 0

for text_len in d.getQuantileValues():
    # Normalize an index into values for each note where 0 < v_i < 1
    #norm_index = (2 * index + 1) / (2 * num_notes)
    #dist_value = d.calculateQuantileFunction(norm_index)
    total_length += text_len
    #text_length = exp(dist_value)
    #print("\tindex\t%d\tnidx\t%f\tvalue\t%f" %(index, norm_index, dist_value))
print("total %f" %(total_length))

