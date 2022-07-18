#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 10:20:47 2022

@author: harshambardekar
"""

import pandas as pd

df = pd.read_csv('deduped.csv')

df2= df.loc[df['pl_controv_flag'] != 1]

df2.reset_index(drop = True, inplace = False)

df2.to_csv('no_controv_flags.csv')


