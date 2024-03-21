# syntax error

# if 10 > 1
#     print("10 is greater")

# logical error
# a = 10
# b = 5
# c = a - b
# print(c)

# runtime error
# a = 10
# b = 0
# c = a/b
# print(c)

# try:
#     x = int(input("enter a number: "))
#     y = int(input("enter a number"))
#     z = x/y
#     print(z)
# except ValueError:
#     print("value or format error")
# except ZeroDivisionError:
#     print("can't divide by zero")

# try:
#     l = [1,2,3,4,5]
#     print(l[10])
# except IndexError:
#     print("Index out of range")

# try:
#     f = open("emptyfile", "r")
#     print(f.read())
# except FileNotFoundError:
#     print("file not found")

# try:
#     from m5 import display
#     m5.dispaly()
# except ModuleNotFoundError:
#     print("Module not found")
# #
# try:
#     dict = {1:"abc", 2:"xyz"}
#     print(dict[3])
# except KeyError:
#     print("key not found")
# try:
#     run this code
# except:
#     run this code when exception occurs
# else:
#     run this code if no exception occures
# finally:
#     always run this code

try:
    a = 10
    b = 2
    c = a/b
    print(c)
except:
    print("exception occured")
else:
    print("no exception")
finally:
    print("programme ends")




