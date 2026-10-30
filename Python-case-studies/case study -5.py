name = input("Employee name: ")
basic = float(input("Basic pay (₹): "))
overtime_hours = float(input("Overtime hours: "))
incentive = float(input("Incentive (₹): "))

if basic < 0 or overtime_hours < 0 or incentive < 0:
    print("Invalid input: values cannot be negative.")
else:
    hra = basic * 0.20
    travel = basic * 0.05
    overtime_pay = overtime_hours * 150
    gross = basic + hra + travel + overtime_pay + incentive

    if gross <= 25000:
        deduction = gross * 0.05
    elif gross <= 50000:
        deduction = 1250 + (gross - 25000) * 0.10
    else:
        deduction = 3750 + (gross - 50000) * 0.15

    net = gross - deduction
    print("\n------ SALARY STATEMENT ------")
    print("Employee:", name)
    print(f"Basic pay       : ₹{basic:.2f}")
    print(f"HRA             : ₹{hra:.2f}")
    print(f"Travel allowance: ₹{travel:.2f}")
    print(f"Overtime pay    : ₹{overtime_pay:.2f}")
    print(f"Incentive       : ₹{incentive:.2f}")
    print(f"Gross salary    : ₹{gross:.2f}")
    print(f"Deduction       : ₹{deduction:.2f}")
    print(f"Net salary      : ₹{net:.2f}")
