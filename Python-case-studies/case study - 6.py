count = int(input("Number of products: "))
items = []
subtotal = 0

for i in range(count):
    print(f"Product {i + 1}")
    name = input("Name: ")
    price = float(input("Price (₹): "))
    quantity = int(input("Quantity: "))
    category = input("Category (electronics/grocery/other): ").lower()

    if price < 0 or quantity <= 0:
        print("Invalid product. Skipped.")
        continue

    line_total = price * quantity
    items.append((name, price, quantity, category, line_total))
    subtotal += line_total

if subtotal >= 2000:
    discount = min(subtotal * 0.10, 500)
else:
    discount = 0

total_tax = 0
print("\n--------- ITEMIZED INVOICE ---------")
for name, price, quantity, category, line_total in items:
    if subtotal > 0:
        item_discount = discount * line_total / subtotal
    else:
        item_discount = 0
    taxable = line_total - item_discount

    if category == "electronics":
        rate = 0.18
    elif category == "grocery":
        rate = 0.05
    else:
        rate = 0.12

    tax = taxable * rate
    total_tax += tax
    print(f"{name}: {quantity} x ₹{price:.2f} = ₹{line_total:.2f}; "
          f"tax ₹{tax:.2f}")

grand_total = subtotal - discount + total_tax
print(f"Subtotal : ₹{subtotal:.2f}")
print(f"Discount : ₹{discount:.2f}")
print(f"Total tax: ₹{total_tax:.2f}")
print(f"Grand total: ₹{grand_total:.2f}")
