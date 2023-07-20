class Account :
    __amount = 0
    def __init__(self , name , account_number ,branch , amount, password ):
        self.name = name
        self.__account_number = account_number # __ for making private
        self.branch = branch
        # self.__amount = amount
        self.set_amount(amount)
        self.password = password
        
    def display_account(self):
        print('account details')

    def get_account_number(self):
        if(self.password == '12345abc') :
              return self.__account_number
        else :
               return 'invalid password' 

   
    def get_amount(self)   :
        if(self.password == '12345abc') :
              return self.__amount
        else :
               return 'invalid password' 

               
    def set_amount(self, amt) :
        # self.__amount += amt    
        if(amt > 0) :
             self.__amount += amt  
        else:
            self.__amount += 0 
            

                
object1 = Account('adithya',1234567891,'poonoor',-4000,'12345abc')  
print(object1.get_account_number())  

print(object1.get_amount())
object1.set_amount (5000)
print(object1.get_amount())

