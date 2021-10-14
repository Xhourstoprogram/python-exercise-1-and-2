a = float(input("Enter length of edge 1: "))
b = float(input("Enter length of edge 2: "))
c = float(input("Enter length of edge 3: "))
x = a + b + c
if a + b < c:
    print("Perimeter cannot be calculated: the input is invalid")
elif a + b > c:
    print("The perimeter is",x)