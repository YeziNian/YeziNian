import numpy as np
from sklearn.ensemble import RandomForestClassifier
with open(r"C:\Users\40437\Desktop\data.txt", "r") as fp:
    lie = []
    label = []
    data = fp.readline().split()
    while data:
        lie.append(np.array(list(map(lambda x: eval(x), data[:4]))))
        label.append(int(data[4]))
        data = fp.readline().split()

clf = RandomForestClassifier(n_estimators=4, max_depth=2, random_state=0)
clf.fit(lie, label)

from sklearn.tree import export_graphviz
import graphviz

for num, tree in enumerate(clf.estimators_):
    dot_data = export_graphviz(tree, out_file=None,
                               feature_names=["he", "asd", "asdsd", "sadaq"],
                               class_names=["0", "1"],
                               filled=True, rounded=True,
                               special_characters=True)

    graph = graphviz.Source(dot_data)
    graph.render(f"decision_tree{num}")
print(clf.predict(lie))
