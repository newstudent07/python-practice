num = int(input("Enter a list of numbers: "))

numbers = []

for i in range(num):
    n = int(input("Enter a number: "))
    numbers.append(n)

# Initialize with the FIRST actual item in the list
max_val = numbers[0]
min_val = numbers[0]

for i in range(num):
    # Check for maximum
    if numbers[i] > max_val:
        max_val = numbers[i]
    
    # Check for minimum (independent 'if' and '<' sign)
    if numbers[i] < min_val:
        min_val = numbers[i]

print("The maximum number is:", max_val)
print("The minimum number is:", min_val)

