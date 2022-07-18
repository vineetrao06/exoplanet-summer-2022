import pandas as pd

df = pd.read_csv('dataset.csv', index_col=False)

# Sorts all the values in the dataset by discovery year
df.sort_values('disc_pubdate', ascending=True)

# Removing all the duplicates with the same name and same date
df = df.drop_duplicates(subset=["pl_name"], keep="last")

df2 = df.loc[df['pl_controv_flag'] != 1]

df2.reset_index(drop=True, inplace=False)

# Converts to csv and saves it in dataset "simplified-dataset.csv"
df2.to_csv('simplified-dataset.csv')
