from datetime import date
from classes.Event import Event
from classes.InputHandler import InputHandler 

class Day:
    def __init__(self, date: date):
        self.date = date
        self.events = []

    

    
    def removeEvent(self):
        name = input("Enter the exact name of the event you're gonna remove ")
        Identity = input("Enter the ID of the event ")
        Identity = int(Identity)
        find = Event(name, date, date, Identity)
        for item in self.events:
            if item.title == find.title:
                if item.ID == find.ID:
                    self.events.remove(item)

    def addEvent(self, eventToAdd):
        # event_input_handler = InputHandler()
        new_event = eventToAdd

        # Insert the new event into the events list in order of start time and ensure no conflicts
        if self._insert_event_in_order(new_event):
            print("Event added successfully.")
        else:
            print("Event conflicts with existing events and was not added.")
    
    def _insert_event_in_order(self, new_event):

        #Insert the new event into the list of events in order based on start and end times.

        new_event_start_time = new_event.startTime
        new_event_end_time = new_event.endTime

        for index, event in enumerate(self.events):
            if new_event_end_time <= event.startTime:
                self.events.insert(index, new_event)
                return True
            elif new_event_start_time >= event.endTime:
                continue
            else:
                # Conflict detected
                return False

        # If no conflict and no earlier event is found, append the new event at the end
        self.events.append(new_event)
        return True
