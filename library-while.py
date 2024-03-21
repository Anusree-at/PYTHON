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
    def up_name(self):
        x = int(input("enter the id: "))
        new = input("Enter the new name: ")
        for i in list1:
            if book.id == x:
                book.name = new


    def up_author(self):
        x = int(input("enter the id: "))
        new = input("Enter the new author: ")
        for i in list1:
            if book.id == x:
                book.author = new

    def up_publisher(self):
        x = int(input("enter the id: "))
        new = input("Enter the new publisher: ")
        for i in list1:
            if book.id == x:
                book.publisher = new

    def ex(self):
        exit()
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

     while True:
         print("1 for update book name\n 2 for update price\n 3 for update author\n 4 for update publisher\n 5 for exit")
         choice = int(input("enter the choice"))

         if choice == 1:
             book.up_name()

         if choice == 2:
             book.up()
         if choice == 3:
             book.up_author()
         if choice == 4:
             book.up_publisher()
         if choice == 5:
             # book.ex()
             break

    if choice == 4:
        book.delete()


