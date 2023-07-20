class A:
    def __init__(self):
        print('parent class  A')
    def display1(self):
        print('hello display1')  
    def display2(self):
        print('hello display2') 
    def display3(self):
        print('hello display3')  



class B(A):
   def __init__(self) :
    super().__init__()
    print('child class B')
   def display4(self):
        print('hello display4')  


class C(B):
    def __init__(self) :
        super().__init__()
        print('grandchild class A')
    def display5(self):
        print('hello display5')    
        
# obj1 = A()
# obj1.display1()
# obj2 = B()  
# obj2.display1
  
obj3 = C()  
obj3.display1() 
       

                    
        