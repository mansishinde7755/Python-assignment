# Parent class 1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_person_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


# Parent class 2 (inherits from Person)
class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        # Call Person constructor
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def show_employee_info(self):
        print(f"Employee ID: {self.employee_id}, Salary: {self.salary}")


# Child class (inherits from BOTH Person and Employee)
class Manager(Employee, Person):
    def __init__(self, name, age, employee_id, salary, department):
        # Call Employee constructor (which already calls Person)
        super().__init__(name, age, employee_id, salary)
        self.department = department

    # New behaviour added in Manager
    def show_manager_info(self):
        print(f"Department: {self.department}")

    # Combined behaviour from all classes
    def display_full_details(self):
        print("\nManager Details")
        self.show_person_info()
        self.show_employee_info()
        self.show_manager_info()


# Create Manager object
m1 = Manager("Mansi", 18, "E101", 50000, "IT")

# Call combined method
m1.display_full_details()