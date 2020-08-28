# ----------------- Inheritance ------------

# ========== parent class ===============
class Employee:

    increment = 1

    def __init__(self, a_name, a_salary):
        self.salary = a_salary
        self.name = a_name

    @classmethod
    def ChangeIncrement(cls, new_increment):
        cls.increment = new_increment

    def ChangeSalary(self):
        self.salary = self.salary * self.increment

    @staticmethod
    def isOpen(day):
        if day == "sunday":
            return False
        else:
            return True


rohan = Employee("rohan", 75000)
rohit = Employee("rohit", 85000)

# print("rohan initial salary : ", rohan.salary)

# change increment

# Employee.ChangeIncrement(2)

# change salary

# rohan.ChangeSalary()

# print("rohan new salary : ", rohan.salary)

# print(Employee.isOpen("sunday"))


# ============== child class ================
class Developer(Employee):

    def __init__(self, a_name, a_salary, a_language, a_experience):
        super().__init__(a_name, a_salary)
        self.language = a_language
        self.experience = a_experience

    def ChangeSalary(self):
        self.salary = self.salary * (self.increment+0.2)


Developer.ChangeIncrement(1.5)

tushar = Developer("tushar", 85000, "Python", "5 yrs")

print(" salary : ", tushar.salary)
tushar.ChangeSalary()


print("new salary : ", tushar.salary)


# what is use super() ?

# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
