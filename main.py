from classes.Calendar import Calendar
from classes.Month import Month
from classes.Week import Week
from classes.Day import Day
from classes.Event import Event
from classes.InputHandler import InputHandler
from datetime import date
from classes.Display import DisplayClient
from datetime import date

displayer = DisplayClient()
calendar = Calendar()
inputHandler = InputHandler()

# STEP 1: Welcome Message

displayer.displayWelcome()
continueChoice = inputHandler.getContinue()
while continueChoice != "C":
    continueChoice = inputHandler.getContinue()
    
    
# STEP 2: Main Menu

displayer.displayMenu()

# Get menu choice

menuChoice = inputHandler.getMenuChoice(calendar)
while menuChoice != "6":
    # Handle their old choice
    calendar.handleUserChoice(menuChoice, displayer, inputHandler)
    # Display the menu again
    displayer.displayMenu()
    # Get new Menu Choice
    menuChoice = inputHandler.getMenuChoice(calendar)
else:
    print("User wants to quit, handle saving progress into txt file here")
'''
try:
    while menuChoice != "Quit":
        calendar.handleUserChoice(menuChoice, displayer, inputHandler)
    
except EOFError:
    print("Done reading from file. Remove this try/except block for final iteration of product")
    '''
# STEP 3: Get Input
#while input("Enter your choice: ") != "q":
    
    #print("do something")
    







# STEP 2: Main loop:
    # STEP 3: Display Menu
    # STEP 4: Do Whatever User Asks
    # STEP 5: Menu Again
    
    # rinse and repeat
    
# Upon exit:
    # STEP 6: Show exit message
    # STEP 7: Terminate program