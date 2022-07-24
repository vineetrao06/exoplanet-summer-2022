# -*- coding: utf-8 -*-
"""K_Type_Habitable.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GrL7AJU-cSW4kVgvhNINtYXEI9fkw0Q0
"""

# Necessary Import Statements
import pandas as pd
import numpy as np

# Imports the datasets
data = pd.read_csv('~/ASDRP/Data/Exoplanet_Data.csv', low_memory=False)
phl = pd.read_csv('~/ASDRP/Data/PHL_Dataset.csv', low_memory=False)

# Removes any planets that have an NA eccentricity value
data = data[data['pl_orbeccen'].notna()]
data = data[data['pl_rade'].notna()]

# Resets the data row index
data = data.reset_index(drop=True)

# Makes an empty m_type dataframe with same column headers
k_type = pd.DataFrame(columns=list(data.columns))

# Makes an empty m_type_habitable dataframe to store planets that result out of this code
k_type_habitable = pd.DataFrame(columns=list(data.columns))

# Fills the m_type dataframe with M-type host stars' planets
k_type = data.loc[(data['st_spectype'].str.startswith('K', na=False))]

# Resets the m_type row index
k_type = k_type.reset_index(drop=True)

# Takes out planets that have no planet radius and eccentricity
phl = phl[phl['pl_rade'].notna()]
phl = phl[phl['pl_orbeccen'].notna()]

# Resets index
phl = phl.reset_index(drop=True)

# Makes a new empty dataframe for the m-type planets in the PHL dataset
phl_k_type = pd.DataFrame(columns=list(phl.columns))

# Fills the empty dataframe with m-type planets from the PHL dataset
phl_k_type = phl.loc[(phl['st_spectype'].str.startswith('K', na=False))]

# Resets index
phl_k_type = phl_k_type.reset_index(drop=True)


def check_match(planet, control_planet):
    if pd.isna(planet['pl_dens']):
        if (not pd.isna(planet['pl_radj'])) & (not pd.isna(planet['pl_massj'])):
            planet['pl_dens'] = (planet['pl_massj'] * (1.898 * (10 ** 27) * 1000)) \
                                / (4 * np.pi * ((planet['pl_radj'] * 43441 * 160934) ** 3) / 3)
        else:
            return

    if pd.isna(planet['pl_orbsmax']) and (pd.isna(planet['pl_ratdor']) or pd.isna(planet['st_rad'])):
        return

    # Calculates orbital period in days for main planet
    if pd.isna(planet['pl_orbper']):
        if pd.isna(planet['pl_ratdor']):
            planet['pl_orbper'] = np.sqrt(planet['pl_orbsmax'] ** 3) * 365
        elif not pd.isna(planet['st_rad']):
            planet['pl_orbper'] = np.sqrt((planet['pl_ratdor'] * planet['st_rad']) ** 3) * 365
        if pd.isna(planet['pl_orbper']):
            return

    if pd.isna(control_planet['pl_orbsmax']) and (
            pd.isna(control_planet['pl_ratdor']) or pd.isna(control_planet['st_rad'])):
        return

    # Calculates orbital period in days for phl planet
    if pd.isna(control_planet['pl_orbper']):
        if pd.isna(control_planet['pl_ratdor']):
            control_planet['pl_orbper'] = np.sqrt(control_planet['pl_orbsmax'] ** 3) * 365
        elif not pd.isna(control_planet['st_rad']):
            control_planet['pl_orbper'] = np.sqrt((control_planet['pl_ratdor'] * control_planet['st_rad']) ** 3) * 365
        if pd.isna(control_planet['pl_orbper']):
            return

    if pd.isna(planet['pl_orbeccen']):
        return

    if (float(planet['pl_dens']) >= 4) & (float(planet['pl_dens']) <= 7):
        if (planet['pl_controv_flag'] == '0'):
            if ('Transit' in planet['discoverymethod']):
                if (planet['pl_orbeccen'] <= 0.2):
                    if (np.abs(float(planet['pl_orbper']) - float(control_planet['pl_orbper'])) <= 50):
                        global k_type_habitable
                        k_type_habitable = k_type_habitable.append(planet, ignore_index=True)


for i in range(len(k_type['pl_rade'])):
    current_dist = np.abs(phl_k_type['pl_rade'][0] - k_type['pl_rade'][i])
    if current_dist < 20:
        planet = k_type.loc[i].copy()
        control_planet = phl_k_type.loc[0].copy()
        check_match(planet, control_planet)

print(k_type_habitable)
