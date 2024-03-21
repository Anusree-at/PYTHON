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
        x = int(input("enter the id: "))
        for i in list1:
            if i.id == x:
                print(i.id)
                print(i.name)
                print(i.price)
                print(i.author)
                print(i.publisher)

    def up(self):
        x = int(input("enter the id: "))
        # new = input("Enter the new value: ")
        for i in list1:
            if i.id == x:
                while True:
                    print("1 for name\n 2 for price\n 3 for author\n 4 for publisher\n 5 for exit")
                    choice1 = int(input("enter the choice"))

                    if choice1 == 1:
                        new = input("Enter the new name: ")
                        i.name= new
                    if choice1 == 2:
                        new = int(input("enter the new price: "))
                        i.price = new
                    if choice1 == 3:
                        new = input("enter the new author: ")
                        i.author = new
                    if choice1 == 4:
                        new = input("enter the new publisher")
                        i.publisher = new
                    if choice1 ==5:
                        break


    def delete(self):
        x = int(input("Enter the id"))
        for i in list1:
            if book.id == x:
                list1.remove(i)
    #
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

        # for i in list1:
        #     i.display()
         book.display()

    if choice == 3:
         book.up()


    if choice == 4:
        book.delete()


