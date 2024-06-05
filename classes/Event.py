from datetime import date, time

class Event:
    def __init__(self, title: str, startTime: time, endTime: time, date: date, description: str):
        self.title = title
        self.startTime = startTime
        self.endTime = endTime
        self.date = date
        self.description = description

    def edit(self, inputHandler):
        choice = inputHandler.getEditInfo()
        while choice != "6":
            if choice == "1":
                self.editTitle(inputHandler)
                choice = inputHandler.getEditInfo()
            elif choice == "2":
                print(self)
                choice = inputHandler.getEditInfo()
            elif choice == "3":
                self.editStartTime(inputHandler)
                choice = inputHandler.getEditInfo()
            elif choice == "4":
                self.editEndTime(inputHandler)
                choice = inputHandler.getEditInfo()
            elif choice == "5":
                self.editDescription(inputHandler)
                choice = inputHandler.getEditInfo()
            else:
                choice = input("Invalid input, try again: ")
        
        print("Event edited successfully")
        return "Succesful"

    def __str__(self) -> str:
        return f"Title: {self.title}\nTiming: {self.startTime} - {self.endTime}\nDescription: {self.description}\n"

    def __repr__(self):
        return f"{self.title}\n{self.date}\n{self.startTime}\n{self.endTime}\n{self.description}\n"
    
    def editTitle(self, inputHandler):
        newTitle = inputHandler.getTitle()
        self.title = newTitle
    
    def editStartTime(self, inputHandler):
        newstartTime = inputHandler.getTime()
        self.startTime = newstartTime

    def editEndTime(self, inputHandler):
        newEndTime = inputHandler.getTime()
        self.endTime = newEndTime

    def editDescription(self, inputHandler):
        newDescription = inputHandler.getDescription()
        self.description = newDescription