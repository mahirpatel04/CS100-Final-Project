from datetime import datetime
from classes.Event import Event

class InputHandler:
    def getContinue(self):
        choice = input("Press 'C' to continue: ")
        while choice != "C":
            choice = input("Press 'C' to continue: ")
        return
        
    def getMenuChoice(self, calendar):
        choice =  input("Enter your input: ")
        while choice not in calendar.possibleChoices:
            return self.getMenuChoice(calendar)
        else:
            return choice
    
    def getSaveChoice(self):
        choice = input("Do you want to save your progress?(Y/N): ")
        while choice != "Y" and choice != "N":
            print("Invalid choice")
            choice = input("Do you want to save your progress?(Y/N): ")
        
        return choice
    
    def getLoadChoice(self):
        choice = input("Do you want to load calendar from a text file?(Y/N): ")
        while choice != "Y" and choice != "N":
            print("Invalid choice")
            choice = input("Do you want to save your progress?(Y/N): ")
        
        return choice
    
    def getFileName(self):
        fileName = input("Enter the filename you want to load from followed by .txt and make sure this file is in the same directory: ")
        while fileName[-4::] != ".txt":
            print("Only .txt files allowed")
            fileName = input("Enter the PROPERLY FORMATTED .txt filename: ")
        return fileName
    
    def getWeek(self, calendar):
        date = input("Enter date in form YYYY-MM-DD: ")
        date = datetime.strptime(date, "%Y-%m-%d").date()
        
        return calendar.findWeek(date)
        
    def getDayOfEventRemove(self, calendar):
        date = input("Enter date in form YYYY-MM-DD: ")
        date = datetime.strptime(date, "%Y-%m-%d").date()
        return calendar.findDay(date)
    
    def getNameofEvent(self):
        name = input("Enter the name of the event you want to remove: ")
        return name
        
    def getEventInfo(self):
        title = input("Enter title of your event: ")
        date = input("Enter date in form YYYY-MM-DD: ")
        startTime = input("Enter start time of event as HH:MM in 24 hour time: ")
        endTime = input("Enter end time of event as HH:MM in 24 hour time: ")
        
        startTime = datetime.strptime(startTime, "%H:%M").time()
        endTime = datetime.strptime(endTime, "%H:%M").time()
        
        date = datetime.strptime(date, "%Y-%m-%d").date()
        desc = input("Enter description of your event: ")
        
        return Event(title, startTime, endTime, date, desc)
    
    def getEditInfo(self):
        print("Edit options")
        print("Select 1 to change TITLE")
        print("Select 2 to Display event")
        print("Select 3 to change START TIME")
        print("Select 4 to change the END TIME")
        print("Select 5 to change the DESCRIPTION")
        print("Select 6 to EXIT")
        choice = input("Enter your input: ")
        return choice

    def getDescription(self):
        description = input("Enter the new descriptionf for the event: ")
        return description

    def getTitle(self):
        title = input("Enter the new title of the event: ")
        return title
    
    def getDate(self):
        date = input("Enter date in form YYYY-MM-DD: ")
        date = datetime.strptime(date, "%Y-%m-%d").date()
        return date
    
    def getTime(self):
        time = input("Enter the new time as HH:MM in 24 hour time: ")
        time = datetime.strptime(time, "%H:%M").time()
        return time

    def getNameofEventEdit(self):
        name = input("Enter the name of the event you want to edit: ")
        return name
        
