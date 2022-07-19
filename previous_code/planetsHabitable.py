import csv

import numpy as np
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

data = pd.read_csv('exoFinal.csv', low_memory=False)
# Change the planet name as necessary. index_location is an integer that stores the location of the control planet
index_location = data['pl_name'][data['pl_name'] == 'GJ 581 c'].index[0]
# Gets the whole control planet and saves as a 1 row dataframe
control_planet = data.loc[index_location].copy()

columns = ['pl_name', 'habitable']

planets = []


def check_all(t, s, e, l, d, dM, oP):
    try:
        if pd.isna(t):
            #             # print(t)
            return False
        if pd.isna(s):
            #             # print(s)
            return False
        if pd.isna(e):
            #             # print(e)
            return False
        if pd.isna(l):
            #             # print(l)
            return False
        if pd.isna(d):
            #             # print(d)
            return False
        if pd.isna(dM):
            #             # print(dM)
            return False
        if pd.isna(oP):
            #             # print(oP)
            return False
        return True
    except:
        return False


def calculate(teff, lum):
    sRunawayG = 1.107
    caRunawayG = 1.332e-4
    cbRunawayG = 1.580e-8
    ccRunawayG = -8.308e-12
    cdRunawayG = -1.931e-15

    sMaximumG = 0.356
    caMaximumG = 6.171e-5
    cbMaximumG = 1.698e-9
    ccMaximumG = -3.198e-12
    cdMaximumG = -5.575e-16

    RunawayG = sRunawayG + caRunawayG * (teff - 5780) + cbRunawayG * math.pow(teff - 5780, 2) + ccRunawayG * math.pow(
        teff - 5780, 3) + cdRunawayG * math.pow(teff - 5780, 4)
    RunawayG = ((round((RunawayG - math.floor(RunawayG)) * 10000)) / 10000) + math.floor(RunawayG)
    MaximumG = sMaximumG + caMaximumG * (teff - 5780) + cbMaximumG * math.pow(teff - 5780, 2) + ccMaximumG * math.pow(
        teff - 5780, 3) + cdMaximumG * math.pow(teff - 5780, 4)
    MaximumG = ((round((MaximumG - math.floor(MaximumG)) * 1000)) / 1000) + math.floor(MaximumG)

    RunawayGdis = math.sqrt(lum / RunawayG)
    RunawayGdis = ((round((RunawayGdis - math.floor(RunawayGdis)) * 1000)) / 1000) + math.floor(RunawayGdis)
    MaximumGdis = math.sqrt(lum / MaximumG)
    MaximumGdis = ((round((MaximumGdis - math.floor(MaximumGdis)) * 1000)) / 1000) + math.floor(MaximumGdis)
    return [RunawayGdis, MaximumGdis]


def inCHZ(sM, e, t, l):
    try:
        semiMinor = sM * math.sqrt(1 - pow(e, 2))
        chzBounds = calculate(t, l)
        if semiMinor > chzBounds[0] and semiMinor < chzBounds[1]:
            # print(current + " is within CHZ")
            return True
        else:
            # print(current + " is not within CHZ")
            return False
    except:
        # print(current + " missing too many values")
        return False


def keplerian(d,dM,e,oP):
    if (d >= 4) and (d <= 7):
        if ('Transit' in dM) or ('Radial' in dM):
            if e <= 0.2:
                if np.abs(float(oP) - float(control_planet['pl_orbper'])) <= 50:
                    return True
    return False


for i in range(0, len(data)):
    current = data['pl_name'][i]
    temperature = data['st_teff'][i]
    # print(temperature)
    semiMajor = data['pl_orbsmax'][i]
    # print(semiMajor)
    eccentricity = data['pl_orbeccen'][i]
    # print(eccentricity)
    luminosity = data['st_lum'][i]
    # print(luminosity)
    density = data['pl_dens'][i]
    # print(density)
    discoveryMethod = data['discoverymethod'][i]
    # print(discoveryMethod)
    orbitalPeriod = data['pl_orbper'][i]
    # print(orbitalPeriod)

    message = ""

    if check_all(temperature, semiMajor, eccentricity, luminosity, density, discoveryMethod, orbitalPeriod):
        if inCHZ(semiMajor, eccentricity, temperature, luminosity):
            if keplerian(density,discoveryMethod,eccentricity,orbitalPeriod):
                message = "yes"
            else:
                message = "no (failed Keplerian)"
        else:
            message = "no (not in CHZ)"
    else:
        message = "no (missing values)"
        # print(current+" missing too many values")
    planets.append({'pl_name': current, 'habitable': message})
    print("Checked: "+current)

with open('habitable.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=columns)
    writer.writeheader()
    writer.writerows(planets)
