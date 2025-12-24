from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier 

# Load the iris dataset
iris = load_iris()  
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42) 
#Train model
clf= RandomForestClassifier()
clf.fit(x_train, y_train)
#test model
accuracy = clf.score(x_test, y_test)    
print(f"Accuracy: {accuracy * 100:.2f}%")  # Print the accuracy of the model
# Predict on a new sample


#your own data
x = [
    [5.1, 3.5, 1.4, 0.2],  # class 0
    [4.9, 3.0, 1.4, 0.2],  # class 0
    [4.7, 3.2, 1.3, 0.2],  # class 0
    [5.0, 3.6, 1.4, 0.2],  # class 0

    [7.0, 3.2, 4.7, 1.4],  # class 1
    [6.4, 3.2, 4.5, 1.5],  # class 1
    [6.9, 3.1, 4.9, 1.5],  # class 1
    [5.5, 2.3, 4.0, 1.3],  # class 1

    [6.3, 3.3, 6.0, 2.5],  # class 2
    [5.8, 2.7, 5.1, 1.9],  # class 2
    [7.1, 3.0, 5.9, 2.1],  # class 2
    [6.3, 2.9, 5.6, 1.8]
  ]  # class 2 # Example input
y = [1, 1, 1, 1,
     0, 1, 0, 1,
     1, 1, 1, 1] # Example output (not used in prediction)
#split the data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
# Predict the class labels for the new samples
#Train model
clf =RandomForestClassifier()
clf.fit(x_train, y_train)

#Test model
accuracy = clf.score(x_test, y_test)
print(f"Accuracy: {accuracy * 100:.2f}%")  # Print the
