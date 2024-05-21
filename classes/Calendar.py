from datetime import date
# from classes.Month import Month
class Calendar:
    def __init__(self, todaysDate: date) -> None:
        
        self.days = []
        currDate = todaysDate
        for i in range(365):
            currDate = date(todaysDate.year, todaysDate.month, todaysDate.day + i)
            self.days.append(currDate)

    def removeMonth():
        pass
    def addEvent():
        pass
    def addMonth():
        pass
    def editEvent():
        pass
    def removeEvent():
        pass
    def searchEvent():
        pass
    