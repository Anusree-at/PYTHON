list1 = []

class Create:
    def veh(self):
        self.number = ""
        self.name = ""
        self.price = ""
        self.wheels = ""

    def datas(self):
        self.number = int(input("enter the vehicle number: "))
        self.name = input("enter the name: ")
        self.price = int(input("enter the price:"))
        self.wheels = int(input("enter the number of wheels: "))

    def display(self):
        x = int(input("enter the number of wheels: "))
        for i in list1:
            if i.wheels == x:
                print(i.number)
                print(i.name)
                print(i.price)
                print(i.wheels)
    def ex(self):
        exit()
while True:
    print("1 for add vehicle\n 2 for display vehicle\n 3 for exit")
    choice = int(input("enter your choice"))

    if choice == 1:
        vehicle = Create()
        vehicle.datas()
        list1.append(vehicle)

    if choice == 2:
        vehicle.display()

    if choice == 3:
        vehicle.ex()