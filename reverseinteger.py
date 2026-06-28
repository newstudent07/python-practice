def reverse_int(n):
    rev=0;j=0
    while n>0:
        rem=n%10
        rev = rev*10 + rem
        n= n//10
    return rev

n = int(input("Enter a number: "))
result = reverse_int(n)
print("The reverse of", n, "is:", result)