#from Event import Event
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
        Args: N/A
        
        Return: N/A
        
        Description: Prints the main menu
        """
        print("Enter 1 to REMOVE week")
        print("Enter 2 to ADD an event")
        print("Enter 3 to ADD a Week")
        print("Enter 4 to VIEW your entire schedule")
        print("Enter 5 to SELECT an event")
        print("Enter 6 to EXIT")

        choice = input()

        if choice == '1': #ADD EVENT
            print("adding event...")
        if choice == '2': #REMOVE EVENT
            print("remove an event..")
        if choice == '3': #EDIT EVENT
            print("edit an event..")
        if choice == '4': #VIEW EVERYTHING
            print('view your entire schedule..')
        if choice == '5': #SELECT AN EVENT
            print('select an event..')
        if choice == '6': #EXIT
            print('select to exit..')
        return

    #def displayEvent(self, event):
        #print(event)
        #return