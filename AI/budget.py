from sklearn.tree import DecisionTreeClassifier

# Data: [Income, Expenses, Family Size]
X = [
    [3000, 3200, 1],  # overspending
    [4000, 3500, 2],  # within budget
    [5000, 2000, 2],  # saving well
    [6000, 6000, 3],  # overspending
    [4500, 3000, 3],  # within budget
    [7000, 2500, 2],  # saving well
    [3500, 4000, 1],  # overspending
    [5500, 4200, 4],  # within budget
    [8000, 3000, 2],  # saving well
    [6000, 7000, 2],  # overspending
    [5000, 4000, 3],  # within budget
    [7500, 2000, 3],  # saving well
]

# Labels: 0 = Overspending, 1 = Within Budget, 2 = Saving Well
y = [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2]

# Train the model
model = DecisionTreeClassifier()
model.fit(X, y)

# Predict a new scenario
# Example: Income $5000, Expenses $3500, Family of 3
new_input = [[6200, 5000, 5]]
prediction = model.predict(new_input)

# Interpret the prediction
if prediction[0] == 0:
    print("You are Overspending")
elif prediction[0] == 1:
    print("You are Within Budget")
else:
    print("You are Saving Well")
