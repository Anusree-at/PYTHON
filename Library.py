my_list = []

while True:
    print("1 for Add book\n 2 for Display book\n 3 for Update book price\n 4 for Delete")
    choice = int(input("Enter your choice"))

    if choice == 1:
        list1 = []
        id1 = int(input("Book ID: "))
        name = input("Book Name: ")
        price = int(input("price: "))
        author = input("Author: ")
        pub = input("Publisher: ")
        list1.append(id1)
        list1.append(name)
        list1.append(price)
        list1.append(author)
        list1.append(pub)

        my_list.append(list1)
    if choice == 2:
        id = int(input("enter book id: "))
        for i in my_list:
            if i[0] == id:
                print(i[0])
                print(i[1])
                print(i[2])
                print(i[3])
                print(i[4])

    if choice == 4:
        id = int(input("Enter the id"))
        for i in my_list:
            if i[0] == id:
                my_list.remove(i)
    if choice == 3:
        id = int(input("Enter id"))
        for i in my_list:
            if i[0] == id:
                new_price = int(input("Enter the new price"))
                i[2] = new_price














