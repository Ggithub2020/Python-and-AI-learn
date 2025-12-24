from sklearn.tree import DecisionTreeClassifier

# Features: [Age, Annual Premium ($), Number of Accidents, Smoker (1/0)]
X = [
    [25, 300, 0, 0],
    [45, 600, 2, 1],
    [30, 450, 1, 0],
    [50, 700, 0, 1],
    [60, 800, 3, 0]
]

# Labels: 1 = Will File Claim, 0 = Will Not File
y = [0, 1, 0, 1, 1]

# Train the model
model = DecisionTreeClassifier()
model.fit(X, y)

# Predict for a new customer
new_customer = [[42, 120000, 0, 0]]
prediction = model.predict(new_customer)

print("Will file a claim" if prediction[0] == 1 else "Will not file a claim")
