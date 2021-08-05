from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np

data = pd.read_csv("study_result.csv", header=None)
x_train, y_train = data.iloc[:, 2:], data.iloc[:, 1]

classifier = KNeighborsClassifier(n_neighbors = 3)

classifier.fit(x_train, y_train)
sample = np.array(x_train.iloc[200, :]).reshape(1, -1)
print(classifier.predict(sample))