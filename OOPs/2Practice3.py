class employee:
    salary=789
    increment=74
    @property
    def salaryafterincrement(self):
        return (self.salary+self.salary*(self.increment/100))
    @salaryafterincrement.setter
    def salaryafterincrement(self):
        self.increment=((salary/self.salary)-1)*100
e=employee()
e.salaryaftericrement=1000
print(e.increment)
