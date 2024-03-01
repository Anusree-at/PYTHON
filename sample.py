# a = 'world'
# print(a[-2:] + a[-2:] + a[-2:] + a[-2:])

n = 5
for i in range(n):
    for j in range(i + 1):
        for k in range(n - i):
            print(" ", end=" ")
        print()
        print("*", end="")
    print()


