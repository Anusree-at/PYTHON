
# single inheritance
# class A:
#     def display(self):
#         print("hello")
#     def display1(self):
#         print("world")
#
# class B(A):
#     pass
#
# obj = B()
# obj.display()
# obj.display1()

#
# multi level inheritance
# class  A:
#     def display(self):
#         print("hello")
#
# class B(A):
#     def display1(self):
#         print("hii")
#
# class C(B):
#     def display2(self):
#         print("python")
#
# obj = C()
# obj.display()
# obj.display1()
# obj.display2()

#
# multiple inheritance
# class A:
#     def display(self):
#         print("hello")
#
# class B:
#     def display1(self):
#         print("hii")
# class C(A,B):
#     def display2(self):
#         print("python")
#
# obj = C()
# obj.display()
# obj.display1()
# obj.display2()
#
#
# Hierarcheal inhritance
# class A:
#     def display(self):
#         print("hello")
# class B(A):
#     def display1(self):
#         print("hii")
# class C(A):
#     def display2(self):
#         print("python")
# obj = C()
# obj.display()
# obj.display2()
#
# obj = B()
# obj.display()
# obj.display1()


# Hybrid inheriance

class A:
    def display(self):
        print('1')
class B(A):
    def display1(self):
        print('2')
class C(A):
    def display2(self):
        print('3')
class D(B,C):
    def display3(self):
        print('4')

obj = D()
obj.display()
obj.display1()
obj.display2()
obj.display3()