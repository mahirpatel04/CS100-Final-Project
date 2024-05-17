from datetime import date

class Event:
    def __init__(self, title: str, startTime: date, endTime: date, ID: int):
        self.title = title
        self.startTime = startTime
        self.endTime = endTime
        self.ID = ID
    