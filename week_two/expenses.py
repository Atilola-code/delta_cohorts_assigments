expenses = [
    ["Transportation", 85000.00],
    ["Food", 200000.00]
]

while True:
    option = input("1. Add an expense\n2. View Expenses\n3. Show total expenses.\n4. Exit.\n5. Delete Expense\n.(Choose 1|2|3|4|5): ")
    if option == "1":
        expense = input("Write your expense here: ")
        amount = input("Write the amount of the expense: ")
        expenses.append([expense, float(amount)])
        print("Expense is successfully added.")
        
    elif option == "2":
        for exp in expenses:
            print(f"{"--" * 21}\nExpense: {exp[0]}, Amount: {exp[1]}\n{"--" * 21}")
    elif option == "3":
        total_amount = 0
        for exp in expenses:
            total_amount = total_amount + exp[1]
        else:
            if total_amount == 0:
                print(f"{"--" * 21}\nYou are broke. You need to work smart and make right connections.\n{"--" * 21}")
            print(f"{"--" * 21}\nYour total amount is {total_amount}.\n{"--" * 21}")
    elif option == "4":
        choice = input("Are you sure you want to exit? (Yes|No): ")
        if choice == "Yes":
            print(f"{"--" * 21}\nLeaving the expense tracker.\n{"--" * 21}")
            break
        elif choice == "No":
            continue
        else:
            print("Invalid response. Returning to main menu. ")

    elif option == "5":
        choice = input("Enter the number of the expenses you want to delete(or type 'cancel' to abort): ")
        if choice == "Cancel":
             continue
        elif choice.isdigit() and 1 <= float(choice) <= len(expenses):
            deleted = expenses.pop(int(choice) - 1)
        print(f"Expenses '{deleted[0]}' deleted.")
    else:
         print("Invalid choice.")
         break
    