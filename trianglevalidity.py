def is_valid_triangle(a,b,c):
    if(a+b>c and b+c>a and c+a>b):
        return True
    else:
        return False
    
s1 = int(input("Enter the first side of the triangle: "))
s2 = int(input("Enter the second side of the triangle: "))
s3 = int(input("Enter the third side of the triangle: "))

result = is_valid_triangle(s1,s2,s3)
print(result)

