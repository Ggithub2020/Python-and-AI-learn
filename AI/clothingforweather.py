from sklearn.tree import DecisionTreeClassifier

# Sample data: [Temperature, Wind Speed, Time of Day]
X = [
    [30, 5, 1],   # Hot afternoon → light clothes
    [28, 10, 0],  # Warm morning → light clothes
    [22, 15, 1],  # Moderate temp → moderate clothes
    [18, 20, 2],  # Cool evening → warm clothes
    [10, 25, 0],  # Cold windy morning → warm clothes
    [25, 5, 2],   # Pleasant evening → moderate clothes
    [16, 18, 1],  # Cool and breezy → warm clothes
    [20, 10, 1],  # Mild day → moderate clothes
    [32, 8, 2],   # Very warm → light clothes
    [12, 30, 0],  # Cold and windy morning → warm clothes
]

# Labels: 0 = Light, 1 = Moderate, 2 = Warm
y = [0, 0, 1, 2, 2, 1, 2, 1, 0, 2]

# Create and train the model
model = DecisionTreeClassifier()
model.fit(X, y)

# Predict for a new weather condition
# Example: 21°C, 12 km/h wind, Morning
new_scenario = [[21, 12, 0]]
prediction = model.predict(new_scenario)

# Interpret prediction
if prediction[0] == 0:
    print("Wear Light Clothes (T-shirt, shorts)")
elif prediction[0] == 1:
    print("Wear Moderate Clothes (Shirt, jeans)")
else:
    print("Wear Warm Clothes (Jacket, sweater)")
