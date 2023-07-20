

class A:
    a = 100
    def __init__(self):
        print('This is class A')
    def display1(self):
        print('This is display1')  
    def display2(self):
        print('This is display2')    
    def display3(self):
        print('This is display3')   
class B(A):#b inherit a
    # def __init__(self):
    #     print('This is class B') if init not give then a will work.. 
    def display4(self):
        print('This is display4') 
    def display3(self):
           print('This is oveeriden method') 

class C(B):
    def display5(self):
           print('This is display5') 





object1=B() 
object1.display2() 
object1.display3()   
object2=B()
object2=B()
print(object1.a,object2.a)
print(B.a)
B.a=20
print(B.a)
object3=C()
object3.display2()