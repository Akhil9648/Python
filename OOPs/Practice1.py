class programmer:
    def __init__(self,name,company,language,salary):
        self.name=name
        self.company=company
        self.language=language
        self.salary=salary
    def print(self):
        print(f"Hii {self.name} Welcome to {self.company} your role is {self.language} developer and your current Salary is {self.salary}")

Akhil=programmer("Akhil","Microsoft","C++",300000)
Archit=programmer("Archit","Microsoft","Python",250000)
Akhil.print()
Archit.print()
