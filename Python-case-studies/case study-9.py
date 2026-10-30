rows = int(input("Number of rows: "))
columns = int(input("Seats per row: "))

if rows <= 0 or columns <= 0 or rows > 26:
    print("Invalid dimensions. Use 1 to 26 rows and positive columns.")
else:
    reserved_text = input("Reserved seats (comma-separated, e.g. A2,B1): ")
    reserved = reserved_text.upper().replace(" ", "").split(",")
    if reserved == [""]:
        reserved = []

    seating = []
    reserved_count = 0

    for r in range(rows):
        row = []
        row_letter = chr(65 + r)
        for c in range(1, columns + 1):
            label = row_letter + str(c)
            if label in reserved:
                row.append(label + "[R]")
                reserved_count += 1
            else:
                row.append(label + "[ ]")
        seating.append(row)

    print("\nSEATING CHART ([R] = Reserved, [ ] = Available)")
    for row in seating:
        print("  ".join(row))

    print(f"Total capacity: {rows * columns}")
    print(f"Reserved seats in chart: {reserved_count}")
    print(f"Available seats: {rows * columns - reserved_count}")
