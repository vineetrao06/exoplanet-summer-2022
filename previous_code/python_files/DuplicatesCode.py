# Necessary Import Statements
import pandas as pd
import numpy as np


df = pd.read_csv('Nasa_Full.csv', low_memory=False)
nasa = df[['rowid', 'pl_name','hostname','pl_letter','hd_name','hip_name','tic_id', 
             'discoverymethod', 'disc_year', 'pl_controv_flag', 'pl_orbeccen', 'pl_rade',
            'st_spectype', 'pl_dens', 'pl_radj', 'pl_massj', 'pl_orbsmax', 'pl_ratdor', 
            'st_rad', 'pl_orbper']]


# To store the bulk of planets
store = pd.DataFrame(columns=list(nasa.columns))

# To store the planets once they have been organized by discovery year
sort = pd.DataFrame(columns=list(nasa.columns))

# To store the final Deduped planet
final_planet = pd.DataFrame(data, columns=list(nasa.columns))

# A dataframe to store all the deduped planets
exo_deduped = pd.DataFrame(columns=list(nasa.columns))


# Dedupe method (Does all the dedupe work)
def dedup(): 
    
    # Index variable to count which column we are on in final_planet
    index = 0
    
    # Sort the bulk of planets by discovery year and save the order to the 'sort' dataframe
    sort = store.sort_values(by=['disc_year'], ascending=False) 
    sort = sort.reset_index (drop = True)
    
    
    # Iterate through columns in sort dataframe
    for x in range (len(sort.columns)): 
        
        # Iterate through data in a column
        for y in range (len(sort)): 
            
            # If the value is not NA (There is a value), then store the value to the final_planet's respective column
            if not pd.isna(sort.iloc[:,x][y]): 
                final_planet.iloc[:,index][0] = sort.iloc[:,x][y] 
                break
        
        index +=1
    
    # Add the deduped planet to the dataframe that stores all the deduped planets
    global exo_deduped  
    exo_deduped = exo_deduped.append(final_planet, ignore_index = True)
    final_planet.loc[0] = np.nan
    

# This code is to find the bulk of similar planets    
start_index = 0
stop_index = 0
i = 0
while (i<len(nasa)):
    start_index = i
    stop_index = i
    while (i<len(nasa) and nasa['pl_name'][i] == nasa['pl_name'][start_index]):
        stop_index+=1
        i+=1
    # The 'store' dataframe has a bulk of similar planets    
    store = nasa.iloc[start_index:stop_index]
    
    
    dedup()
    
    
exo_deduped.to_csv (r'Exoplanet_Deduped.csv', index = False, header=True)