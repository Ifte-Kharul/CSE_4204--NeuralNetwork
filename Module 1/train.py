import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
# from matplotlib.colors import ListedCOlormap
# cmap = ListedCOlormap()

df = pd.read_csv('diabetes.csv')

x = df.drop(['Outcome'], axis=1)
y = df['Outcome']

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=1)

plt.figure()
plt.scatter(x[:, 2], X[:, 3], s=20)
plt.show()
