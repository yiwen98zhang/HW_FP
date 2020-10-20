import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
src_dir = os.path.join(parent_dir,'src')
sys.path.insert(0,src_dir)

import pytest
from methods import read_all
from methods import get_filedir


def test_get_dir_is_not_none():
    a = get_filedir('US',parent_dir)
    assert a is not None

def test_read_results_is_not_none():
    a = read_all('/Volumes/SamsungTF/study/Statistical_Computing/HW_FP/FP/data/us.csv')
    b = read_all('/Volumes/SamsungTF/study/Statistical_Computing/HW_FP/FP/data/us-states.csv')
    c = read_all('/Volumes/SamsungTF/study/Statistical_Computing/HW_FP/FP/data/us-counties.csv')
    assert len(a)>0
    assert b is not None
    assert c is not None





    