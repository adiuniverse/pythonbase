# class Products:
#     product_name='apple'
#     category='fruits'
#     price=50

# product1=Products()
# print(product1.product_name)
# product2=Products()
# print(product1.product_name)




class Products:
    def __init__ (self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_product(self):
        print('product name is', self.name, 'price is' , self.price, 'quantity is' ,self.quantity)   
product1=Products('apple', 50, 10)
print(product1.name)   
product1.display_product()
product2=Products('orange', 100 ,5)
print(product2.name)
product2.display_product()





