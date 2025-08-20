def sum(n):
    if(n==1):
        return 11
    return sum(n-1) + n
print(sum(int(input("Enter a Num: "))))