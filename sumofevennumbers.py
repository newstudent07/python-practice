def sum_evens(n):
    sum = 0
    for i in range(1,n+1):
        if i % 2 == 0:
            sum += i
    return sum
          
        
n = int(input("Enter a number: "))

result = sum_evens(n)
print("The sum of even numbers from 1 to", n, "is:", result)