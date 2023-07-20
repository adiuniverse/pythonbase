
def student_details(**kwargs):

   print(kwargs)

student_details('adithya',50,'female')
student_details(name='hari',gender='male',age=19)
student_details(age=20,gender='male',name='john',place='kjhxkus')

#variable length keyword arguement