class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = int(base_salary)
    
    def total_salary(self):
        return self.base_salary

    def display(self):
        print(f"Name: {self.name}, Total: {self.total_salary():.2f}")

class Manager(Employee):
    def __init__(self, name, base_salary, bonus_percent):
        super().__init__(name, base_salary)
        self.bonus_percent = float(bonus_percent)

    def total_salary(self):
        return self.base_salary * (1 + self.bonus_percent/100)

class Developer(Employee):
    def __init__(self, name, base_salary, completed_projects):
        super().__init__(name, base_salary)
        self.completed_projects = int(completed_projects)

    def total_salary(self):
        return self.base_salary + self.completed_projects * 500

class Intern(Employee):
    def __init__(self, name, base_salary):
        super().__init__(name, base_salary)

info = input().split()

match info[0]:
    case "Manager":
        worker = Manager(info[1], info[2], info[3])
    case "Developer":
        worker = Developer(info[1], info[2], info[3])
    case "Intern":
        worker = Intern(info[1], info[2])

worker.display()