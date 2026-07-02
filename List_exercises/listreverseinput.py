
def list_reverse(list):
    num=[]
    for i in list:
        num=[i]+num
    return num



e = int(input("Enter the number of elements in the list: "))

list = []

for i in range (e):
    n =int(input("Enter a number: "))
    list.append(n)

d = list_reverse(list)
print(d)