# --- Data types ---
name = "Girum"           # string
age = 25                 # integer
daily_budget = 50.0      # float
expenses = []            # list to store expenses

print("Hello " + name + "!")  # String concatenation

# --- Input daily expenses ---
for i in range(3):  # loop 3 times (you can change to any number)
    item = input("Enter expense item: ")      # string
    amount = float(input("Enter amount: "))   # float
    expenses.append((item, amount))           # store as tuple in list

# --- Arithmetic: calculate total and remaining ---
total = 0
for item, amount in expenses:
    total += amount

remaining_budget = daily_budget - total

# --- Display results ---
print("\n--- Daily Expense Report ---")
for item, amount in expenses:
    print(item + ": $" + str(amount))  # concatenation with numbers

print("Total spent: $" + str(total))
print("Remaining budget: $" + str(remaining_budget))

# --- Optional: check if over budget ---
if remaining_budget < 0:
    print("You went over budget! 😱")
else:
    print("You are within budget. 👍")

today_expense =[{"item":"coffee", "amount":5.0}, {"item":"lunch", "amount":15.0}, {"item":"snacks", "]  amount":7.5}]
total_expense = sum(expense["amount"] for expense in today_expense)