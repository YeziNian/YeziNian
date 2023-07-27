import numpy as np

import matplotlib.pyplot as plt

from sklearn import svm
import pandas as pd
import os
import tarfile
from six.moves import urllib

path = r"D:\Project\Practice\porject\housing.csv"
data = pd.read_csv(path)


d = [1, 2, 3, 21, 1, 2]

#print(np.random.permutation(len(d)))

binss = pd.IntervalIndex.from_tuples([(1, 2), (9, 10)])
da = pd.cut(np.array([1, 2, 3]), bins=[0.1, 1.1, 2.2, 3.3], labels=["A", "B", "C"], retbins=True)

pe = pd.DataFrame(np.arange(25).reshape(5, 5), index=list("abcde"), columns=list("ABCDE"))
"""print(pe)
print(pe.iloc[1])
print(pe.loc[:, "A"])

print(len(data.loc[data["total_bedrooms"] > 0, :]))
"""


