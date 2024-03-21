class Calc:
    def add(self):
        a = int(input("enter a number"))
        b = int(input("enter a number"))
        print(a+b)
    def min(self):
        a = int(input("enter a number"))
        b = int(input("enter a number"))
        print(a - b)

    def mul(self):
        a = int(input("enter a number"))
        b = int(input("enter a number"))
        print(a * b)
    def div(self):
        a = int(input("enter a number"))
        b = int(input("enter a number"))
        print(a / b)
res = Calc()
while True:
    print("1 for addition \n 2 for subtraction\n 3 for multiplication\n 4 for division")
    choice = int(input("enter your choice"))

    if choice == 1:
        res.add()
    if choice == 2:
        res.min()
    if choice == 3:
        res.mul()
    if choice == 4:
        res.div()




