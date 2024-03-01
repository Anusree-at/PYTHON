dict1 = { 1: "name", 2: "ID" }
print(type(dict1))

while True:
    print("1 for enquiry\n 2 for cash deposit\n 3 for cash withdrawal\n 4 for Exit")
    x = int(input("Enter your choice"))
    Name = input("Enter Your Name")
    ID = int(input("Enter Yor ID"))
    balance = 5000

    if x==1:
        print("Your name is %s", Name, "and ID is %d", ID)
        print("Account balance: 5000 ")
    elif x == 2:
        print("Enter your PIN")
        amt = int(input("Enter the amount"))
        new_balance = balance + amt
        print("Account balance: %d", new_balance)
    elif x == 3:
        print("Enter your PIN")
        amt = int(input("Enter the amount"))
        new_balance = balance - amt
        print("Account balance: %d", new_balance)
    elif x == 4:
        exit()
    else:
        print("Wrong Choice")














