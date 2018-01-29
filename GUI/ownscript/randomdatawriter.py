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
open('HSrandom.txt','w').close()
open('HSvolt.txt','w').close()
open('HStemperature.txt','w').close()

for i in range(1000):
    randomdata = open('testfile.txt','a')
    r_num = random.randint(2,30)*math.sin(2*math.pi*i/10)
    randomdata.write("%5.2f,%5.2f\n" % (i,r_num))
    randomdata.close()
    print('%',i)
    randomdata3 = open('HSrandom.txt','a')
    r_num = random.randint(2,30)*math.cos(2*math.pi*i/20)
    randomdata3.write("%5.2f,%5.2f\n" % (i,r_num))
    randomdata3.close()
    print('%',i)
    randomdata2 = open('HSvolt.txt','a')
    r_num = random.randint(2,30)*math.sin(2*math.pi*i/20)
    randomdata2.write("%5.2f,%5.2f\n" % (i,r_num))
    randomdata2.close()
    print('%',i)
    randomdata1 = open('HStemperature.txt','a')
    r_num = random.randint(2,30)*math.cos(2*math.pi*i/10)
    randomdata1.write("%5.2f,%5.2f\n" % (i,r_num))
    randomdata1.close()
    print('%',i)
    time.sleep(10)