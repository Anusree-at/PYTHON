mylist = [10, 20, 30, 50]
mylist.append(15)
print(mylist)

mylist.remove(30)
print(mylist)
print(mylist.index(50))
mylist.count(50)

newlist = [100, 20, 35, 15, 50]
newlist.sort()
print(newlist)

print(len(newlist))
print(newlist[1 : 4])

list1 = [10,50,12]
list2 = [30,22,45]
list3 = list1+list2
print(list3)

print(50 in list1)

x = list1.copy()
print(x)