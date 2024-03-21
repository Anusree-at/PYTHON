# class Student:
#     name = "rahul"
# s = Student()
# print(s.name)
# d = Student()
# print(d.name)
# s.name="hello"
# print(s.name)
# print(d.name)


# class Student:
#     def display(self,x):
#         print(x)
#     def display2(self):
#         print("hello world")
#
# s=Student()
# s.display("hello")
# s.display2()


# class Calculator:
#     def addition(self,a,b):
#         print(a+b)
#     def subtraction(self,a,b):
#         print(a - b)
#     def multiplication(self,a,b):
#         print(a * b)
#     def division(self, a, b):
#         print(a / b)
# c=Calculator()
#
# while True:
#     print("1 for addition \n 2 for subtraction\n 3 for multiplication\n 4 for division")
#     choice = int(input("enter your choice"))
#     if choice == 1:
#         c.addition(10,5)
#     elif choice==2:
#         c.subtraction(10,5)
#     elif choice==3:
#         c.multiplication(10,5)
#     elif choice==4:
#         c.division(10,5)
#     else:
#         print("wrong choice")
#
#
#
# class Student:
#     def __init__(self):
#         print("This is non parametrized constructor")
#     def show(self,name):
#         print("hello",name)
# student = Student()
# (here  above, init activates on every time when a variable is created.so the init function
# works eventhough the function is not called)
class Student:
    def __init__(self):
        print("The first constructor")
    def __init__(self):
        print("The second constructor")
st = Student()
# (if there are 2 init functions the 2nd one works)




