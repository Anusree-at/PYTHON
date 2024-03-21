from add import add
from display import dis
from delete import delete
from update import up
while True:
    print("1 for Add book\n 2 for Display book\n 3 for Update book price\n 4 for Delete")
    choice = int(input("Enter your choice"))

    if choice == 1:
       add()
    if choice == 2:

        dis()

    if choice == 4:

        delete()
    if choice == 3:

        up()







