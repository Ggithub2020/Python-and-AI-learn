from sklearn.tree import DecisionTreeClassifier

# Sample dataset: [Temperature, Humidity, Windy, Rainy]
X = [
    [22, 85, 0, 1],  # Rainy, high humidity, not windy -> Yes
    [25, 80, 1, 1],  # Rainy, windy -> Yes
    [30, 70, 0, 0],  # Clear, warm -> No
    [21, 90, 0, 1],  # Rainy, not windy, humid -> Yes
    [28, 60, 0, 0],  # Hot and dry -> No
    [26, 75, 1, 0],  # Cloudy, windy, not rainy -> No
    [24, 88, 1, 1],  # Rainy, humid, windy -> Yes
    [20, 95, 0, 1],  # Cold, very humid, rainy -> Yes
    [29, 65, 0, 0],  # Warm, moderate humidity -> No
    [23, 85, 1, 0],  # Humid but not rainy -> No
]

# Labels: 1 = Carry Umbrella, 0 = Don’t Carry
y = [1, 1, 0, 1, 0, 0, 1, 1, 0, 0]

# Create and train the model
model = DecisionTreeClassifier()
model.fit(X, y)

# Predict for a new day's weather condition
new_day = [[23, 90, 0, 1]]  # Cool, high humidity, not windy, rainy
prediction = model.predict(new_day)

# Output
print("Carry Umbrella" if prediction[0] == 1 else "No Need for Umbrella")
