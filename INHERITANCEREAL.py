class Person:
    def __init__(self,name,contact):
        self.name = name
        self.contact = contact
    def address(self):
        print(self.name,self.contact)   

class Doctor(Person):
    pass
class Patient(Person):
    pass

doct1 = Doctor('john',12345)
pat1 = Patient('sunil',67891)

doct1.address()
pat1.address()