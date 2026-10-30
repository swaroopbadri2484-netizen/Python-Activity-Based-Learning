products = [
    ("P101", 50.0, 10),
    ("P102", 120.0, 3),
    ("P103", 75.0, 0),
    ("P102", 90.0, 4)
]

seen_ids = []
total_value = 0

print("PRODUCT CATALOGUE AUDIT")
for product in products:
    product_id, price, quantity = product  # tuple unpacking

    if product_id in seen_ids:
        print(f"{product_id}: duplicate product ID")
    else:
        seen_ids.append(product_id)

    if price < 0 or quantity < 0:
        print(f"{product_id}: invalid price or quantity")
    else:
        value = price * quantity
        total_value += value
        print(f"{product_id}: price=₹{price:.2f}, stock={quantity}, "
              f"inventory value=₹{value:.2f}")
        if quantity < 5:
            print(f"{product_id}: replenishment required")

print(f"Total inventory value (valid numeric records): ₹{total_value:.2f}")
