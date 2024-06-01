from classes.Calendar import Calendar
from classes.InputHandler import InputHandler
from classes.Display import DisplayClient


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
    quitChoice = inputHandler.getQuitChoice()
    calendar.handleQuitChoice(quitChoice, displayer, inputHandler)
    