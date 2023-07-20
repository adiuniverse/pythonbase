a = int(input('enter a number'))
b = int(input('enter another number'))
result = 0
try :
    result = a/b
except ZeroDivisionError: 
    print('division by zero')   
print(result)    