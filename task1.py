Name=input("Enter the name:")
balance=float(input("Enter the balance:"))
print("1.Deposit","2.withdraw","3.Balance")
choice=int(input("Enter your choice(1/2/3)"))
if(choice==1):
  amount=int(input("Enter your amount to deposit:"))
  if amount>0:
    balance=balance+amount
    print(balance)
  else:
    print("Invalid amount")
elif(choice==2):
  amount=int(input("Enter amount for withdraw:"))
  if amount<balance:
    balance=balance-withdraw
    print("Balance amount",balance)
  else:
    print("invalid amount")
elif(choice==3):
  print("Account name",Name)
  print("Balance",balance)
else:
  print("Invalid choice!!")
