class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hello! I am {self.name}.", end=" ")


class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

    def introduce(self):
        super().introduce()
        print(f"I am a student of class {self.grade}.")


class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def introduce(self):
        super().introduce()
        print(f"I teach {self.subject}.")


class School:
    def __init__(self, people):
        self.people = people

    def assembly(self):
        for person in self.people:
            person.introduce()


if __name__ == "__main__":
    school = School(
        [
            Student("Ali", 8),
            Student("Sara", 9),
            Teacher("Miss Hina", "Python"),
        ]
    )
    school.assembly()
