list1 = []

class create:
    def __init__(self):
        self.name = ""
        self.number = ""
        self.balance = ""
        self.deposit = ""
        self.withdraw = ""
    def data(self):
        self.name = input("enter the name: ")
        self.number = int(input("enter a/c number: "))
        self.balance = int(input("enter the balance: "))
        # self.deposit = int(input("enter the amount"))
        # self.withdraw = int(input("enter the amount"))
    def dep(self):
        x = int(input("enter the a/c number: "))
        amt1 = int(input("enter the amount:"))
        for i in list1:
            if i.number == x:
                bal = (i.balance + amt1)
                print("balance is ", bal)
                i.balance = bal
    def withd(self):
        x = int(input("enter the a/c number: "))
        amt = int(input("enter the amount: "))

        for i in list1:
            if i.number == x:
                while True:
                    minim = 500
                    if i.balance > minim:
                        bal = (i.balance - amt)
                        print("balance is", bal)

                        i.balance = bal
                        break
                    if i.balance < minim:
                            print("A/C balance is less than 500")
                            break

    def enquiry(self):
        x = int(input("enter the A/C number: "))
        for i in list1:
            if i.number == x:
                print("Available balance is ", i.balance)


while True:
    print(" 1 for add details\n 2 for deposit\n 3 for withrwal\n 4 for balance enquiry")
    choice = int(input("enter the choice: "))

    if choice == 1:
        account = create()
        account.data()
        list1.append(account)
    if choice == 2:
        account.dep()
    if choice == 3:
        account.withd()
    if choice == 4:
        account.enquiry()


