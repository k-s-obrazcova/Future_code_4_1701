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


class Department:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def list_employees(self):
        return [str(employee) for employee in self.employees]

employee_first = Employee("Иван Иванов", "Инженер", 50000)
employee_second = Employee("Петр Петров", "Аналитик", 60000)
manager_first = Manager("Анна Смирнова", "Менеджер по закупкам", 80000)

department = Department()
department.add_employee(employee_first)
department.add_employee(employee_second)
department.add_employee(manager_first)

manager_first.add_subordinate(employee_first)
manager_first.add_subordinate(employee_second)

print("Все сотрудники отдела: ")
for emp in department.list_employees():
    print(emp)

print("Подчиненные менеджера: ")
for emp_sub in manager_first.list_subordinates():
    print(emp_sub)