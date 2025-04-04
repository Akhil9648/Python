import random
class Train:
    def __init__(self,trainNo):
        self.trainNo=trainNo
    def book(self,fro,to):
        print(f"Ticket in Train  No. {self.trainNo} is boked from {fro} to {to}")
    def getstatus(self):
        print(f"Train No. {self.trainNo} is Running on Time")
    def getFare(self,fro,to):
        print(f"Ticket in Train No. {self.trainNo} from {fro} to {to} is worth {random.randint(200,800)}")
t=Train(123654)
t.book("Rampur","Lucknow")
t.getstatus()
t.getFare("Rampur","Lucknow")
