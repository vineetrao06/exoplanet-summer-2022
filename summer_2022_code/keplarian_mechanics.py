import csv

import pandas as pd
import math

"""
Code and equations taken from:
"Habitable Zones Around Main-Sequence Stars: New Estimates" by Kopparapu et al.(2013), Astrophysical Journal, 765, 131
https://arxiv.org/abs/1301.6674
"Habitable Zones Around Main-Sequence Stars: Dependence on Planetary Mass" by Kopparapu et al.(2014), Astrophysical Journal Letters, 787, L29
http://arxiv.org/abs/1404.5292
http://depts.washington.edu/naivpl/sites/default/files/hz_0.shtml#overlay-context=content/hz-calculator
"""

data = pd.read_csv('Exoplanet-Elimination.csv', low_memory=False)

columns = ['pl_name', 'habitable']

planets = []

def check_all(t,s,e,l):
    if pd.isna(t):
        return False
    if pd.isna(s):
        return False
    if pd.isna(e):
        return False
    if pd.isna(l):
        return False
    return True

def calculate (teff, lum):
    sRunawayG  = 1.107
    caRunawayG = 1.332e-4
    cbRunawayG = 1.580e-8
    ccRunawayG = -8.308e-12
    cdRunawayG = -1.931e-15

    sMaximumG = 0.356
    caMaximumG = 6.171e-5
    cbMaximumG = 1.698e-9
    ccMaximumG = -3.198e-12
    cdMaximumG = -5.575e-16

    RunawayG = sRunawayG + caRunawayG*(teff-5780) + cbRunawayG*math.pow(teff-5780,2) + ccRunawayG*math.pow(teff-5780,3) + cdRunawayG*math.pow(teff-5780,4)
    RunawayG = ((round((RunawayG - math.floor(RunawayG))*10000))/10000) + math.floor(RunawayG)
    MaximumG = sMaximumG + caMaximumG*(teff-5780) +cbMaximumG*math.pow(teff-5780,2) +ccMaximumG*math.pow(teff-5780,3) +cdMaximumG*math.pow(teff-5780,4)
    MaximumG = ((round((MaximumG - math.floor(MaximumG))*1000))/1000) + math.floor(MaximumG)

    RunawayGdis = math.sqrt(lum/RunawayG)
    RunawayGdis = ((round((RunawayGdis - math.floor(RunawayGdis))*1000))/1000) + math.floor(RunawayGdis)
    MaximumGdis = math.sqrt(lum/MaximumG)
    MaximumGdis = ((round((MaximumGdis - math.floor(MaximumGdis))*1000))/1000) + math.floor(MaximumGdis)
    return [RunawayGdis, MaximumGdis]

for i in range(0, len(data)):
    current = data['pl_name'][i]
    temperature = data['st_teff'][i]
    semiMajor = data['pl_orbsmax'][i]
    eccentricity = data['pl_orbeccen'][i]
    luminosity = data['st_lum'][i]
    if(check_all(temperature,semiMajor,eccentricity,luminosity)):
        try:
            semiMinor = semiMajor*math.sqrt(1-pow(eccentricity,2))
            chzBounds = calculate(temperature, luminosity)
            if(semiMinor>chzBounds[0] and semiMinor<chzBounds[1]):
                print(current+" is within CHZ")
                planets.append({'pl_name': current, 'habitable': 'yes'})
            # else:
            #     print(current + " is not within CHZ")
            #     planets.append({'pl_name': current, 'habitable': 'no'})
        except:
            print(current+" missing too many values")
            # planets.append({'pl_name': current, 'habitable': 'no (missing values)'})
    # else:
    #     print(current+" missing too many values")
    #     planets.append({'pl_name': current, 'habitable': 'no (missing values)'})

# print(planets)

def trim(dataset):
    trim = lambda x: x.strip() if type(x) is str else x
    print(type(dataset.applymap(trim)))
    return dataset.applymap(trim)

# newWriter = [trim(pd.read_csv('habitable-5.csv'))]
# print(newWriter)

with open('habitable-5.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = columns)
    # writer.writeheader()
    # writer.writerow({'pl_name': 'Baked', 'habitable': 'Beans'})
    # writer.writerow({'pl_name': 'Lovely', 'habitable': 'Spam'})
    # writer.writerow({'pl_name': 'Wonderful', 'habitable': 'Spam'})
    
    writer.writerows(planets)

    
