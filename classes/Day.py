from datetime import date

class Day:
    def __init__(self, date: date, events: list):
        self.events = []
        self.date = date
    

    
    def removeEvent(self):
        name = input("Enter the exact name of the event you're gonna remove ")
        for item in self.events:
            if item == name:
                self.events.remove(name)

    def addEvent():
        pass


# test
#things = ["apple", "banana", "orange"]
#todo = Day(date, things)
#print(todo.events)
#todo.events = ["apple", "banana", "orange"]
#print(todo.events)
#todo.removeEvent()
#print(todo.events)