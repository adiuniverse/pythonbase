# def sum(a,b):
#     c = a + b
#     return c
# print(sum(10,20))   


# def printDetails(*components):
#     # print('%s costs %d' %(item,price))
#     print('components of  are')
#     for i in components:
#         print (i)
# # printDetails('apple')    
# printDetails('apple','orange','banana') 



def printDetails(*components):
    global x 
    x= 100
    # print('%s costs %d' %(item,price))
    print('components of  are')
    for i in components:
        print (i)
# printDetails('apple')    
printDetails('apple','orange','banana') 
print(x)
