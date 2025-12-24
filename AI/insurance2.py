from sklearn.tree import DecisionTreeClassifier

# Features: [Age, Premium, Accidents, Smoker, BMI, Married, Credit Score]
X = [
    [25, 300, 0, 0, 22.5, 0, 700],
    [45, 600, 2, 1, 30.2, 1, 620],
    [30, 450, 1, 0, 25.0, 0, 710],
    [50, 700, 0, 1, 29.0, 1, 640],
    [60, 800, 3, 0, 26.3, 1, 600],
    [35, 400, 0, 0, 24.0, 1, 750],
    [40, 500, 1, 1, 28.5, 0, 670],
    [55, 720, 2, 1, 31.0, 1, 590]
]

# Labels: 1 = Will file claim, 0 = Will not file
y = [0, 1, 0, 1, 1, 0, 1, 1]

# Create and train the model
model = DecisionTreeClassifier()
model.fit(X, y)

# Predict for a new customer
# [Age, Premium, Accidents, Smoker, BMI, Married, Credit Score]
new_customer = [[42, 550, 1, 1, 27.8, 1, 680]]
prediction = model.predict(new_customer)

# Output result
print("🚨 Will file a claim" if prediction[0] == 1 else "✅ Will not file a claim")
