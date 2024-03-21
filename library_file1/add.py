my_list = []

def create():
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
