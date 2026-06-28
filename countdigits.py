def count_digits(number):
    count = 0
    while number>0:
        rem = number%10
        count += 1
        number = number//10
    return count

number = int(input("Enter a number: "))

result = count_digits(number)
print("The number of digits in", number, "is:", result)