# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 17:41:18 2018

@author: doktor
"""

import random
import time
i=1

open('testfile.txt','w').close()

for i in range(1000):
    randomdata = open('testfile.txt','a')
    i = i+random.randint(2,3)
    r_num = random.randint(2,20)
    randomdata.write("%5.2f,%5.2f\n" % (i,r_num))
    randomdata.close()
    print('%',i)
    time.sleep(1)