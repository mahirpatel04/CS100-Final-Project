from datetime import date, timedelta
from classes.Week import Week
from classes.Day import Day

from typing import List

import sys
import os

sys.path.append(os.getcwd()) # fixing module not found error for classes



class Month:
    def __init__(self, listOfDays: List[date], monthNum) -> None:
        self.monthNum = monthNum
        # Adding the days at the beginning
        firstDay = listOfDays[0]
        offset = firstDay.weekday()
        for i in range(1, offset + 1):
            listOfDays.insert(0, firstDay - timedelta(i))
        
        # Adding the days at the end
        lastDay = listOfDays[-1]
        offsetEnd = 7 - lastDay.weekday()
        for i in range(1, offsetEnd):
            listOfDays.append(lastDay + timedelta(i))
        
        # Spliting up the list of Days into Weeks
        currWeekDays = []
        self.weeks = []
        for day in listOfDays:
            if day.weekday() == 0:
                currWeekDays = [day]
            elif day.weekday() == 6:
                currWeekDays.append(day)
                self.weeks.append(Week(currWeekDays))
                currWeekDays = []
            else:
                currWeekDays.append(day)
                
    def removeWeek():
        pass
    def addEvent(self, eventToAdd):
        for week in self.weeks:
            for day in week.days:
                if day.date == eventToAdd.date:
                    day.addEvent(eventToAdd)
        
    def addWeek():
        pass
    def editEvent():
        pass
    def removeEvent(self):
        for item in self.weeks:
            item.removeEvent()
    def searchEvent():
        pass