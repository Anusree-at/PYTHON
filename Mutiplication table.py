n=10
num=2
res=1
for i in range(1,n):
    for j in range(i-1):
        res *=num
        print(i, "*",  num, "=", res, end="")
    print()
