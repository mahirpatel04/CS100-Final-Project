from classes.Day import Day
from classes.InputHandler import InputHandler

import sys
import os

sys.path.append(os.getcwd()) # fixing module not found error for classes

class Week:
    def __init__(self, listOfDays) -> None:
        self.days = [Day(day) for day in listOfDays]

    def removeEvent(self):
        i = InputHandler()
        for item in self.days:
            item.removeEvent(i)