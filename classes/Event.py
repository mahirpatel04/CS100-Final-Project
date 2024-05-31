from datetime import date

class Event:
    def __init__(self, title: str, startTime: date, endTime: date, ID: int, description: str):
        self.title = title
        self.startTime = startTime
        self.endTime = endTime
        self.ID = ID
        self.description = description

    def __str__(self):
        return f"{self.title}, {self.startTime} - {self.endTime}\n{self.description}"
    
    
    def __repr__(self) -> str:
        twentyDashes = "-" * 20
        return f"{self.title}\n{twentyDashes}\n{self.startTime} - {self.endTime}\n{twentyDashes}\n{self.description}"

