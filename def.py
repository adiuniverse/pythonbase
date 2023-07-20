def display(num1,num2):

    sum=num1+num2
    sub=num1-num2
    return sum,sub

result1,result2=display(1,2)
result=result1,result2

print('sum is ',str(result1))
print('sub is', str(result2))
print(result)
print(result[0])

