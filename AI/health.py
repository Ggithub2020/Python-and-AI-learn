from sklearn.tree import DecisionTreeClassifier

# Sample data: [Age, Blood Pressure, Cholesterol Level, Smoker (1=yes, 0=no)]
X = [
    [45, 130, 220, 1],
    [50, 140, 180, 0],
    [38, 120, 160, 1],
    [60, 150, 240, 1],
    [55, 135, 200, 0]
]

# Labels: 1 = At Risk, 0 = Not At Risk
y = [1, 0, 1, 1, 0]

# Create and train model
model = DecisionTreeClassifier()
model.fit(X, y)

# New patient data
new_patient = [[52, 145, 230, 1]]
prediction = model.predict(new_patient)

print("At Risk" if prediction[0] == 1 else "Not At Risk")
