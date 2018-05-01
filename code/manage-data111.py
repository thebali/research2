import os
import pandas as pd

review_path = "data/digitalmusic/reviews/"

df = pd.read_json(review_path+"complete_reviews_Digital_Music.json", orient='records', lines=True)

df = df.to_csv(review_path+"complete_reviews_Digital_Music.csv")

# file = open(review_path, 'w')

print(df.head)






