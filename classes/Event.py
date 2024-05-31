from datetime import date

class Event:
    def __init__(self, title: str, startTime: date, endTime: date, ID: int, description: str):
        self.title = title
        self.startTime = startTime
        self.endTime = endTime
        self.ID = ID

    def __str__(self):
        return self.title

        self.description = description
    
    def __repr__(self) -> str:
        twentyDashes = "-" * 20
        return f"{self.title}\n{twentyDashes}\n{self.startTime} - {self.endTime}\n{twentyDashes}\n{self.description}"

