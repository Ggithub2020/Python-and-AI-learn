# --- Data types ---
name = "Alice"          # string
age = 25                # integer
daily_goal_minutes = 60 # float: daily exercise goal in minutes
exercises = []          # list to store exercises

print("Hello " + name + "! Let's track your exercises today.\n")

# --- Input today's exercises ---
num_exercises = int(input("How many exercises today? "))

for i in range(num_exercises):
    exercise = input("Enter exercise name: ")     # string
    duration = float(input("Enter duration (minutes): "))  # float
    exercises.append((exercise, duration))       # store as tuple

# --- Arithmetic: total exercise time ---
total_duration = 0
for exercise, duration in exercises:
    total_duration += duration

remaining_goal = daily_goal_minutes - total_duration

# --- Display results ---
print("\n--- Today's Exercise Report ---")
for exercise, duration in exercises:
    print(exercise + ": " + str(duration) + " minutes")

print("Total exercise time: " + str(total_duration) + " minutes")
print("Remaining goal: " + str(remaining_goal) + " minutes")

# --- Optional: check if goal reached ---
if remaining_goal <= 0:
    print("Great job! You reached your daily exercise goal! 💪")
else:
    print("Keep going! You need " + str(remaining_goal) + " more minutes to reach your goal.")

