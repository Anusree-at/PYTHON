# f = open("file.txt", 'r')
# print(f.read())
#
# with open("file.txt", 'r') as f:
#     print(f.read())
#
# f = open("new.txt", 'x')

f = open("new.txt", 'w')
f.write("hello")
f.write(" world")

f = open("new.txt", 'a')
f.write(" python")




