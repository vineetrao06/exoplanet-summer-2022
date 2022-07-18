import pandas as pd
import numpy as np

df = pd.read_csv('dataset.csv', low_memory=False)

store = pd.DataFrame(columns=list(df.columns))
sort = pd.DataFrame(columns=list(df.columns))
data = [[np.nan] * len(df.columns)]
final_planet = pd.DataFrame(data, columns=list(df.columns))

exo_deduped = pd.DataFrame(columns=list(df.columns))

def dedup(): 
    index = 0
    sort = store.sort_values(by=['disc_year'], ascending=False) 
    sort = sort.reset_index (drop = True)
    
    
    # Iterate through columns
    for x in range (len(sort.columns)): 
        
        # Iterate through data in a column
        for y in range (len(sort)): 
            
            if not pd.isna(sort.iloc[:,x][y]): 
                final_planet.iloc[:,index][0] = sort.iloc[:,x][y] 
                break
        
        index +=1
                
    global exo_deduped  
    exo_deduped = exo_deduped.append(final_planet, ignore_index = True)
    final_planet.loc[0] = np.nan
    

start_index = 0
stop_index = 0
i = 0
while (i<len(df)-1):
    start_index = i
    stop_index = i
    while (df['pl_name'][i] == df['pl_name'][i+1]):
        stop_index+=1
        i+=1
    # The 'store' dataframe has a bulk of similar planets    
    store = df.iloc[start_index:(stop_index + 1)]
    
    dedup()
    
    i+=1
   
exo_deduped.to_csv (r'NASA_Deduped.csv', index = False, header=True)