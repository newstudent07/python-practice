n = int(input("Enter a number: "))
sum = 0
temp = n
while temp>0:
    d = temp%10
    sum = sum+(d*d*d)
    temp = temp//10
if sum==n:
    print("It is an Armstrong Number! ")
else: 
    print("It is not an Armstong Number!")

