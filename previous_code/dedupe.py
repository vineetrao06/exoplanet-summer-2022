import pandas as pd
import numpy as np
import csv

data = pd.read_csv('may22.csv', low_memory=False)

# columns will be the columns to dedupe
# this can be changed by specifying which columns to download from the dataset online
# The columns planet name and controversial flag are required for operation
columns = data.columns

# planets is a dict that holds the name of a planet and a list of every index it appears in
planets = {}

# planetsFinal is a list that holds dicts that will hold all final values for the dataset
planetsFinal = []

# returns all values in the dataset for a given planet
def getAll(pos):
    values = {}
    for x in columns:
        # ignores all planets with the controversial flag
        if x != 'pl_controv_flag':
            values[x] = data[x][pos]
    return values


# fills in planets with index that they appear at
for i in range(0, len(data)):
    current = data['pl_name'][i]
    # if the given planet is already in planets
    if current in planets:
        planets[current].append(i)

    # if the given planet is not already in planets
    else:
        planets[current] = [i]

# dedupe process
for name in planets:
    # grab all indexes of given
    indexes = planets[name]
    # final is the dict that will eventually be added to the planetsFinal list
    final = {}

    # loop through all indexes of the given planet
    for i in indexes:
        # read the usage of functions at the given function
        temp = getAll(i)
        # on first run through all places in the dictionary must be initialized
        if len(final) == 0:
            final = temp
        # on ever subsequent run through the dedupe process begins
        else:
            # loop through all values (planet properties I guess?)
            for j in final:
                ins = final[j]
                # To make sure both values are actually numbers
                if (type(final[j]) is np.float64) and (type(temp[j]) is np.float64):
                    if pd.isna(temp[j]) and not pd.isna(final[j]):
                        ins = final[j]
                    elif pd.isna(final[j]) and not pd.isna(temp[j]):
                        ins = temp[j]
                    else:
                        # Take median
                        ins = np.median([temp[j], final[j]])
                else:
                    if pd.isna(temp[j]):
                        ins = final[j]
                    elif pd.isna(final[j]):
                        ins = temp[j]
                    else:
                        # if they are not numbers and not the same text the value will be replaced with "disputed"
                        if temp[j] != final[j]:
                            ins = "disputed"
                final[j] = ins
    planetsFinal.append(final)
    print("Deduped: " + name)

with open('exoFinal.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=planetsFinal[0].keys())
    writer.writeheader()
    writer.writerows(planetsFinal)
