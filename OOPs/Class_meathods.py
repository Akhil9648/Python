class employee:
    a=1
    @classmethod #By using this meathod this will show the value of a in class instead of modified one
    def show(cls):
        print(f"The class value of a is {cls.a}")
e=employee()
e.a=45
e.show()
