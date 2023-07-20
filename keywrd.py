def details(**kwargs):
     print(kwargs)
     for i in kwargs:
         print(i,'is',kwargs[i])
details(age=22,name='ravi',gender='male')
details(age=20,name='adiya',gender='female',place='calicut')