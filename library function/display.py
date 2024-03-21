from add import my_list

def dis():
    id = int(input("enter book id: "))
    for i in my_list:
        if i[0] == id:
            print(i[0])
            print(i[1])
            print(i[2])
            print(i[3])
            print(i[4])
