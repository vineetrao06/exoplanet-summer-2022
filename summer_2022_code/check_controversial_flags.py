import csv
import pd

filename = 'simplified-dataset.csv'



    



# '''

# import csv

# lines = list()
# with open('dataset.csv', 'r') as readFile:
#     reader = csv.reader(readFile)
#     for row in reader:
#         lines.append(row)
#         if row[32] == "1":
#             lines.remove(row)

# with open('without-controv-flags.csv', 'w') as writeFile:
#     writer = csv.writer(writeFile)
#     writer.writerows(lines)

# with open('without-controv-flags.csv', 'w') as input, open('without-controv-flags-2.csv', 'w', newline='') as output:
#      writer = csv.writer(output)
#      for row in csv.reader(input):
#          if any(field.strip() for field in row):
#              writer.writerow(row)



# rows_to_remove = list()

# with open('without-controv-flags.csv', 'r') as csvfile:
#     df = csv.reader(csvfile)
#     # print(df)

#     # Getting a list of all the rows to remove
#     for row in df:
#         pl_name = row[1]
#         controv_flag = row[32]
#         # print(row)
#         if (controv_flag == "1"):
#             print(pl_name + " has controversial flag of 1")
#             # Getting the row index value
#             rows_to_remove.append(int(row[0]) - 1)



# df = df[df['Team'] != 'C']
