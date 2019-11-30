# WIP: This is not complete
#
# A script to train a model on previous winning lotto numbers
# and attempt use that model to predict future winning numbers

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv('data/numbers.csv', header=None)

X = df[[x for x in range(3)]]
y = df[[x for x in range(3, 52)]]

X = pd.get_dummies(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = RandomForestClassifier(n_estimators=100)

multi_target_forest = MultiOutputClassifier(model, n_jobs=-1)
multi_target_forest.fit(X_train, y_train)
y_predict = multi_target_forest.predict(X_test)

multi_target_forest.score(y_test.values, y_predict)
