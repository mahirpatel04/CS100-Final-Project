from classes.Calendar import Calendar
from classes.Month import Month
from classes.Week import Week
from classes.Day import Day
from classes.Event import Event
from datetime import date
from classes.Display import DisplayClient
from datetime import date

import sys
import os

sys.path.append(os.getcwd()) # fixing module not found error for classes


#todaysDate = date.today()

displayer = DisplayClient()
#calendar = Calendar(todaysDate,)

#print("hi")

# STEP 1: Welcome Message
# displayer.displayWelcome()

# STEP 2: Main Menu
displayer.displayMenu()

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