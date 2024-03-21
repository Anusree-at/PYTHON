from library_file1.add import my_list
def delete():
    id = int(input("Enter the id"))
    for i in my_list:
        if i[0] == id:
            my_list.remove(i)
