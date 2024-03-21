list1 = []
class Library:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.price = ""
        self.author = ""
        self.publisher = ""

    def datas(self):
        self.id = int(input("enter the id: "))
        self.name = input("enter book name: ")
        self.price = int(input("enter the price: "))
        self.author = input("author:  ")
        self.publisher = input("publisher: ")
        list1.append([id, self.name, self.price, self.author, self.publisher])
    def display(self):
        x = int(input("enter the id: "))
        for i in list1:
            if i[0] == x:

                # print(i[0])
                # print(i[1])
                # print(i[2])
                # print(i[3])
                # print(i[4])
    def up(self):
        x = int(input("enter the id: "))
        for i in list1:
            if i[2] == x:
               new = int(input("Enter the new price"))
               i[2] = new
    def delete(self):
        x = int(input("Enter the id"))
        for i in list1:
            if i[0] == x:
                list1.remove(i)


book = Library()
upd = Library()
while True:

    print("1 for add book\n 2 display\n 3 for update\n 4 for delete")
    choice = int(input("enter your choice"))

    if choice == 1:
        book.datas()
    if choice == 2:
        book.display()

    if choice == 3:
        upd.up()
    if choice == 4:
        book.delete()






