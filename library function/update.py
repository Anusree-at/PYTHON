
from add import my_list
def up():
    id = int(input("Enter id"))
    for i in my_list:
        if i[0] == id:
            new_price = int(input("Enter the new price"))
            i[2] = new_price
