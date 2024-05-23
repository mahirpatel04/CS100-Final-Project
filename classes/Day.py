from datetime import date
from Event import Event

class Day:
    def __init__(self, date: date, events: list):
        self.events = []
        self.date = date
    

    
    def removeEvent(self):
        name = input("Enter the exact name of the event you're gonna remove ")
        Identity = input("Enter the ID of the event ")
        Identity = int(Identity)
        find = Event(name, date, date, Identity)
        for item in self.events:
            if item.title == find.title:
                if item.ID == find.ID:
                    self.events.remove(item)
    def addEvent():
        pass

#test 
#one = Event("apple", date(2024, 5, 22), date(2024, 5, 23), 1)
#two = Event("banana", date(2024, 5, 22), date(2024, 5, 23), 1)
#three = Event("orange", date(2024, 5, 22), date(2024, 5, 23), 1)
#things = [one, two, three]
#todo = Day(date, things)
#todo.events = [one, two, three]
#for item in todo.events:
    #print(item)
##todo.removeEvent()
#for item in todo.events:
    #print(item)