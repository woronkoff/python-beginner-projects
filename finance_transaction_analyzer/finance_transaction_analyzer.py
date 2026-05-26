data = [
  (749.17, "Investment Return"),
  (-11.54, "Utilities"),
  (-247.58, "Online Shopping"),
  (981.17, "Investment Return"),
  (-410.65, "Rent"),
  (310.60, "Rent"),
  (563.70, "Gift"),
  (220.79, "Salary"),
  (-49.85, "Car Maintenance"),
  (308.49, "Salary"),
  (-205.55, "Car Maintenance"),
  (870.64, "Salary"),
  (-881.51, "Utilities"),
  (518.14, "Salary"),
  (-264.66, "Groceries")
]

def print_transactions(transactions):
  for transaction in transactions:
    amount, statement = transaction
    print(f"${amount} - {statement}")

def print_summary(transactions):
  deposits = [transaction[0] for transaction in transactions if transaction[0] >= 0]
  total_deposited = sum(deposits)
  print(f"Deposited: {total_deposited}")
  withdrawals = [transaction[0] for transaction in transactions if transaction[0] < 0]
  total_withdrawan = sum(withdrawals)
  print(f"Withdrawan: {total_withdrawan}")
  balance = total_deposited + total_withdrawan
  print(f"Balance: {balance:.2f}")

def analyze_transactions(transactions):
  transactions.sort()
  largest_withdrawal = transactions[0]
  largest_deposit = transactions[-1]
  print(f"Largest withdrawals: {largest_withdrawal}")
  print(f"Largest deposit: {largest_deposit}")

  deposits = [transaction[0] for transaction in transactions if transaction[0] >= 0]
  total_deposit = sum(deposits)
  average_deposit = total_deposit / len(deposits) if deposits else 0
  print(f"Average deposit: {average_deposit:.2f}")

  withdrawals = [transaction[0] for transaction in transactions if transaction[0] < 0]
  total_withdrawan = sum(withdrawals)
  average_withdrawan = total_withdrawan / len(withdrawals) if withdrawals else 0
  print(f"Average withdrawals: {average_withdrawan:.2f}")

while True:
  print("1. Print Summary\n2. Analyze Transactions\n3. Close Program")
  option = int(input("Choose an Option above: "))
  if option == 1:
    print_summary(data)
  elif option == 2:
    analyze_transactions(data)
  elif option == 3:
    break
  else:
    print("Invalid choice")