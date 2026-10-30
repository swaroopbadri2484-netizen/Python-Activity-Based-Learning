months = int(input("Enter number of months: "))
bills = []

for month in range(1, months + 1):
    units = int(input(f"Units used in month {month}: "))

    if units < 0:
        print("Invalid units. Enter a non-negative value.")
        continue

    if units <= 100:
        energy = units * 2
    elif units <= 200:
        energy = 100 * 2 + (units - 100) * 3
    else:
        energy = 100 * 2 + 100 * 3 + (units - 200) * 5

    surcharge = energy * 0.05
    subtotal = energy + 50 + surcharge
    rebate = 0

    if units <= 100:
        rebate = subtotal * 0.10

    bill = subtotal - rebate
    bills.append(bill)
    print(f"Month {month}: Energy=₹{energy:.2f}, "
          f"Surcharge=₹{surcharge:.2f}, Rebate=₹{rebate:.2f}, "
          f"Bill=₹{bill:.2f}")

for i in range(1, len(bills)):
    if bills[i - 1] > 0:
        increase = (bills[i] - bills[i - 1]) / bills[i - 1] * 100
        if increase > 30:
            print(f"Unusual increase in month {i + 1}: {increase:.1f}%")

if not bills:
    print("No valid bills were calculated.")
