import pandas as pd
import numpy as np

# UPDATE 8/16: Added Aaryan's code to determine if planet is in it's star's habitable zone
# 13 planets orbit M-type stars and are in the star's habitable zone > 7 planets with density 4-7 > 

# UPDATE 8/15: Incorporated Hrithik's code for orbital period and eccentricity
# Currently, +-15 for orbital period and +-0.2 for eccentricity yields one match other than K2-18b, K2-3 d
# Still figuring out how to incorporate habitable zone calculations

# UPDATE 8/08: From what I can tell, most if not all planets with M*sin(i) values in 'pl_bmassj' do NOT have a 'pl_orbincl' value
# But for some reason, my code is not able to match 'Msini' in the 'pl_bmassj' column

# TODO: ADD MORE ATTRIBUTES TO MATCH TO K2-18 b (semi-major and minor axes, orbital period, eccentricity, etc.)
# So far, the only accounted attributes are spectral type and density

# TODO: Look into 'pl_bmassj', it has 1747 values, while 'pl_massj' only has 966 values
# Only caveat is that 'pl_bmassj' has mass measured in diff ways (check column definitions)

# url = 'https://raw.githubusercontent.com/allench36/NASA-Caltech-Exoplanet-Archive/master/updatedexoplanet.csv'

url = "planets_2020.07.23_16.01.35"
exo = pd.read_csv(url)

pd.set_option('display.max_columns', None, 'display.max_rows', None)
pd.options.mode.chained_assignment = None

# Variables needed for K2-18b
K2orbperiod = exo['pl_orbper'][1093]
K2eccentricity = exo['pl_orbeccen'][1093] 
K2dist = exo['st_dist'][1093]

# create new dataframe for planets with jupiter radii value, mass value, and no density value
new_exo_mass = exo.loc[(exo['pl_dens'].isnull()) & (exo['pl_radj'].notnull()) & (exo['pl_massj'].notnull())]
# filter original dataframe for planets with density value
exo = exo.loc[exo['pl_dens'].notnull()]

# calculate densities for child dataframe
new_exo_mass['pl_dens'] = (new_exo_mass['pl_massj'] * (1.898 * (10 ** 27) * 1000)) \
/ (4 * np.pi * ((new_exo_mass['pl_radj'] * 43441 * 160934) ** 3) / 3)

# append everything into 'total_dens'
total_dens = exo.append(new_exo_mass, ignore_index=True)

# create child with 'pl_orbper' value
total_y_orbper = total_dens.loc[total_dens['pl_orbper'].notnull()]
# create child with no 'pl_orbper' and 'pl_ratdor' but with 'pl_orbsmax'
total_n_orbper = total_dens.loc[(total_dens['pl_orbper'].isnull()) & (total_dens['pl_ratdor'].isnull()) & (total_dens['pl_orbsmax'].notnull())]

# calculate 'pl_orbper' for planets without it
total_n_orbper['pl_orbper'] = np.sqrt(total_n_orbper['pl_orbsmax']**3) * 365

# append all child dataframes into 'total_orbper'
total_orbper = total_y_orbper.append(total_n_orbper, ignore_index=True)

# filter out planets without 'pl_orbeccen' value
total = total_orbper.loc[total_orbper['pl_orbeccen'].notnull()]

# filter by matching K2-18b (M-type host star, density between 4 and 7 g/cm^3, no controversy, discovered via transit, less than 38 pc away, eccentricity 0.2 or less)
total = total.loc[(total['st_spstr'].str.startswith('M', na=False)) & (total['pl_dens'] >= 4) & (total['pl_dens'] <= 7) 
& (total['pl_controvflag'] == 0) & (total['pl_discmethod'].str.contains('Transit', na=False)) & (total['st_dist'] <= K2dist) 
& (total['pl_orbeccen'] <= 0.2)] 
# & (np.abs(total['pl_orbper'] - K2orbper) <= 15)

# calculate star's habitable zone
total = total.loc[(total['st_optmag'].notnull()) & (total['st_dist'].notnull()) & (total['pl_orbsmax'].notnull())]
total['abs_mag'] = total['st_optmag'] - 5 * np.log(total['st_dist'] / 10)
total['bolo_mag'] = total['abs_mag'] - 2.0
total['abs_lum'] = 10**((total['bolo_mag'] - 4.72) / -2.5)
total['inner_bound'] = np.sqrt(total['abs_lum'] / 1.1)
total['outer_bound'] = np.sqrt(total['abs_lum'] / 0.53)

# calculate semi-minor axis 
total['pl_orbsmin'] = total['pl_orbsmax']**2 - (total['pl_orbeccen'] * total['pl_orbsmax'])**2
# check if planet is located in habitable zone
total = total.loc[(total['pl_orbsmax'] > total['inner_bound']) & (total['pl_orbsmax'] < total['outer_bound']) 
& (total['pl_orbsmin'] > total['inner_bound']) & (total['pl_orbsmin'] < total['outer_bound'])]
total.reset_index(drop=True, inplace=True)

# print out planets matching the criteria excluding K2-18 b
# total = total.loc[total['pl_name'] != 'K2-18 b']
print(total['pl_name'])
print(total['pl_orbeccen'])
print(total['pl_orbper'])
print(total['pl_eqt'])
