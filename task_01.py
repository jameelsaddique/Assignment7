class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        return f"My name is {self.name} and I am {self.age}."


class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no

    def intro(self):
        return f"{super().intro()} Roll no: {self.roll_no}"


if __name__ == "__main__":
    student = Student("Sara", 15, 101)
    print(student.intro())
