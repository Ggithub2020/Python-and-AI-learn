# This script defines four basic arithmetic functions: Add, subtract, multiply, and divide.
# Each function takes two numbers as arguments and prints the result of the operation.


def Add(num1, num2):
    print(num1 + num2)

def subtract(num1, num2):
    print(num1 - num2)

def multiply(num1, num2):
    print(num1 * num2)

def divide(num1, num2):
    print(num1 / num2)

# # Example usage of the functions
print(Add(10, 25))  # Output: 35
print(subtract(10, 25))  # Output: -15
print(multiply(10, 25))  # Output: 250  
print(divide(10, 25))  # Output: 0.4
# # Note: The print statements in the example usage will print None because the functions do not return a value.


def greet():
    return("Hello, welcome to the calculator functions!")
print(greet())  # Output: Hello, welcome to the calculator functions!


def process_order(order_items, tax_rate=0.07, discount_threshold=100, discount_rate=0.10):
    """
    Calculate the total price for an order.

    Args:
      order_items (list of dict): Each dict has 'item', 'quantity', 'price_per_unit'.
      tax_rate (float): Tax rate to apply to subtotal.
      discount_threshold (float): Minimum subtotal to qualify for discount.
      discount_rate (float): Discount percentage applied if threshold met.

    Returns:
      dict: Breakdown with subtotal, discount, tax, and total.
    """

# #🛒 Example: Process Customer Order and Calculate Total with Discounts & Taxes
def process_order(order_items, tax_rate=0.07, discount_threshold=100, discount_rate=0.10):
    subtotal = 0
    print("\nCalculating your order:\n")
    for item in order_items:
        item_total = item['quantity'] * item['price_per_unit']
        print(f"Adding {item['quantity']} x {item['item']} at ${item['price_per_unit']:.2f} each: ${item_total:.2f}")
        subtotal += item_total

    discount = 0
    if subtotal > discount_threshold:
        discount = subtotal * discount_rate
        print(f"\nSubtotal exceeds ${discount_threshold}, applying discount of {discount_rate*100}%: -${discount:.2f}")

    taxable_amount = subtotal - discount
    tax = taxable_amount * tax_rate
    total = taxable_amount + tax

    print(f"\nSubtotal: ${subtotal:.2f}")
    print(f"Discount: -${discount:.2f}")
    print(f"Tax (@{tax_rate*100}%): ${tax:.2f}")
    print(f"Total: ${total:.2f}")

    return {
        "subtotal": subtotal,
        "discount": discount,
        "tax": tax,
        "total": total
    }

def get_order_from_user():
    order_items = []
    print("Enter your order items. Type 'done' when finished.\n")
    while True:
        item_name = input("Item name: ").strip()
        if item_name.lower() == 'done':
            break
        try:
            quantity = int(input("Quantity: ").strip())
            price = float(input("Price per unit: ").strip())
        except ValueError:
            print("Invalid input. Please enter numeric values for quantity and price.\n")
            continue
        order_items.append({
            "item": item_name,
            "quantity": quantity,
            "price_per_unit": price
        })
        print()  # blank line for readability
    return order_items

# # Main execution
order = get_order_from_user()

if order:
    result = process_order(order)
    print("\nOrder Summary:", result)
else:
    print("No items entered. Exiting.")
 








# # 🕒 Example: Calculate Employee Weekly Pay with Overtime and Taxes
# python
# Copy
# Edit
def calculate_pay(work_log, hourly_rate, overtime_rate=1.5, overtime_threshold=40, tax_rate=0.20):
    total_hours = sum(work_log)
    regular_hours = min(total_hours, overtime_threshold)
    overtime_hours = max(total_hours - overtime_threshold, 0)

    regular_pay = regular_hours * hourly_rate
    overtime_pay = overtime_hours * hourly_rate * overtime_rate
    gross_pay = regular_pay + overtime_pay
    tax = gross_pay * tax_rate
    net_pay = gross_pay - tax

    print(f"\nTotal Hours Worked: {total_hours:.2f}")
    print(f"Regular Hours: {regular_hours:.2f} at ${hourly_rate}/hr = ${regular_pay:.2f}")
    print(f"Overtime Hours: {overtime_hours:.2f} at ${hourly_rate} * {overtime_rate} = ${overtime_pay:.2f}")
    print(f"Gross Pay: ${gross_pay:.2f}")
    print(f"Tax Deducted (@{tax_rate*100}%): ${tax:.2f}")
    print(f"Net Pay: ${net_pay:.2f}")

    return {
        "total_hours": total_hours,
        "regular_hours": regular_hours,
        "overtime_hours": overtime_hours,
        "gross_pay": gross_pay,
        "tax": tax,
        "net_pay": net_pay
    }

def get_work_hours():
    print("Enter hours worked each day for the week (7 days).")
    work_log = []
    for i in range(1, 8):
        while True:
            try:
                hours = float(input(f"Day {i} hours: ").strip())
                if hours < 0:
                    print("Hours cannot be negative. Try again.")
                    continue
                work_log.append(hours)
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
    return work_log

def get_hourly_rate():
    while True:
        try:
            rate = float(input("Enter hourly pay rate: ").strip())
            if rate < 0:
                print("Rate cannot be negative. Try again.")
                continue
            return rate
        except ValueError:
            print("Invalid input. Please enter a number.")

# # Main program
hours_worked = get_work_hours()
rate = get_hourly_rate()
pay_summary = calculate_pay(hours_worked, rate)

print("\nPay Summary:", pay_summary)










# Appointment Booking Without Any Libraries
# python
# Copy
# Edit
# Store appointments as a list of dictionaries
appointments = []

def time_to_minutes(time_str):
    # Converts 'HH:MM' to total minutes
    hours, minutes = map(int, time_str.split(":"))
    return hours * 60 + minutes

def is_conflict(new_start, new_end):
    for appt in appointments:
        existing_start = time_to_minutes(appt['start'])
        existing_end = time_to_minutes(appt['end'])
        if (new_start < existing_end) and (new_end > existing_start):
            return True
    return False

def book_appointment(client_name, date, start_time, duration_minutes):
    new_start = time_to_minutes(start_time)
    new_end = new_start + duration_minutes

    if is_conflict(new_start, new_end):
        print(f"⚠️ Conflict! {client_name}'s appointment at {start_time} on {date} overlaps with an existing one.")
        return False

    appointments.append({
        "client": client_name,
        "date": date,
        "start": start_time,
        "end": minutes_to_time(new_end)
    })

    print(f"✅ Appointment booked for {client_name} on {date} from {start_time} to {minutes_to_time(new_end)}")
    return True

def minutes_to_time(minutes):
    # Converts total minutes back to 'HH:MM' format
    h = minutes // 60
    m = minutes % 60
    return f"{h:02}:{m:02}"

def show_schedule():
    if not appointments:
        print("\nNo appointments scheduled.")
        return
    print("\n📋 Current Schedule:")
    for appt in appointments:
        print(f"- {appt['client']} on {appt['date']} from {appt['start']} to {appt['end']}")

# # Main input loop
print("📆 Simple Appointment Scheduler")
while True:
    name = input("\nEnter client name (or 'done' to exit): ").strip()
    if name.lower() == 'done':
        break

    date = input("Enter date (YYYY-MM-DD): ").strip()
    time = input("Enter start time (HH:MM): ").strip()
    try:
        duration = int(input("Enter duration in minutes: ").strip())
        book_appointment(name, date, time, duration)
    except ValueError:
        print("❌ Invalid input. Please enter numbers for duration.")
        continue

show_schedule()



# Code: Gym Workout Tracker
# python
# Copy
# Edit
# Store members and their workouts
gym_members = {}

def add_member(name):
    if name in gym_members:
        print(f"⚠️ Member '{name}' already exists.")
    else:
        gym_members[name] = []
        print(f"✅ Member '{name}' added.")

def record_workout(name, workout_type, duration_minutes):
    if name not in gym_members:
        print(f"❌ Member '{name}' not found. Please add them first.")
        return
    workout = {
        "type": workout_type,
        "duration": duration_minutes
    }
    gym_members[name].append(workout)
    print(f"✅ Workout recorded for {name}: {workout_type} - {duration_minutes} minutes")

def show_member_workouts(name):
    if name not in gym_members:
        print(f"❌ No member named '{name}'.")
        return
    workouts = gym_members[name]
    if not workouts:
        print(f"📭 No workouts recorded for {name}.")
        return
    print(f"\n📈 Workouts for {name}:")
    for i, workout in enumerate(workouts, start=1):
        print(f" {i}. {workout['type']} - {workout['duration']} mins")

def show_all_members():
    if not gym_members:
        print("📭 No members in the system.")
        return
    print("\n🏋️ All Gym Members:")
    for name in gym_members:
        print(f"- {name}")

# Main program loop
print("🏋️ Welcome to Simple Gym Tracker")

while True:
    action = input("\nWhat do you want to do? (add / workout / history / members / exit): ").strip().lower()
    
    if action == 'exit':
        break
    elif action == 'add':
        name = input("Enter member name: ").strip()
        add_member(name)
    elif action == 'workout':
        name = input("Enter member name: ").strip()
        workout_type = input("Workout type (e.g. Cardio, Weights, Yoga): ").strip()
        try:
            duration = int(input("Duration in minutes: ").strip())
            if duration <= 0:
                print("❌ Duration must be positive.")
                continue
            record_workout(name, workout_type, duration)
        except ValueError:
            print("❌ Invalid duration.")
    elif action == 'history':
        name = input("Enter member name: ").strip()
        show_member_workouts(name)
    elif action == 'members':
        show_all_members()
    else:
        print("❌ Invalid action. Try: add, workout, history, members, or exit.")