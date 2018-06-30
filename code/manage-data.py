import json
import pandas as pd

filelocation = "./data/amazon5core/cellphone/"
# filelocation = "./data/amazon5core/healthcare/"

file = pd.read_json(filelocation+"Cell_Phones_and_Accessories_5.json", lines=True)
# file = pd.read_json(filelocation+"Health_and_Personal_Care_5.json", lines=True)

file = file[["asin", "reviewerID", "overall", "reviewText"]]
file = file.dropna()
file = file.sample(frac=1, random_state=23) # frac=0.75   for 75% of the row in the data
file.to_csv(filelocation+"cellphone5core.csv", sep=",", encoding='utf-8')

