import calendar
import datetime
import math
import string
import sys
import textwrap
from datetime import date
from math import pi
import os.path
from os import listdir
from os.path import isfile, join
import platform
import site
from stat import ST_CTIME, ST_MODE, S_ISREG
from subprocess import call
import multiprocessing
import cProfile
import getpass
import time
import textwrap
import os.path
import functools
import glob
from operator import itemgetter
import re
import itertools
from heapq import nlargest
from statistics import mean

import numpy as np
import pandas as pd
import re
import json
# !/usr/bin/python
import datetime

# class Student:
#     def __init__(self, firstName, lastName):
#         self.firstName = firstName
#         self.lastName = lastName
#
#
# s1 = Student("Autumn", "Ma")
# print(json.dumps(s1.__dict__))
# dic ={
#   "id": "04",
#   "name": "sunil",
#   "department": "HR"
# }
import pandas as pd
import textwrap

import string


import sys
import re
pattern = '^a...s$'
test = 'abbss'
result = re.match(pattern, test)
if result:

    print('pass')
else:
    print('failed')
print(sys.path)




# Brute Force solution: linear search algorithm--> compare one by one
def locate_card(card):
    position = 0
    while position < len(card['input']['card']):
        if card['input']['card'][position] == card['input']['query']:
            return position
        position +=1
        if position == len(card['input']['card']):
            return -1
    return -1


tests = [{'input': {
    'card': [3, 6, 4, 7, 8],
    'query': 17
    },
    'output': 3},
    {'input': {
        'card': [3, 6, 4, 7, 8],
        'query': 6
    },
    'output': 1},
    {'input': {
        'card': [],
        'query': 4
    },
    'output': 1}
]

for test in tests:
    query = test['input']['query']
    if (locate_card(test) == test['output']):
        position = test['output']
        print(f'Found position: {position} for queried number {query}')
    else:
        print(f'Not found positionfor queried number {query}')

