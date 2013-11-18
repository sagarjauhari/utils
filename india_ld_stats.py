# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 03:21:59 2013

@author: sagar
"""
from os.path import join
import matplotlib.pyplot as plt
import csv
from datetime import datetime
import numpy as np
from itertools import groupby

#local config
try:
    from dev_settings import *
except:
    pass


with open(join(INDIA_LD_DATA_URL, "IndiaLD_call_history.csv"), 'r') as fi:
    fr = csv.reader(fi, delimiter=',')
    header = next(fr)
    
    data=list(fr)
    day = [datetime.strptime(i[0], "%m/%d/%Y") for i in data]
    desc = [i[2][-12:] for i in data]
    mins = [int(i[4]) for i in data]
    
    top_nums = zip(* sorted([[key, len(list(group))] for key,group in \
                     groupby(sorted(desc))],key=lambda k:k[1], \
                     reverse=True)[0:2])[0]
    
    x=np.array(day)
    y=np.array(mins)
    for num in top_nums:
        idx=[i for i in range(len(data)) if desc[i]==num]
        plt.plot([day[i] for i in idx], [mins[i] for i in idx], label=num)

    plt.grid(True)
    plt.legend()
    plt.show()