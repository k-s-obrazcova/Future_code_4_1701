class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"Name: {self.name}, Position: {self.position}, Salary: {self.salary} rub."


class Manager(Employee):
    def __init__(self, name, position, salary):
        super().__init__(name, position, salary)
        self.subordinates = []

    def add_subordinate(self, employee):
        self.subordinates.append(employee)

    def remove_subordinate(self, employee):
        self.subordinates.remove(employee)

    def list_subordinates(self):
        return [str(subordinate) for subordinate in self.subordinates]
