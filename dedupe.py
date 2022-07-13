import pandas as pd

# Sorts all the values in the dataset by discovery year
df = pd.read_csv('dataset.csv', index_col=False)
df.sort_values('disc_year', ascending=True)

# Removing all the duplicates with the same name and same date
df = df.drop_duplicates(subset=["pl_name"], keep="last")
df.to_csv('Exoplanet_Deduped.csv')
