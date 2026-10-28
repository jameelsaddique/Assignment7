class Employee:
    def __init__(self, base_salary):
        self.base_salary = base_salary

    def salary(self):
        return self.base_salary


class Manager(Employee):
    def __init__(self, base_salary, bonus):
        super().__init__(base_salary)
        self.bonus = bonus

    def salary(self):
        return super().salary() + self.bonus


if __name__ == "__main__":
    employee = Employee(50000)
    manager = Manager(50000, 30000)
    print(f"Employee: {employee.salary()}")
    print(f"Manager: {manager.salary()}")
