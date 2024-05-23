# Classes and Instances for employees
# describe the Difference  a class and instance of class
# constructor and normal function
# class variable and instance variable
# classmethods and staticmethods
class employee:
    user_type: int = 1

    def __init__(self, name, age, email) -> None:
        self.name: str = name
        self.age: str = age
        self.email: str = email

    def nameandage(self):
        return '{} have {} years'.format(self.name, self.age)


emp: employee = employee("mohanad", "18", "mg@sg.com")
print(emp.nameandage())
