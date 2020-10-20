from methods import get_filedir
from methods import read_all
from methods import print_list
import os
import inspect


dataType = input('Please type in the dataset you want to see (Counties, States, or US):')

path = os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))

print_list(read_all(get_filedir(dataType, path)))

