a = int(input("Enter the number of packages purchase: "))
price = 99
discount = 0 or 0.1 or 0.2 or 0.3 or 0.4
if 1 <= a <= 9:
    discount = 0
    print(f"\nDiscount amount @ 0%: ${price*a*discount:.2f}")
    print(f"\n Total amount: ${(price*a)-(price*a*discount):.2f}")
elif 10 <= a <= 19:
    discount = 0.1
    print(f"\nDiscount amount @ 10%: ${price*a*discount:.2f}")
    print(f"\n Total amount: ${(price*a)-(price*a*discount):.2f}")
elif 20 <= a <= 49:
    discount = 0.2
    print(f"\nDiscount amount @ 20%: ${price*a*discount:.2f}")
    print(f"\n Total amount: ${(price*a)-(price*a*discount):.2f}")
elif 50 <= a <= 99:
    discount = 0.3
    print(f"\nDiscount amount @ 30%: ${price*a*discount:.2f}")
    print(f"\n Total amount: ${(price*a)-(price*a*discount):.2f}")
elif a >= 100:
    discount = 0.4
    print(f"\nDiscount amount @ 40%: ${price*a*discount:.2f}")
    print(f"\n Total amount: ${(price*a)-(price*a*discount):.2f}")