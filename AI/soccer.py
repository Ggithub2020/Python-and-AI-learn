from sklearn.tree import DecisionTreeClassifier

# Sample match data
X = [
    [5, 20, 2.3, 1.8],  # Top team vs lower team → win
    [8, 10, 1.8, 1.6],  # Close match → win
    [15, 5, 1.5, 1.2],  # Lower team vs top team → lose
    [7, 25, 2.0, 2.5],  # Mid vs weak → win
    [30, 8, 0.9, 1.1],  # Weak vs strong → lose
    [10, 18, 1.7, 1.9], # Close match → win
    [18, 12, 1.1, 1.3], # Mid vs mid → lose
    [2, 6, 2.5, 1.1],   # Top team → win
    [20, 9, 1.2, 1.0],  # Lower vs strong → lose
    [12, 12, 1.5, 1.5], # Equal teams → draw/lose
]

# Target outcomes (1 = Team A wins, 0 = does not win)
y = [1, 1, 0, 1, 0, 1, 0, 1, 0, 0]

# Train the model
model = DecisionTreeClassifier()
model.fit(X, y)

# New prediction
# Team A rank 6, opponent rank 14, Team A avg goals = 2.1, opponent concedes avg = 1.7
new_match = [[6, 14, 2.1, 1.7]]
prediction = model.predict(new_match)

# Output result
print("Team A is Likely to Win" if prediction[0] == 1 else "Team A May Not Win")
