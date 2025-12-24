#🏫 School Registration System in Python
# This code defines a simple school registration system using Python classes.
# This code defines a simple school registration system using Python classes.   

# Class to represent a student
class Student:
    def __init__(self, student_id, first_name, last_name, grade):
        self.student_id = student_id  # Unique ID
        self.first_name = first_name
        self.last_name = last_name
        self.grade = grade

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_details(self):
        return f"ID: {self.student_id}, Name: {self.get_full_name()}, Grade: {self.grade}"


# Class to represent the school registration system
class School:
    def __init__(self, name):
        self.name = name
        self.students = []  # List to store registered students

    def register_student(self, student):
        self.students.append(student)
        print(f"✅ {student.get_full_name()} has been registered.")

    def list_students(self):
        if not self.students:
            print("No students registered yet.")
        else:
            print(f"📋 List of registered students in {self.name}:")
            for student in self.students:
                print(student.get_details())


# Example usage
school = School("Green Valley High School")

# Creating some students
student1 = Student(101, "Alice", "Johnson", 10)
student2 = Student(102, "Bob", "Smith", 11)

# Registering students
school.register_student(student1)
school.register_student(student2)

# Listing students
school.list_students()