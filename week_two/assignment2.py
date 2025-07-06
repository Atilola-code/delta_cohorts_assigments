Transactions = []
correct_pin = "1234"

while True:
    user_pin = input("Please enter your four-digit pin to proceed: ")
    if user_pin == correct_pin:
        print("Welcome to Naija Simple ATM, what do you want to do today?" )
        break
    else: 
            print("Incorrect pin, please try again")

while True:
    option = input("1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit:\nChoose an option (1-4): ")
    if option == "1":
        savings = 0
        for dep in Transactions:
            savings += dep
        print(f"Your balance is: {savings} naira") 

    elif option == "2":
        deposit_amount = input("How much do you want to deposit? ")
        if deposit_amount.replace(".", "").isdigit():
            Transactions.append(float(deposit_amount))
            print(f"{deposit_amount} naira deposited successfully. Thank you for banking with us! ")
        else:
            print("Invalid amount. Please enter a valid amount")

    elif option == "3":
        withdraw_amount = input("How much do you want to withdraw? ")
        if  withdraw_amount.replace(".", "").isdigit():
            withdraw_amount = float(withdraw_amount)
            savings = 0
            for dep in Transactions:
                savings += dep
            if withdraw_amount > savings:
                    print("insufficient balance. Please enter a lower amount")
            else:
                    Transactions.append(-withdraw_amount)
                    print("Withdrawal successful. Thank you for banking with Us!")

    elif option == "4":
        choice = input("Are you sure you want to exit?: (Yes/No) ")
        if choice == "Yes":
            print("Thank you for choosing Naija Simple ATM. Goodbye!")
            break
        elif choice == "No":
            continue


                 


    

        









