from datetime import date

class Event:
    def __init__(self, title: str, startTime: date, endTime: date, ID: int, description: str):
        self.title = title
        self.startTime = startTime
        self.endTime = endTime
        self.ID = ID
        self.description = description
    
    def __repr__(self) -> str:
        return f"{self.title}\n----------\n{self.startTime} - {self.endTime}\n----------\n{self.description}"
    