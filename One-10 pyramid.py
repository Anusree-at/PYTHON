n=int(input("Enter a number"))
count=0
for i in range(n):
    for j in range(i+1):
        count +=1
        print(count, end=" ")
    print()