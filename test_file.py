from datetime import date, timedelta
from classes.Calendar import Calendar
from classes.Day import Day
from classes.Display import DisplayClient
from classes.Event import Event
from classes.Month import Month
from classes.Week import Week
import pytest
today = date.today()
tmrw = today + timedelta(1)
dayAftertmrw = tmrw + timedelta(1)

testEvent1 = {"title": "event1",
              "startTime": today,
              "endTime": tmrw}


class TestDisplay:
    def test_displayClient(self):
        d = DisplayClient()
        
    def test_menu(self):
        d = DisplayClient()
        output = d.displayMenu()
        expected = f"Menu\n--------------------\n1. Add Event\n2. Remove Event\n3. Edit Event\n4. View Calendar\n5. Exit"
        assert output == expected
    
    def test_event(self):
        d = DisplayClient()
        event = Event("title", today, tmrw, 123, "description")
        output = d.displayEvent(event)
        expected = f"{event.title}\n--------------------\n{event.startTime} - {event.endTime}\n--------------------\n{event.description}"
        assert output == expected

class TestEvent:
    def test_event_constructor(self):
        e = Event("title", today, tmrw, 123, "description")
        assert e.title == "title"
        
        # START TIME AND END TIME DO NOT CONTAIN THE ACTUAL TIMES. THEY SIMPLE CONTAIN THE DATE. FIX LATER!!!
        # ---------------------------------------------------------------------
        assert e.startTime == today
        assert e.endTime == tmrw
        # ---------------------------------------------------------------------
        assert e.ID == 123
        assert e.description == "description"
    
    def test_edit_startTime(self):
        e = Event("title", today, tmrw, 123, "description")
        # not done...
        
    