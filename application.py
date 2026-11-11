tickets = []

def create_ticket():
    name = input("Enter your name: ")
    issue = input("Describe your issue: ")
    priority = input("Enter priority (Low, Medium, High): ")

    ticket = {
        "id": len(tickets) + 1,
        "name": name,
        "problem": issue,
        "priority": priority,
        "status": "Open"
    }
    tickets.append(ticket)
    print("Ticket created successfully!")

def show_tickets():
    if not tickets: # oder if len(tickets) == 0
        print("No tickets found.")

    else: 
     for ticket in tickets:
        
        print("--------------------------------")
        print(f"Ticket ID: {ticket['id']}")
        print(f"Name: {ticket['name']}")
        print(f"Issue: {ticket['problem']}")
        print(f"Priority: {ticket['priority']}")
        print(f"Status: {ticket['status']}")
        print("--------------------------------")
        print("\n")
        

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
        print("Ticket is being created, plwease wait...")
        create_ticket()

    elif choice == "2":
        print("The following exisitting tickets:")
        show_tickets()

    elif choice == "3":
        print("Thank you for using IT Helpdesk!")
        break

    elif choice == "4":
        print("Please contact: itsupport@company.com")

    else:
        print("Invalid option. Please try again.")