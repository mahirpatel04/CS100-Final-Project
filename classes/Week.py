from classes.Day import Day

import sys
import os

sys.path.append(os.getcwd()) # fixing module not found error for classes

class Week:
    def __init__(self, listOfDays) -> None:
        self.days = [Day(day) for day in listOfDays]

    def removeDay(self):
        pass
    def addEvent(self):
        pass
    def addDay(self):
        pass
    def editEvent(self):
        pass
    def removeEvent(self):
        for item in self.days:
            item.removeEvent()
    def searchEvent(self):
        pass