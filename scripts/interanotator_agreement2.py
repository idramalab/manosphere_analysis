import statsmodels.stats.inter_rater
import pandas as pd
import numpy as np

df = pd.read_csv("../helpers/other_label.csv")

df_correct = pd.DataFrame(columns=[str(i) for i in range(5)])

table = []

for idx, vs in df.iterrows():
    tmp = np.zeros(5)
    for v in vs.values[1:]:
        print(v)
        tmp[v-1] += 1
    table.append(tmp)

print(table)

print("Fleiss Kappa:", statsmodels.stats.inter_rater.fleiss_kappa(table))
#
# # Fleiss Kappa: 0.9120129815534144
