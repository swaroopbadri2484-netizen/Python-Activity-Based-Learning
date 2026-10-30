students = []
subject_count = int(input("Number of subjects: "))
student_count = int(input("Number of students: "))
subjects = []

for j in range(subject_count):
    subjects.append(input(f"Subject {j + 1} name: "))

for i in range(student_count):
    name = input(f"Student {i + 1} name: ")
    marks = []
    for subject in subjects:
        mark = float(input(f"{subject} marks for {name} (0-100): "))
        if mark < 0 or mark > 100:
            print("Invalid mark; using 0 for this entry.")
            mark = 0
        marks.append(mark)
    students.append([name, marks])

print("\nSTUDENT SUMMARY")
top_name = ""
top_total = -1
for name, marks in students:
    total = sum(marks)
    average = total / subject_count
    print(f"{name}: total={total:.1f}, average={average:.1f}")
    if total > top_total:
        top_total = total
        top_name = name

print("\nSUBJECT AVERAGES")
for j in range(subject_count):
    total = 0
    for student in students:
        total += student[1][j]
    average = total / student_count
    status = "LOW AVERAGE" if average < 50 else "OK"
    print(f"{subjects[j]}: {average:.1f} ({status})")

if top_name:
    print(f"Top performer: {top_name} ({top_total:.1f} marks)")
