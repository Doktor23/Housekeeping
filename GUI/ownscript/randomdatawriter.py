# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 17:41:18 2018

@author: doktor
"""

import random
import time
import math
i=1

open('testfile.txt','w').close()

for i in range(1000):
    randomdata = open('testfile.txt','a')
    r_num = random.randint(2,20)*math.sin(2*math.pi*i/20)
    randomdata.write("%5.2f,%5.2f\n" % (i,r_num))
    randomdata.close()
    print('%',i)
    time.sleep(1)