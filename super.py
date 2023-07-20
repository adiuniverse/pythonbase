class BankAccount :
    def __init__(self,account_number,name,email,phone_number,branch):
        self.account_number=account_number
        self.name=name
        self.__email=email
        self.phone_number=phone_number
        self.branch=branch

    def display_functions(self):
        print('name',self.name)
        print('account_number',self.account_number)
    def getphone__number(self): 
       return self.email   
    def setemail(self,email):
        self.__email=email  

class B(BankAccount):    
    def __init__(self,account_number,name,email,phone_number,branch,address):
        super() . __init__(self,account_number,name,email,phone_number,branch): 
        self.address=address
       
BankAccount1=BankAccount('123456789','adithya','adithya@gmail.com',1234567899,'calicut')      
# print(BankAccount1.phone_number)  
# BankAccount1.phone_number='1234567897'
# print(BankAccount1.phone_number) 
# print(BankAccount1.__email)
# print(BankAccount1.getemail())
BankAccount1.setemail('adi@gmail.com')
print(BankAccount1.setemail())
BankAccount2=B('123456789','adithya','adithya@gmail.com',1234567899,'calicut','mangad')
print(BankAccount2.address)