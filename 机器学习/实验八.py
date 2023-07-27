import numpy as np
from sklearn.naive_bayes import MultinomialNB
data = np.genfromtxt('ss.csv', delimiter=',', dtype=None, names=True)
Data = []
for n in data:
    Data.append(np.array(list(n)[:4]))
Data = np.array(Data)
label = np.array([0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1])

clf = MultinomialNB(alpha=0.1)
clf.fit(Data, label)
d = np.array([26, 1, 0, 1])
y_pred = clf.predict(np.array([d]))
print(y_pred)