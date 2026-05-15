class Employee:
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary

    def display(self):
        print(self.name, self.salary)


class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language=language
    def code(self):
        print(self.name, "writes", self.language, "code")


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size=team_size
    def manage(self):
        print(self.name, "manages", self.team_size, "people")

d1=Developer("Aditi", 7000000, "Python")
d1.display()
d1.code()

d2= Manager("Aditya", 70000000, 100)
d2.display()
d2.manage()
