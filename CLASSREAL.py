class Cars:
    def __init__(self,name,price,colour):
        self.name = name
        self.price = price
        self.colour = colour
    def start(self):
        print(self.name + "Engine Started")
car1 = Cars('Maruthi Swift',10000,'red')  
car2 = Cars('Toyota Innova',20000,'white')
del car2

print(car1.name,car1.price)
# print(car2.name,car2.colour)