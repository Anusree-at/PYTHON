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
        # list1.append([id, self.name, self.price, self.author, self.publisher])
    def display(self):
        print(self.id)
        print(self.name)
        print(self.price)
        print(self.author)
        print(self.publisher)

    def up(self):
        x = int(input("enter the id: "))
        new = int(input("Enter the new price: "))
        for i in list1:
            if book.id == x:

               book.price = new
    def delete(self):
        x = int(input("Enter the id"))
        for i in list1:
            if book.id == x:
                list1.remove(i)


# book = Library()
# upd = Library()
while True:

    print("1 for add book\n 2 display\n 3 for update\n 4 for delete")
    choice = int(input("enter your choice"))

    if choice == 1:
        book = Library()
        book.datas()
        list1.append(book)
    if choice == 2:

        for i in list1:
           i.display()


    if choice == 3:
        book.up()
    if choice == 4:
        book.delete()


