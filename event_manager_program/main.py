class Event:
    def __init__(self, event_id, name, date, capacity):
        self.event_id = event_id
        self.name = name
        self.date = date
        self.capacity = capacity
        self.ticket_sold = 0

    def has_space(self):
        return self.ticket_sold < self.capacity
    
    def sell_ticket(self):
        if self.has_space():
            self.ticket_sold += 1
            return True
        return False
    
    def refund_ticket(self):
        if self.ticket_sold > 0:
            self.ticket_sold -= 1
            return True
        return False
    
class Attendee:
    def __init__(self, attendee_id, name, email):
        self.attendee_id = attendee_id
        self.name = name
        self.email = email
        self.tickets = []
        
    def add_ticket(self, event_id):
        self.tickets.append(event_id)

    def remove_ticket(self, event_id):
        if event_id in self.tickets:
            self.tickets.remove(event_id)
            return True
        return False
    
class Ticket:
    def __init__(self, event_id, attendee_id):
     self.event_id = event_id
     self.attendee_id = attendee_id
    


class EventManager:
    def __init__(self):
        self.events = {}
        self.attendees = {}
        self.tickets = []

    def add_event(self, event_id, name, date, capacity):
        if event_id not in self.events:
            self.events[event_id] = Event(event_id, name, date, capacity)
            print(f"✅ Event with the name '{name}' has been added.")
        else:
            print(f"❌ Event's ID already exists, please recheck ID")
        return False

    def register_attendee(self, attendee_id, name, email):
        if attendee_id not in self.attendees:
            self.attendees[attendee_id] = Attendee(attendee_id, name, email)
            print(f"✅ Attendee with the name '{name}' has been added.")
        else:
            print(f"❌ Attendee's ID already registered, please recheck ID")
            return False

    def sell_ticket(self, event_id, attendee_id):
        if event_id not in self.events:
            print("Event does not exist. Please check again.")
            return
        if attendee_id not in self.attendees:
           print("Attendee not registered. Please check again.") 
           return
        
        event = self.events[event_id]
        attendee = self.attendees[attendee_id]
        if event.sell_ticket():
            attendee.add_ticket(event_id)
            self.tickets.append(Ticket(attendee_id, event_id))
            print(f"🎟️ Ticket sold to '{attendee.name}' for event '{event.name}' ")
        else:
            print("🚫 No Ticket available for this event.")

    def refund_ticket(self, event_id, attendee_id):
        if event_id not in self.events or attendee_id not in self.attendees:
            print("Invalid event or attendee ID")
            return
        
        event = self.events[event_id]
        attendee = self.attendees[attendee_id]

        if not attendee.remove_ticket(event_id):
            print("❌ Ticket not found for this attendee")
            return
        if not event.refund_ticket():
            print("❌ Could not process event refund")
            return
        ticket_refunded = False
        new_ticket_list = []
        for ticket in self.tickets:
            if not (ticket.attendee_id == attendee_id and ticket.event_id == event_id):
                new_ticket_list.append(ticket)
            else:
                ticket_refunded = True
        self.tickets = new_ticket_list
        if ticket_refunded:
                print(f"💵 Ticket refunded for '{attendee.name}' from event '{event.name}'. ")
        else:
                print("❌ Ticket record not found or already refunded.")

    def cancel_event(self, event_id):
        if event_id not in self.events:
            print("❌ Event not found!")
            return
        event = self.events.pop(event_id)
        print(f"🚫 Event '{event.name}' cancelled")

# Remove all tickets related to the cancelled event
        deleted_tickets = []
        for ticket in self.tickets:
            if ticket.event_id != event_id:
                deleted_tickets.append(ticket)
        self.tickets = deleted_tickets

# Remove event ID from all attendee ticket lists
        for attendee in self.attendees.values():
            updated_event = []
            for deleted_event in attendee.tickets:
                if deleted_event != event_id:
                  updated_event.append(deleted_event)
                  attendee.tickets = updated_event
    
    def check_availability(self, event_id):
        if event_id in self.events:
            event = self.events[event_id] 
            availability = event.capacity - event.ticket_sold
            print(f"🎟️ Ticket available for '{event.name}': {availability}")
            return availability
        else:
            print("❌ Event not found.")
            return 0
        
    def lookup_attendee(self, attendee_id):
        if attendee_id in self.attendees:
            attendee = self.attendees[attendee_id]
            print(f"🔎 Ticket found for {attendee.name}:")
            for event_id in attendee.tickets:
                event_name = self.events[event_id].name if event_id in self.events else "Cancelled event"
                print(f"Event name: {event_name} (ID: {event_id})")
        else:
            print("❌ Attendee not found.")



    def run_program(self):
        print(f"{"==" * 24}\n Welcome to the Event Management Program!\n{"==" * 24}")
        while True:
            print("Please make a selection:\n1. Add an event\n2. Register Attendee\n3. Sell Ticket\n4. Refund Ticket\n5. Cancel Event\n6. Lookup Attendee\n7. Check Ticket Availability\n8. Exit")
            choice = input("Choose from option (1 - 8): ")
            if choice == "1":
                while True:
                    try:
                        event_id = int(input("Enter the Event's ID: "))
                        name = input("Enter the name of the event: ")
                        date = str(input("Enter the date of the event (YYYY-MM-DD): "))
                        capacity = int(input("Enter the capacity of the event (in number): "))
                        self.add_event(event_id, name, date, capacity)
                    except ValueError:
                        print("Invalid input, please try again")

                    repeat_choice = input("Do you want to add another event? (Yes | No): ").strip().lower()
                    if repeat_choice == "yes":
                        continue
                    elif repeat_choice == "no":
                        break

    
            elif choice == "2":
                while True:
                    try:
                        attendee_id = int(input("Enter the Attendee's ID: "))
                        name = input("Enter the Attendee's name: ")
                        email = input("Enter the Attendee's email(must include an @): ")
                        self.register_attendee(attendee_id, name, email)
                    except ValueError:
                        print("Invalid input, please try again")

                    repeat_a_choice = input("Do you want to add another attendee? (Yes | No): ").strip().lower()
                    if repeat_a_choice == "yes":
                        continue
                    elif repeat_a_choice == "no":
                        break

            elif choice == "3":
                while True:
                    try:
                        event_id = int(input("Enter the Event's ID: "))
                        attendee_id = int(input("Enter the Attendee's ID: "))
                        self.sell_ticket(attendee_id, event_id)
                    except ValueError:
                        print("Invalid input, please try again")

                    repeat_ticket_choice = input("Do you want to buy another ticket? (Yes | No): ").strip().lower()
                    if repeat_ticket_choice == "yes":
                        continue
                    elif repeat_ticket_choice == "no":
                        break

            elif choice == "4":
                 while True:
                    try:
                        event_id = int(input("Enter the Event's ID: "))
                        attendee_id = int(input("Enter the Attendee's ID: "))
                        self.refund_ticket(event_id, attendee_id)
                    except ValueError:
                        print("Invalid input, please try again")
                    break

            elif choice == "5":
                 while True:
                    try:
                        event_id = int(input("Enter the Event's ID to cancel: "))
                        self.cancel_event(event_id)
                    except ValueError:
                        print("Invalid input, please try again")
                    repeat_cancel_choice = input("Do you want to cancel another event? (Yes | No): ").strip().lower()
                    if repeat_cancel_choice == "yes":
                        continue
                    elif repeat_cancel_choice == "no":
                        break
            elif choice == "6":
                 while True:
                    try:
                        attendee_id = int(input("Enter the Attendee's ID to look up: "))
                        self.lookup_attendee(attendee_id)
                    except ValueError:
                        print("Invalid input, please try again")
                    repeat_lookup_choice = input("Do you want to look up another attendee? (Yes | No): ").strip().lower()
                    if repeat_lookup_choice == "yes":
                        continue
                    elif repeat_lookup_choice == "no":
                        break
            elif choice == "7":
                 while True:
                    try:
                        event_id = int(input("Enter the Event's ID to check availability: "))
                        self.check_availability(event_id)
                    except ValueError:
                        print("Invalid input, please try again")
                    repeat_available_choice = input("Do you want to check for another event's availability? (Yes | No): ").strip().lower()
                    if repeat_available_choice == "yes":
                        continue
                    elif repeat_available_choice == "no":
                        break
            elif choice == "8":
                print("Exiting the program. Thank you for choosing us")
                break
            else:
                print("❌ Invalid choice, please select from option 1 - 8")
                

                

                

if __name__ == "__main__":
    manager = EventManager()
    manager.run_program()
