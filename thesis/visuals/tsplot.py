import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set(color_codes=True)

data = pd.read_csv("trainingplot-matrixfact.csv")


plt.figure(figsize=(20,10))

# ax = sns.tsplot(data=data, interpolate=True, time="Iter.", value="RMSE")
sns.pointplot(x="Iter.", y="RMSE", data=data, palette="Blues_d")

plt.show()


# gammas = sns.load_dataset("gammas")
# print(gammas)
