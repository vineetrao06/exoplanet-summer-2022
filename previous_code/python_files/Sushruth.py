#!/usr/bin/env python
# coding: utf-8
​
# In[35]:
​
​
import pandas as pd
import numpy as np
import array
import math
Gplanet = pd.read_csv("/Users/sushruth/Downloads/Copy of Data Set #1 planets_2019.06.06_15.41.16 - planets_2019.06.06_15.41.16-2.csv")
Gstar = pd.read_csv("/Users/sushruth/Downloads/Copy of Data Set #1 planets_2019.06.06_15.41.16 - HZ zone for stars.csv")
pd.set_option('display.max_rows', None)
for i in range(0, 1597):
    indice = (Gstar.loc[Gstar.StellarName==Gplanet.loc[i,'pl_hostname']].index) 
    app_mag = Gplanet.loc[i,'st_optmag']
    st_dist = Gplanet.loc[i,'st_dist'] / 10
    st_dist = math.log(st_dist, 10)
    abs_mag = app_mag- 5* st_dist
    st_spstr = Gplanet.loc[i,'st_spstr']
    print()
    bol_const = abs_mag-0.4 # replace this -0.4 with whatever value goes with your star type.
    L_star = 10**((bol_const - 4.72)/(-2.5))
    inner = math.sqrt(L_star/1.1)
    outer = math.sqrt(L_star/0.53)
    #print(Gplanet.loc[i,'pl_hostname'])
    #print(inner)
    #print(outer)
    if Gplanet.loc[i,'pl_orbsmax'] < inner or Gplanet.loc[i, 'pl_orbsmax'] >outer:
        Gplanet = Gplanet.drop([i])
results = Gplanet.to_csv(r'/Users/sushruth/Desktop/ASDRP/TypeGPlanetBiology.csv', index = None, header = True)         
display(Gplanet)