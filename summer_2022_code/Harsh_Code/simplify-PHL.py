import pandas as pd

df = pd.read_csv('../data/PHL_DataSet.csv')

df2 = df['pl_name'].copy()

df2.to_csv('PHL-dataset-simplified.csv')
