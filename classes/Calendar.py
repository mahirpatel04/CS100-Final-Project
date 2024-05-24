from datetime import date, timedelta
from Month import Month
# from classes.Month import Month
class Calendar:
    def __init__(self) -> None:
        # CREATES EMPTY MONTH, EMPTY CURR MONTH, AND 
        # GETS TODAY's DATE
        self.months = []          
        currMonthList = []
        currDay = date.today()
        currMonthNum = currDay.month
        
        # ADD THE 365 DAYS INTO THE CALENDAR
        for i in range(365):
            if currDay.month == currMonthNum:
                currMonthList.append(currDay)
            else:
                self.months.append(Month(currMonthList))
                currMonthNum += 1
                if currMonthNum == 13:
                    currMonthNum = 1
                currMonthList = [currDay]
                
            currDay += timedelta(days=1)
        
        self.months.append(Month(currMonthList))
        
        # WE END WITH 1 LIST OF 12/13 MONTHS
            
    
    def removeMonth():
        pass
    def addEvent():
        pass
    def addMonth():
        pass
    def editEvent():
        pass
    def removeEvent(self):
        for item in self.months:
            item.removeEvent()
    def searchEvent():
        pass
