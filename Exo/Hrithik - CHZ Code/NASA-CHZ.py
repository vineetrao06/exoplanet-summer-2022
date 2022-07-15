'''
                # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
                #                                                                                     #
                #    Author: Hrithik Pai                                                              #
                #    Created: November 4th, 2020                                                      #
                #    Language: Python                                                                 #
                #    Description: This code calculates the CHZ of the planets from the NASA Database. #
                #                 It prints the planets that are inside the CHZ of the host star.     #
                #                                                                                     # 
                # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  
'''

import pandas as pd
import numpy as np
from scipy.constants import pi
np.seterr(divide = 'ignore')



exo = pd.read_csv('Exoplanet_Data.csv', low_memory=False) # Need to replace with file path if the CSV file is not in the same folder as code

for i in range (len(exo['st_lum'])): 
    if pd.isna(exo['st_lum'][i]) or exo['st_lum'][i][0:1]=="[" or exo['st_lum'][i][0:1]=="<" or exo['st_lum'][i][0].isalpha():
        exo = exo.drop([i])
exo = exo.reset_index(drop = True)

exo['st_lum'] = pd.to_numeric(exo['st_lum'])

exo['st_lum'] = exo['st_lum'] * (3.828*(10**26))

for i in range (len(exo['sy_dist'])): 
    if pd.isna(exo['sy_dist'][i]) or exo['sy_dist'][i][0:1]=="[" or exo['sy_dist'][i][0:1]=="<" or exo['sy_dist'][i][0].isalpha():
        exo = exo.drop([i])
exo = exo.reset_index(drop = True)
exo['sy_dist'] = pd.to_numeric(exo['sy_dist'])

bolometric_luminosity = exo['st_lum']/(4*pi*exo['sy_dist']*exo['sy_dist'])

for i in range (len(bolometric_luminosity)): 
    if bolometric_luminosity[i]<=0:
        exo = exo.drop([i])
exo = exo.reset_index(drop = True)

bolometric_mag = -2.5 * np.log10(bolometric_luminosity)

for i in range (len(exo['st_teff'])): 
    if pd.isna(exo['st_teff'][i]) : 
        exo = exo.drop([i])
exo = exo.reset_index(drop = True)
exo['st_teff'] = pd.to_numeric(exo['st_teff'])
exo['st_spectype'] = exo['st_spectype'].astype(str)

# BC = Bolometic Correction Constant
for i in range (len(exo['st_teff'])):
    BC = 0
    if (exo['st_teff'][i] >= 2400 and exo['st_teff'][i] <=3700) or exo['st_spectype'][i][0]=='M':
        BC = -2.0
    elif (exo['st_teff'][i] >= 3700 and exo['st_teff'][i] <=5200) or exo['st_spectype'][i][0]=='K':
        BC = -0.8
    elif (exo['st_teff'][i] >= 5200 and exo['st_teff'][i] <=6000) or exo['st_spectype'][i][0]=='G':
        BC = -0.4
    elif (exo['st_teff'][i] >= 6000 and exo['st_teff'][i] <=7500) or exo['st_spectype'][i][0]=='F':
        BC = -0.15
    elif (exo['st_teff'][i] >= 7500 and exo['st_teff'][i] <=10000) or exo['st_spectype'][i][0]=='A':
        BC = -0.3
    elif (exo['st_teff'][i] >= 10000 and exo['st_teff'][i] <=30000) or exo['st_spectype'][i][0]=='B':
        BC = -2.0
    bolometric_mag[i] = bolometric_mag[i] + BC
    
abs_lum = 10**((bolometric_mag-4.72)/-2.5)

inner_boundary = np.sqrt(abs_lum/1.1)
outer_boundary = np.sqrt(abs_lum/0.53)

exo['pl_orbsmax'] = pd.to_numeric(exo['pl_orbsmax'])
for i in range (len(exo['pl_orbsmax'])): 
    axis = exo['pl_orbsmax'][i]
    if (axis < inner_boundary[i]) | (axis > outer_boundary[i]):
        exo = exo.drop([i])
exo = exo.reset_index(drop = True) 
print(exo['pl_name'])
