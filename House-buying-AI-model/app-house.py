from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

# Load the saved model
model = joblib.load("model.pkl")

@app.route("/")
def home():
    return render_template("form.html")

@app.route("/predict", methods=["POST"])
def predict():
    age = int(request.form["age"])
    income = int(request.form["income"])
    prediction = model.predict([[age, income]])[0]
    result = "will buy a house" if prediction == 1 else "will not buy a house"
    return render_template("form.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)
# This code trains a Decision Tree model to predict house buying behavior based on age and income.
# The model is saved to a file named "model.pkl" for later use in a Flask web application.
# This code sets up a Flask web application that uses the trained model to predict whether a user   # will buy a house based on their age and income, displaying the result on a web page.