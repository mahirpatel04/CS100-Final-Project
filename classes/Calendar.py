from datetime import date, timedelta
from classes.Month import Month # need to have full path not just the file name


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
                self.months.append(Month(currMonthList, currMonthNum))
                currMonthNum += 1
                if currMonthNum == 13:
                    currMonthNum = 1
                currMonthList = [currDay]
                
            currDay += timedelta(days=1)
        
        self.months.append(Month(currMonthList, currMonthNum))
        
        # WE END WITH 1 LIST OF 12/13 MONTHS
            
    

    def removeMonth():
        pass
    def addEvent(self, eventToAdd):
        monthObject = self.findMonth(eventToAdd.date)

        monthObject.addEvent(eventToAdd)
        # print("HELLO HELLO HELP:", eventToAdd.date, "!!!!")
        
    def findMonth(self, date):
        m = date.month
        currMonthNum = self.months[0].monthNum
        offset = m - currMonthNum
        return self.months[offset]
    
    
    def findWeek(self, date):
        monthObject = self.findMonth(date)
        for week in monthObject.weeks:
            for day in week.days:
                if day.date == date:
                    return week
        
        
    def addMonth():
        pass
    def editEvent():
        pass
    def removeEvent(self):
        for item in self.months:
            item.removeEvent()
    def searchEvent():
        pass
