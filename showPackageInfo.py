# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 08:54:47 2023

@author: Eric
"""

import pip
import sys
import re

from contextlib import redirect_stdout
import io
from operator import itemgetter



def showInfo(package):
   f = io.StringIO()
   with redirect_stdout(f):
    if hasattr(pip, 'main'):
        result = pip.main(['show', package])
        result = f.getvalue()
    else:
        result = pip._internal.main(['show', package])
        result = f.getvalue()
    tokens = result.split("\n")
    kvl = []
    for t in tokens:
        keyValue = t.split(": ")
        if len(keyValue) > 1:
            d = {keyValue[0]:keyValue[1]}
            kvl.append(d)
    return kvl

# Example
if __name__ == '__main__':
    result = showInfo('glob2')[2]['Summary']
   
   
        