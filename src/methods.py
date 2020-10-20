import os
from functools import reduce
import pandas


def get_filedir(datatype,currentdir):
    if datatype == 'Counties':
        return currentdir + '/data/us-counties.csv'
    if datatype == 'States':
        return currentdir + '/data/us-states.csv'
    if datatype == 'US':
        return currentdir + '/data/us.csv'

def read_all(filedir): 
    return pandas.read_csv(filedir)

def over_200000(number):
    return number >= 200000

def death_over200000(data):
    return list(filter(over_200000, data['deaths']))

def average_cases(data):
    return reduce(lambda x,y : x+y, data['cases'])/(data.shape[0])

def print_list(data):
    print('Average case number would be',average_cases(data),'\n')
    print('First 10 rows in the dataset:')
    print(data[1:11],'\n')
    print('Death numbers over 200,000:')
    print(death_over200000(data))

