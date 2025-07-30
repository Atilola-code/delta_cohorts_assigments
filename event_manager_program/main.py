class Event:
    def __init__(self, event_id, name, date, capacity):
        self.event_id = event_id
        self.name = name
        self.date = date
        self.capacity = capacity
        self.ticket_sold = 0

    def has_space(self):
        return self.ticket_sold < self.capacity  # Check if there are still tickets available
    
    def sell_ticket(self):
        if self.has_space():
            self.ticket_sold += 1  # Increment ticket count if space is available
            return True
        return False
    
    # Attendee class represents a participant who can hold tickets to events
class Attendee:
    def __init__(self, attendee_id, name, email):
        self.attendee_id = attendee_id
        self.name = name
        self.email = email
        self.tickets = []   # Stores IDs of events this attendee has tickets for
        
    def add_ticket(self, event_id):  # Add an event ID to the attendee's list
        self.tickets.append(event_id)

    def remove_ticket(self, event_id):  # Remove an event ID if present
        if event_id in self.tickets:
            self.tickets.remove(event_id)
            return True
        return False
    
    # Ticket class connects an attendee with an event
class Ticket:
    def __init__(self, event_id, attendee_id):
     self.event_id = event_id
     self.attendee_id = attendee_id
    

# EventManager class manages all events, attendees, and ticket transactions
class EventManager:
    def __init__(self):
        self.events = {}
        self.attendees = {}
        self.tickets = []

    def add_event(self, event_id, name, date, capacity):
        if event_id not in self.events:
            self.events[event_id] = Event(event_id, name, date, capacity)
            print(f"Event with the name '{name}' has been added.")
        else:
            print(f"Event's ID already exists, please recheck ID")
        return False

    def register_attendee(self, attendee_id, name, email):
        if attendee_id not in self.attendees:
            self.attendees[attendee_id] = Attendee(attendee_id, name, email)
            print(f"Attendee with the name '{name}' has been added.")
        else:
            print(f"Attendee's ID already registered, please recheck ID")
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
            print(f"Ticket sold to '{attendee.name}' for event '{event.name}' ")
        else:
            print("No Ticket available for this event.")
    
    def check_availability(self, event_id):
        if event_id in self.events:
            event = self.events[event_id] 
            availability = event.capacity - event.ticket_sold  # Calculate remaining tickets
            print(f"Ticket available for '{event.name}': {availability}")
            return availability
        else:
            print("Event not found.")
            return 0
        
    def lookup_attendee(self, attendee_id):
        if attendee_id in self.attendees:
            attendee = self.attendees[attendee_id]
            print(f"Ticket found for {attendee.name}:")
            for event_id in attendee.tickets:
            # Get the event name or show cancelled event if it's been removed
                event_name = self.events[event_id].name if event_id in self.events else "Cancelled event"
                print(f"Event name: {event_name} (ID: {event_id})")
        else:
            print("Attendee not found.")



    def run_program(self):
        print(f"{"==" * 24}\n Welcome to the Event Management Program!\n{"==" * 24}")
        while True:
            print("Please make a selection:\n1. Add an event\n2. Register Attendee\n3. Sell Ticket\n4. Lookup Attendee\n5. Check Ticket Availability\n6. Exit")
            choice = input("Choose from option (1 - 6): ")
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

            # Register Attendee
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
            # Sell Ticket
            elif choice == "3":
                while True:
                    try:
                        event_id = int(input("Enter the Event's ID: "))
                        attendee_id = int(input("Enter the Attendee's ID: "))
                        self.sell_ticket(event_id, attendee_id)
                    except ValueError:
                        print("Invalid input, please try again")

                    repeat_ticket_choice = input("Do you want to buy another ticket? (Yes | No): ").strip().lower()
                    if repeat_ticket_choice == "yes":
                        continue
                    elif repeat_ticket_choice == "no":
                        break
            # Lookup Attendee
            elif choice == "4":
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
            # Check Ticket Availability
            elif choice == "5":
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
            # Exit Program
            elif choice == "6":
                print("Exiting the program. Thank you for choosing us")
                break
            else:
                print("Invalid choice, please select from option 1 - 6")
                

if __name__ == "__main__":
    manager = EventManager()
    manager.run_program()
