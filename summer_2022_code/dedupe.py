import pandas as pd
import csv
import os
import numpy as np

df = pd.read_csv('dataset.csv', index_col=False)

# Sorts all the values in the dataset by discovery year
df.sort_values('disc_pubdate', ascending=True)

# Removing all the duplicates with the same name and same date
df = df.drop_duplicates(subset=["pl_name"], keep="last")

csv_header = list(df.columns.values)

df_to_np = df.to_numpy()

# testing:
# a = np.ones((2, 3))
# print(a)
# b = np.delete(a, 1, axis=0)
# print(b)

# print(df_to_np[254][32])
# print("length: " + str(len(df_to_np)))

# df_to_np = np.delete(df_to_np, 254, axis=0)
# print("new length: " + str(len(df_to_np)))

print(df_to_np[0][1])

print("length: " + str(len(df_to_np)))
arr_length = len(df_to_np)

for i in range(0, arr_length ):
    if (i == arr_length):
        break

    pl_name = df_to_np[i][1]
    pl_controv_flag = df_to_np[i][32]

    if (pl_controv_flag == 1):
        print(pl_name, "has a conversial flag of 1")
        # print(df_to_np[i][32])
        df_to_np = np.delete(df_to_np, i, axis=0)
        print("new length: " + str(len(df_to_np)))
        arr_length -= 1
        print('arr_length: ' + str(arr_length))


df = pd.DataFrame(df_to_np, columns = csv_header)

df.to_csv('simplified-dataset.csv')




