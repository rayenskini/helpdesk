print("================================")
print("       IT HELPDESK SYSTEM")
print("================================")

while True:
    print("\nPlease select an option:")
    print("1. Create a new ticket")
    print("2. View all tickets")
    print("3. Exit")
    print("4. Contact IT Support")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print("You selected: Create a new ticket")

    elif choice == "2":
        print("You selected: View all tickets")

    elif choice == "3":
        print("Thank you for using IT Helpdesk!")
        break

    elif choice == "4":
        print("Please contact: itsupport@company.com")

    else:
        print("Invalid option. Please try again.")