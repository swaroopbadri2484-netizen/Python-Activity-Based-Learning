total = int(input("Total classes held: "))
attended = int(input("Classes attended: "))
threshold = float(input("Required attendance percentage: "))

if total <= 0 or attended < 0 or attended > total or threshold <= 0 or threshold > 100:
    print("Invalid input.")
else:
    current = attended / total * 100
    future = 0
    while (attended + future) / (total + future) * 100 < threshold:
        future += 1

    print(f"Current attendance: {current:.2f}%")
    if future == 0:
        print("You already meet the attendance requirement.")
    else:
        print(f"Minimum consecutive classes to attend: {future}")
        final_percentage = (attended + future) / (total + future) * 100
        print(f"Attendance after attending them: {final_percentage:.2f}%")
