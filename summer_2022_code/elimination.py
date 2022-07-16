# @author: Vineet Rao

import pandas as pd

class dataset:
    def __init__(self, src="dataset.csv"):
        self.src = src

    def dedupe():
        # Sorts all the values in the dataset by discovery year
        df = pd.read_csv('dataset.csv', index_col=False)
        df.sort_values('disc_pubdate', ascending=True)

        # Removing all the duplicates with the same name and same date
        df = df.drop_duplicates(subset=["pl_name"], keep="last")

        # for i in df.iterrows():
        #     print(i[1])
    
    
    # TODO: check all controversial flags, and remove entries w/ 1
    def check_controversial_flags():
        pass

    # TODO: used supervised learning w/ control planet of k218b and k23d
    def keplarian_mechanics():
        pass

    def export_csv():
        df.to_csv('Exoplanet_Deduped-1.csv')

