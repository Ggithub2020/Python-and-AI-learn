import pandas as pd
import numpy as np

np.random.seed(42)

# Sample size
n = 300

# Generate features
data = {
    'student_id': [f"S{1000+i}" for i in range(n)],
    'attendance_rate': np.round(np.random.normal(85, 10, n), 2).clip(50, 100),
    'average_grade': np.round(np.random.normal(75, 12, n), 2).clip(40, 100),
    'assignment_completion': np.round(np.random.normal(80, 15, n), 2).clip(30, 100),
    'discipline_incidents': np.random.poisson(1, n),
    'parental_engagement': np.random.choice(['High', 'Medium', 'Low'], n, p=[0.4, 0.4, 0.2]),
}

df = pd.DataFrame(data)

# Dropout logic (for simulation)
def calculate_dropout(row):
    score = 0
    if row['attendance_rate'] < 70: score += 1
    if row['average_grade'] < 60: score += 1
    if row['assignment_completion'] < 60: score += 1
    if row['discipline_incidents'] > 3: score += 1
    if row['parental_engagement'] == 'Low': score += 1
    return 'Yes' if score >= 2 else 'No'

df['dropout'] = df.apply(calculate_dropout, axis=1)

# Save
df.to_csv("student_data.csv", index=False)
print("Sample data saved as student_data.csv")
