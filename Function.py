def fun1(num1, num2):
    res = num1 + num2
    return res
def fun2(num1, num2):
     res = num1 - num2
     return res
def fun3(num1, num2):
    res = num1 * num2
    return res
def fun4(num1, num2):
    res = num1 / num2
    return res

while True:
    print("1 for Addition\n 2 for subtraction\n 3 for multiplication\n 4 for division")
    x = int(input("enter your choice"))
    # num1 = int(input("enter the first number"))
    # num2 = int(input("enter the second number"))
    if x == 1:
        fun1(10, 20)
        print(fun1(10, 20))
    elif x == 2:
        fun2(10, 20)
        print(fun2(10, 20))
    elif x == 3:
        fun3(10, 20)
        print(fun3(10, 20))
    elif x == 4:
        fun4(10, 20)
        print(fun4(10, 20))






