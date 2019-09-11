import statsmodels.stats.inter_rater
import pandas as pd
import numpy as np

df = pd.read_csv("../labels_all.csv")
df_correct = pd.DataFrame(columns=[str(i) for i in range(7)])

table = []

for idx, vs in df.iterrows():
    tmp = np.zeros(7)
    for v in vs.values[1:-1]:
        tmp[v] += 1
    table.append(tmp)

print("Fleiss Kappa:", statsmodels.stats.inter_rater.fleiss_kappa(table))

# Fleiss Kappa: 0.9120129815534144
