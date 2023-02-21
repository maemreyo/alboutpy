from sklearn.cluster import AgglomerativeClustering
import pandas as pd
import numpy as np

dataset = pd.DataFrame({
    'x': [11, 21, 28, 17, 29, 33, 24, 45, 45, 52, 51, 52, 55, 53,
          55, 61, 62, 70, 72, 10],
    'y': [39, 36, 30, 52, 53, 46, 55, 59, 63, 70, 66, 63, 58, 23,
          14, 8, 18, 7, 24, 10]
})

cluster = AgglomerativeClustering(n_clusters=2,
                                  affinity='euclidean', linkage='ward')
cluster.fit_predict(dataset)
