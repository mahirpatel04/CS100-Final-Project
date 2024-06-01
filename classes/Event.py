from datetime import date, time

class Event:
    def __init__(self, title: str, startTime: time, endTime: time, date: date, description: str):
        self.title = title
        self.startTime = startTime
        self.endTime = endTime
        self.date = date
        self.description = description


    def __str__(self) -> str:
        return f"Title: {self.title}\nTiming: {self.startTime} - {self.endTime}\nDescription: {self.description}\n"

    def __repr__(self):
        return f"{self.title}\n{self.date}\n{self.startTime}\n{self.endTime}\n{self.description}\n"
    
