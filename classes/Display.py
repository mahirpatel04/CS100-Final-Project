from classes.Event import Event
from classes.Calendar import Calendar
from classes.Week import Week
from datetime import date, timedelta

class DisplayClient:
    def displayWelcome(self):
        print("Welcome to R'Agenda! You can plan and schedule events in this text-based planner.\n")

    def displayMenu(self):
        print("MAIN MENU")
        print("Select 1 to ADD an event")
        print("Select 2 to REMOVE an event")
        print("Select 3 to EDIT an event")
        print("Select 4 to VIEW your calendar")
        print("Select 5 to SAVE your calendar")
        print("Select 6 to EXIT")
        
    def displayAllEvents(self, calendar: Calendar):
        for month in calendar.months:
            for week in month.weeks:
                for day in week.days:
                    for event in day.events:
                        print(event)
        print("\n")
        
    def viewWeek(self, week):
        for day in week.days:
            print(day.date)
            print("-" * 20)
            for event in day.events:
                print(event)

            
        