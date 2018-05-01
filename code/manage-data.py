import os
import json
import pandas as pd

review_path = "data/digitalmusic/reviews/"
meta_path = "data/digitalmusic/meta/"

fileread = meta_path+"meta_Digital_Music.json"

# file = open(meta_path+"meta_Digital_Music.json")
# obj = json.load(file)

print(fileread)


df = pd.read_json(fileread, lines=True)

print(df.head())

# df = df.to_csv(meta_path+"small_meta_Digital_Music.csv")

# file = open(review_path, 'w')
