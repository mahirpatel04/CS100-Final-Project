from Event import Event
from Calendar import Calendar
from Week import Week
from datetime import date, timedelta

import sys
import os

sys.path.append(os.getcwd()) # fixing module not found error for classes

class DisplayClient:
    def displayWelcome(self):
        """        
        Displays the welcome message at the beginning of the program
        """
        choice = ""
        print("Welcome to R'Agenda! You can plan and schedule events in this text-based planner.\nPress 'C' to continue...")
        choice = input()
        return choice

    def displayMenu(self):
        """

        """
        choice = self.displayWelcome()

        while choice != 'C':
            choice = self.displayWelcome()

        print("MAIN MENU")
        print("Select 1 to ADD an event")
        print("Select 2 to REMOVE an event")
        print("Select 3 to EXIT")


    def displayEvent(self, event):
        """_summary_

        Args:
            event (_type_): _description_
        """
        print("Enter 1 to ADD an event")
        print("Enter 2 to REMOVE an event")
        print("Enter 3 to EDIT an event")
        print("Enter 4 to VIEW your entire schedule")
        print("Enter 5 to SELECT an event")
        print("Enter 6 to EXIT")

        choice = input()

        # if choice == '1': #ADD EVENT
        #     print("adding event...")
        # if choice == '2': #REMOVE EVENT
        #     print("remove an event..")
        # if choice == '3': #EDIT EVENT
        #     print("edit an event..")
        # if choice == '4': #VIEW EVERYTHING
        #     print('view your entire schedule..')
        # if choice == '5': #SELECT AN EVENT
        #     print('select an event..')
        # if choice == '6': #EXIT
        #     print('select to exit..')
        # return

        #logic for main menu 

        if choice == '1':
            #addEvent()
            print("Event added successfully!")
        elif choice == '2':
            #removeEvent()
            print("Event removed successfully!")
        elif choice == '3':
            #editEvent()
            print("Event edited successfully!")
        elif choice == '4':
            print("Viewing entire schedule...")
        elif choice == '5':
            print("Selecting event...")
        elif choice == '6':
            print("Exiting program...")
            #break
        else:
            print("Invalid choice. Please try again.")


       
    def displaySpecificEvent(self, event):
        """_summary_

        Args:
            event (_type_): _description_
        """
        print(event)
        return

    def displayAllEvents(self, calendar: Calendar):
        for month in calendar.months:
            for week in month.weeks:
                for day in week.days:
                    for event in day.events:
                        print(event)

