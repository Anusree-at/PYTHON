def pattern(a,b):
for i in range(a):
    for j in range(b):
        if i%2 == 0:
            print("*", end="")
        elif j == (b-i):
            print("*", end="")


pattern(3, 4)

