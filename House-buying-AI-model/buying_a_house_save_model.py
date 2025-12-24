from sklearn.tree import DecisionTreeClassifier
import joblib

# Training data
x = [
    [25,50000],
    [35,60000],
    [45,80000],
    [20,30000],
    [50,100000],
    [23,40000],
    [70,70000]
]
y = [0, 1, 1, 0, 1, 0, 1]  # 0: will not buy, 1: will buy

# Train model
model = DecisionTreeClassifier()
model.fit(x, y)

# Save the trained model
joblib.dump(model, "model.pkl")
