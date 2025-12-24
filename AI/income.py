from sklearn.tree import DecisionTreeClassifier
x =[
    [25,50000],
    [35,60000],
    [45,80000],
    [20,30000],
    [50,100000],
    [23,40000],
    [70,70000]
]
# Labels for the income levels
y = [0, 1, 1, 0, 1, 0, 1]  # 0: low income, 1: medium income, 2: high income
# Create and train the Decision Tree Classifier
model= DecisionTreeClassifier()
model.fit(x, y)
#predict the income level for a new person
new_person = [[42, 120000]]  # Example: 28 years old, earning 55000
predicted_income_level = model.predict(new_person)
# Output the predicted income level
print("will buy a house" if predicted_income_level[0] == 1 else "will not buy a house")


