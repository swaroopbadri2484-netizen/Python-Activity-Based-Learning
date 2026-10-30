balance = 5000.0
successful = 0
deposits = 0.0
withdrawals = 0.0
count = int(input("Number of transactions: "))

for i in range(count):
    kind = input("Transaction type (deposit/withdraw): ").lower()
    amount = float(input("Amount (₹): "))

    if amount <= 0:
        print("Rejected: amount must be positive.")
    elif kind == "deposit":
        balance += amount
        deposits += amount
        successful += 1
        print(f"Deposit accepted. Balance: ₹{balance:.2f}")
    elif kind == "withdraw":
        if amount > 10000:
            print("Rejected: withdrawal limit is ₹10000.")
        elif amount > balance:
            print("Rejected: insufficient balance.")
        else:
            balance -= amount
            withdrawals += amount
            successful += 1
            print(f"Withdrawal accepted. Balance: ₹{balance:.2f}")
    else:
        print("Rejected: unknown transaction type.")

print("\n------ TRANSACTION SUMMARY ------")
print(f"Opening balance : ₹5000.00")
print(f"Total deposits  : ₹{deposits:.2f}")
print(f"Total withdrawals: ₹{withdrawals:.2f}")
print(f"Successful transactions: {successful}")
print(f"Closing balance : ₹{balance:.2f}")
