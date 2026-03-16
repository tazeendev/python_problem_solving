class Student:
    def __init__(abc, name,  age):
        abc.names = name
        abc.age=age
        print('constructor is called')

s1 = Student("Ali" ,23)
print(s1.names)
print(s1.age)