from Event import Event
from datetime import date

class DisplayClient:
    def displayWelcome(self):
        """
        Args: N/A
        
        Return: N/A
        
        Description: Displays the welcome message at the beginning of the program
        """
        print("Welcome to R'Agenda")
        return
    def displayMenu(self):
        """

        Args:
        
        Return:
        
        Description:
        """
        print("This is menu")
        print("1. ")
        print("2. ")
        return

    def displayEvent(self, event):
        """
        Args: N/A
        
        Return: N/A
        
        Description: Prints the main menu
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


       
    def displayEvent(self, event):
        print(event)
        return

