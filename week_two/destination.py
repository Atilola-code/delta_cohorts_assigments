store = ["United state", "Canada", "Italy"]
print("Welcome to Emirate Airways. What destination do you have in mind?")
options = input(" 1. Add a destination:\n2. Delete a destination:\n3. Make an enquiry ")
if options == "1":
    destination = input("What destination do you want to add in here?: ")
    store.append(destination)
    print(f"Destination has been added", store)
elif options == "2":
    deletion = input("enter the destionation you want to delete: ")
    store.remove(deletion)
    print(store)
elif options == "4":
    print(store)
else:
    print("No option was added")




#     print("Proceed to book a ticket")
# elif options == 2:
#     print("Option not available at the moment")
