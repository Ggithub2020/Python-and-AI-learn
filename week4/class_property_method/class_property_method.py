# Here's a clean and simple example of a Python class that represents a Car, demonstrating:

# Class

# Constructor (__init__)

# Properties

# Functions (methods)

# python
# Copy
# Edit
class Car:
    # Constructor
    def __init__(self, make, model, year, color):
        self.make = make        # Property: car brand
        self.model = model      # Property: car model
        self.year = year        # Property: manufacturing year
        self.color = color      # Property: car color
        self.engine_on = False  # Initial state of the engine

    # Method to display car details
    def display_info(self):
        print(f"{self.year} {self.color} {self.make} {self.model}")

    # Method to start the engine
    def start_engine(self):
        if not self.engine_on:
            self.engine_on = True
            print("Engine started.")
        else:
            print("Engine is already running.")

    # Method to stop the engine
    def stop_engine(self):
        if self.engine_on:
            self.engine_on = False
            print("Engine stopped.")
        else:
            print("Engine is already off.")

# Example usage
my_car = Car("Toyota", "Camry", 2021, "Blue")
my_car.display_info()
my_car.start_engine()
my_car.start_engine()  # Will say already running
my_car.stop_engine()