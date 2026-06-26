n = int(input("Enter a Year: "))

if (n%4==0 and n%100!=0) or (n%400==0):
    print(n,"is a Leap Year")
else:
    print(n,"is not a Leap Year")
