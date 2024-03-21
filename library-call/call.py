from library_file1 import add, display, delete, update


while True:
    print("1 for Add book\n 2 for Display book\n 3 for Update book price\n 4 for Delete")
    choice = int(input("Enter your choice"))

    if choice == 1:
        add.create()
    if choice == 2:
        display.dis()

    if choice == 4:
       delete.delete()
    if choice == 3:
        update.up()

