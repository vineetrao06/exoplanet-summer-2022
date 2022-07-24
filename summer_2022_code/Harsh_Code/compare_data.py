# Compares data from habitable-planets.csv and PHL-dataset-simplified.csv

import pandas as pd
import numpy as np

our_planets = pd.read_csv('habitable-planets.csv')['pl_name'].to_numpy()
phl_planets = pd.read_csv('PHL-dataset-simplified.csv')['pl_name'].to_numpy()

np.sort(our_planets)
np.sort(phl_planets)

print(our_planets)
print(phl_planets)

stringVal = "HD"
our_planets = [
    our_planet for our_planet in our_planets if stringVal not in our_planet]

print(our_planets)

num_similar_planets = 0

for our_planet in our_planets:
    our_planet = our_planet[:-2]

    for phl_planet in phl_planets:
        phl_planet = phl_planet[:-2]
        if (our_planet == phl_planet):
            num_similar_planets += 1

print(num_similar_planets)
print("Accuracy: " + str(pcnt_accuracy))


# print(our_planets)
# print(phl_planets)

# comparison_column = np.where(
#     df_our_dataset["pl_name"] == df_nasa_PHL["pl_name"], True, False)

# print(comparison_column)
