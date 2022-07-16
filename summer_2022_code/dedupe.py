import pandas as pd

# Sorts all the values in the dataset by discovery year
df = pd.read_csv('dataset.csv', index_col=False)
df.sort_values('disc_pubdate', ascending=True)

# Removing all the duplicates with the same name and same date
df = df.drop_duplicates(subset=["pl_name"], keep="last")

# TODO: check all controversial flags, and remove entries w/ 1
# TODO: used supervised learning w/ control planet of k218b and k23d




# for i in df.iterrows():
#     print(i[1])

df.to_csv('Exoplanet_Deduped-1.csv')

#TODO: remove values with certain controversial flags
