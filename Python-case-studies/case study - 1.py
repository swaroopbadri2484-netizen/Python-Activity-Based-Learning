month = input("Month name: ")
start_day = int(input("Starting weekday (Mon=0 ... Sun=6): "))
days = int(input("Number of days (28 to 31): "))

if start_day < 0 or start_day > 6 or days < 28 or days > 31:
    print("Invalid weekday or number of days.")
else:
    print("\n", month)
    print("Mo Tu We Th Fr Sa Su")
    print("   " * start_day, end="")

    for day in range(1, days + 1):
        print(f"{day:2}", end=" ")
        if (start_day + day) % 7 == 0:
            print()
    if (start_day + days) % 7 != 0:
        print()
