class Employee:
    company="Apple"
    def show(self):
        print(f"The name of employee is {self.name} and his salary is {self.salary}")
# class programmer:
#     company="Apple India"
#     def show(self):
#         print(f"The name of employee is {self.name} and his salary is {self.salary}")
#     def showlan(self):
#         print(f"The name of employee is {self.name} and he is good in {self.language}")
class programmer(Employee):
    company="Apple India"
    def showlan(self):
        print(f"The name of employee is {self.name} and he is good in {self.language}")
a=Employee()
b=programmer()
print(a.company,b.company)
