# @author: Vineet Rao

import pandas as pd

class Dataset:
    def __init__(self, src="dataset.csv", newSrc="Exoplanet-Elimination.csv"):
        self.src = src
        self.df = pd.read_csv(src, index_col=False)
        self.newSrc = newSrc


    def dedupe(self):
        # Sorts all the values in the dataset by discovery year
        self.df.sort_values('disc_pubdate', ascending=True)

        # Removing all the duplicates with the same name and same date
        self.df = self.df.drop_duplicates(subset=["pl_name"], keep="last")

        # for i in self.df.iterrows():
        #     print(i[1])
    
    
    # TODO: check all controversial flags, and remove entries w/ 1
    # TODO: NOT YET FULLY TESTED 
    def remove_controv_flags_of_1(self):
        self.df = self.df[self.df['pl_controv_flag'] != '1']

    def check_for_controv_flags_of_1(self):
        pass

    # TODO: used supervised learning w/ control planet of k218b and k23d
    def keplarian_mechanics(self):
        pass

    def export_csv(self):
        self.df.to_csv(self.newSrc)

if __name__ == "__main__":
    newDataset = Dataset(src='dataset.csv')
    newDataset.dedupe()
    newDataset.remove_controv_flags_of_1()
    newDataset.export_csv()