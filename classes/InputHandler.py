from datetime import datetime
from Event import Event

class InputHandler:
    def get_event_from_user(self):
        title = input("Enter the event title: ")
        start_time_str = input("Enter the event start time (HH:MM): ")
        end_time_str = input("Enter the event end time (HH:MM): ")
        description = input("Enter a description for the event: ")

        # Convert start and end time to datetime objects
        start_time = datetime.strptime(start_time_str, "%H:%M").time()
        end_time = datetime.strptime(end_time_str, "%H:%M").time()

        # event_id placeholder
        event_id = 1340981

        # Create an Event instance using Event constructor
        return Event(title, start_time, end_time, event_id, description)
