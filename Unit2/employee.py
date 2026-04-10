class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Person details")
        print("Name:", self.name)
        print("Age:", self.age)


class employee:
    def __init__(self, emp_id, salary):
        self.emp_id = emp_id
        self.salary = salary

    def display_employee(self):
        print("Employee details")
        print("Employee ID:", self.emp_id)
        print("Salary:", self.salary)


class manager(person, employee):
    def __init__(self, name, age, emp_id, salary, department):
        person.__init__(self, name, age)
        employee.__init__(self, emp_id, salary)
        self.department = department

    def display_manager(self):
        print("\n---- Manager Details ----")
        self.display_person()
        self.display_employee()
        print("Department:", self.department)

    def conduct_meeting(self):
        print(f"{self.name} is conducting a meeting for the {self.department} department")


# Creating object
manager1 = manager("ABC", 22, "1000", 95000, "IT")

# Calling methods
manager1.display_manager()
manager1.conduct_meeting()