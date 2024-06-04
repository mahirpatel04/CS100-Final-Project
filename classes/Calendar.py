from datetime import date, timedelta
from classes.Month import Month # need to have full path not just the file name
from classes.Event import Event
from datetime import datetime
from classes.InputHandler import InputHandler
class Calendar:
    def __init__(self) -> None:
        # CREATES EMPTY MONTH, EMPTY CURR MONTH, AND 
        # GETS TODAY's DATE
        self.months = []          
        currMonthList = []
        self.possibleChoices = ["1", "2", "3", "4", "5", "6"]
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
            
    def handleUserMenuChoice(self, choice, display, inputHandler):
        if choice == '1':
            event = inputHandler.getEventInfo()
            self.addEvent(event)
            return True
        
        elif choice == '2':
            self.removeEvent(inputHandler)
            print("Event removed successfully")
            
        elif choice == '3':
            self.editEvent(inputHandler)
            print("Event edited successfully")
            
        elif choice == '4':
            week = inputHandler.getWeek(self)
            display.viewWeek(week)
            
        elif choice == '5':
            file = inputHandler.getFileName()
            self.saveToFile(file)
            print("Saving entire schedule")
            
        elif choice == '6':
            print("Exiting calendar")
            return "Quit"
        
        else:
            print("Invalid choice. Please try again.")
            return False
    
    def handleSaveChoice(self, choice, display, inputHandler):
        if choice == "N":
            return
        elif choice == "Y":
            file = inputHandler.getFileName()
            self.saveToFile(file)
            return
    def handleLoadCHoice(self, choice, display, inputHandler):
        if choice == "N":
            return
        elif choice == "Y":
            file = inputHandler.getFileName()
            self.loadFromFile(file)
            return
    
    def saveToFile(self, fileName):
        f = open(fileName, "w")
        for month in self.months:
            for week in month.weeks:
                for day in week.days:
                    for event in day.events:
                        f.write(repr(event))
                        f.write("\n")
                        
        
    def loadFromFile(self, fileName):
        f = open(fileName, "r")
        lines = [line.strip() for line in f.readlines()]
        for i in range(0, len(lines), 6):
            title = lines[i]
            date = lines[i + 1]
            startTime = lines[i + 2]
            endTime = lines[i + 3]
            description = lines[i + 4]
            
            startTime = datetime.strptime(startTime, "%H:%M:%S").time()
            endTime = datetime.strptime(endTime, "%H:%M:%S").time()
            date = datetime.strptime(date, "%Y-%m-%d").date()
            
            event = Event(title, startTime, endTime, date, description)
            self.addEvent(event)
    
    def removeMonth():
        pass
    def addEvent(self, eventToAdd: Event):
        day = self.findDay(eventToAdd.date)
        day.addEvent(eventToAdd)
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
            
    def findDay(self, date):
        week = self.findWeek(date)  
        for day in week.days:
            if day.date == date:
                return day  
        
        
    def addMonth():
        pass
    def editEvent(self, inputHandler):
        day = inputHandler.getDayOfEventRemove(self)
        day.editEvent(inputHandler)
    def removeEvent(self, inputHandler):
        day = inputHandler.getDayOfEventRemove(self)
        day.removeEvent()
    def searchEvent():
        pass
