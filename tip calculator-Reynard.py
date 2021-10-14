x = float(input("enter the subtotal: $"))
y = int(input("enter tip amount(as a %):"))
subtotal = x
tip = x*y/100
total = subtotal + tip
print(f"\nsubtotal: ${subtotal:.2f}")
print(f"\ntip: $ {tip:.2f}")
print(f"\ntotal: $ {total:.2f}")