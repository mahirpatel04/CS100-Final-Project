from classes.Day import Day

import sys
import os

sys.path.append(os.getcwd()) # fixing module not found error for classes

class Week:
    def __init__(self, listOfDays) -> None:
        self.days = [Day(day) for day in listOfDays]

    def removeDay():
        pass
    def addEvent():
        pass
    def addDay():
        pass
    def editEvent():
        pass
    def removeEvent():
        for item in self.days:
            item.removeEvent()
    def searchEvent():
        pass