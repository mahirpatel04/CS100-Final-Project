from datetime import datetime
from classes.Event import Event
# from classes.Calendar import Calendar

class InputHandler:
    def getContinue(self):
        return input()
    
    def getChoice(self, calendar, display):
        choice = input("Enter your input: ")
        if choice == '1':
            event = self.getEventInfo()
            calendar.addEvent(event)
            print("Event adding... <FIX_ME>")
            return 
        elif choice == '2':
            print("Event removed... <FIX_ME>")
        elif choice == '3':
            print("Event edited... <FIX_ME>")
        elif choice == '4':
            week = self.getWeek(calendar)
            display.viewWeek(week)
            print("Viewing entire schedule... <FIX_ME>")
        elif choice == '5':
            print("Saving entire schedule... <FIX_ME>")
        elif choice == '6':
            print("Exiting calendar... <FIX_ME>")
            return "Quit"
        else:
            print("Invalid choice. Please try again.")
            return False
            
    def getWeek(self, calendar):
        date = input("Enter date in form YYYY-MM-DD: ")
        date = datetime.strptime(date, "%Y-%m-%d").date()
        
        return calendar.findWeek(date)
        
        
        
        
        
        
    def getEventInfo(self):
        title = input("Enter title of your event: ")
        date = input("Enter date in form YYYY-MM-DD: ")
        startTime = input("Enter start time of event as HH:MM in 24 hour time: ")
        endTime = input("Enter end time of event as HH:MM in 24 hour time: ")
        
        startTime = datetime.strptime(startTime, "%H:%M").time()
        endTime = datetime.strptime(endTime, "%H:%M").time()
        
        date = datetime.strptime(date, "%Y-%m-%d").date()
        desc = input("Enter description of your event: ")
        
        return Event(title, startTime, endTime, date, desc)
        
        
    def get_event_from_user(self):
        title = input("Enter the event title: ")
        start_time_str = input("Enter the event start time (HH:MM): ")
        end_time_str = input("Enter the event end time (HH:MM): ")
        description = input("Enter a description for the event: ")

        # Convert start and end time to datetime objects
        start_time = datetime.strptime(start_time_str, "%H:%M").time()
        end_time = datetime.strptime(end_time_str, "%H:%M").time()

        # event_id placeholder
        event_id = 1340981

        # Create an Event instance using Event constructor
        return Event(title, start_time, end_time, event_id, description)
