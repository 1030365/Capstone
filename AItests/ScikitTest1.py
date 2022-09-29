from sklearn.ensemble import RandomForestClassifier
X = [[0, 0], [1, 1]]
y = [0, 1]
clf = RandomForestClassifier(n_estimators=10)
clf.fit(X, Y)
