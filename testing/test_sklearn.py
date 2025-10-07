import sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

print("scikit-learn version:", sklearn.__version__)

X, y = load_iris(return_X_y=True)
clf = RandomForestClassifier(n_estimators=10, random_state=42)
clf.fit(X, y)
print("sample prediction:", clf.predict(X[:2]).tolist())
