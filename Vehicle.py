vehicle = []

while True:
    choice = int(input("1 for Add vehicle\n 2 for Display vehicle"))
    if choice == 1:
        no = int(input("Vehicle number: "))
        name = input("Name: ")
        price = int(input("Price: "))
        wheels = int(input("No. of Wheels: "))
        list1 = []
        list1.append(no)
        list1.append(name)
        list1.append(price)
        list1.append(wheels)
        vehicle.append(list1)
    if choice == 2:
        num = int(input("Number of wheels"))

        for i in vehicle:
            if i[3] == num:
                print(i[0])
                print(i[1])
                print(i[2])
                print(i[3])









