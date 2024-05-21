from datetime import date
from classes.Event import Event
class Day:
    def __init__(self, date: date):
        self.date = date
        
    def addEvent(self):
        title = input("Enter the event title: ")
        start_time = input("Enter the event start time (HH:MM): ")
        end_time = input("Enter the event end time (HH:MM): ")
        description = input("Enter a description for the event: ")
        
        event = {
            "title": title,
            "start_time": start_time,
            "end_time": end_time,
            "description": description
        }
        
        self.events.append(event)
        print("Event", event, "was added successfully.")