print('===== Welcome to Dhruva Bank=====')
b = 10000

while True:
    print("\n\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit\n")
    op = int(input('Choose an option: '))

    match op:
        case 1:
            print(f"The amount in your account is ₹{b}")
        case 2:
            d = int(input('Enter amount to deposit: '))
            b += d
            print(f"Amount deposited successfully. New balance: ₹{b}")
        case 3:
            w = int(input('Enter amount to withdraw: '))
            if w > b:
                print("Insufficient Balance ❌")
            else:
                b -= w
                print(f"Withdrawal successful. New balance: ₹{b}")
        case 4:
            print("Thank you for using Dhruva Bank. Visit Again! 🏦")
            break
        case _:
            print("Invalid option. Please try again.")
