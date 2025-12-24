from sklearn.tree import DecisionTreeClassifier
# sample dataset: [Age,Income]
x=[
    [25,50000],  # class 0
    [30,60000],  # class 0
    [35,70000],  # class 0
    [40,80000],  # class 0

    [45,90000],  # class 1
    [50,100000], # class 1
    [55,110000], # class 1
    [60,120000], # class 1

    [65,130000], # class 2
    [70,140000], # class 2
    [75,150000], # class 2
    [80,160000]  # class 2
]
# labels: 1=will buy, 0=will not buy
y=[0,1,1,0,1,1,0,1,1,0,1,0]  # Example output (not used in prediction)
#create the model
model = DecisionTreeClassifier()
# Train the model
model.fit(x, y)
# Predict for a new customer
new_customer = [[45, 90000]]  # Example input: [Age, Income]
prediction = model.predict(new_customer)
# Output the prediction
print("will buy" if prediction[0] == 1 else "will not buy")
# Predict the class labels for the new samples


####

