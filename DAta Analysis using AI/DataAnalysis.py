import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Step 1: Load data
data = {
    'Area (sqft)': [750, 800, 850, 900, 1000, 1100, 1200, 1300, 1400, 1500],
    'Price ($)': [150000, 160000, 170000, 180000, 200000, 220000, 240000, 260000, 280000, 300000]
}
df = pd.DataFrame(data)

# Step 2: Exploratory Data Analysis
print("Data Summary:\n", df.describe())
plt.scatter(df['Area (sqft)'], df['Price ($)'], color='blue')
plt.title('House Price vs Area')
plt.xlabel('Area (sqft)')
plt.ylabel('Price ($)')
plt.grid(True)
plt.show()

# Step 3: Model Training
X = df[['Area (sqft)']]  # Features
y = df['Price ($)']      # Target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
model = LinearRegression()
model.fit(X_train, y_train)

# Step 4: Predictions & Evaluation
y_pred = model.predict(X_test)
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))

# Step 5: Visualization of Prediction
plt.scatter(X_test, y_test, color='black', label='Actual')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Predicted')
plt.title('Test Data Prediction')
plt.xlabel('Area (sqft)')
plt.ylabel('Price ($)')
plt.legend()
plt.show()
