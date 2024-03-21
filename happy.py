st = 19
def num(n):
    for digit in str(n):
        sum = (digit[0] * digit[1])
        print(sum)
print(num(15))