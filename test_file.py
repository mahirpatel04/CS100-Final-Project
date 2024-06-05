from datetime import date, time, timedelta
from classes.Calendar import Calendar
from classes.Day import Day
from classes.Display import DisplayClient
from classes.InputHandler import InputHandler
from classes.Event import Event
from classes.Month import Month
from classes.Week import Week

import pytest
import mock



class TestCalendar:
    def test_calendar_constructor(self):
        c = Calendar()
        for month in c.months:
            for week in month.weeks:
                for day in week.days:
                    assert type(day.date) == date
    
    def test_calendar_choices(self):
        c = Calendar()
        assert c.possibleChoices == ["1", "2", "3", "4", "5", "6"] 
        
                     
    def test_calendar_choices_addEvent(self):
        c = Calendar()
        d = DisplayClient()
        i = InputHandler()
        module = "classes.Calendar"
        mockFunc = f"{module}.InputHandler.getEventInfo"
        with mock.patch(mockFunc, return_value=Event("title", time(), time(), date.today(), "description")):
            assert c.handleUserMenuChoice("1", d, i) == 1
    
    def test_calendar_choices_removeEvent(self):
        c = Calendar()
        d = DisplayClient()
        i = InputHandler()
        module = "classes.Calendar"
        mockFunc = f"{module}.Calendar.removeEvent"
        
        with mock.patch(mockFunc, return_value=""):
            assert c.handleUserMenuChoice("2", d, i) == 2
    
    def test_calendar_choices_editEvent(self):
        c = Calendar()
        d = DisplayClient()
        i = InputHandler()
        module = "classes.Calendar"
        mockFunc = f"{module}.Calendar.editEvent"
        
        with mock.patch(mockFunc, return_value=""):
            assert c.handleUserMenuChoice("3", d, i) == 3
            
    def test_calendar_choices_viewWeek(self):
        c = Calendar()
        d = DisplayClient()
        i = InputHandler()
        module = "classes.Calendar"
        mockGetEventInfo = f"{module}.InputHandler.getWeek"
        with mock.patch(mockGetEventInfo, return_value=Week([Day(date.today())])):
            assert c.handleUserMenuChoice("4", d, i) == 4
    
    def test_calendar_choices_save(self):
        c = Calendar()
        d = DisplayClient()
        i = InputHandler()
        module = "classes.Calendar"
        mockGetEventInfo = f"{module}.InputHandler.getFileName"
        with mock.patch(mockGetEventInfo):
            assert c.handleUserMenuChoice("5", d, i) == 5
    
    def test_calendar_choices_quit(self):
        c = Calendar()
        d = DisplayClient()
        i = InputHandler()
        assert c.handleUserMenuChoice("6", d, i) == "Quit"
            
    def test_calendar_save_choice_NO(self):
        c = Calendar()
        d = DisplayClient()
        i = InputHandler()
        assert c.handleSaveChoice("N", d, i) == "N"
    
    def test_calendar_save_choice_YES(self):
        c = Calendar()
        d = DisplayClient()
        i = InputHandler()
        module = "classes.Calendar"
        mockGetEventInfo = f"{module}.InputHandler.getFileName"
        with mock.patch(mockGetEventInfo):
            assert c.handleSaveChoice("Y", d, i) == "Y"
    
    def test_calendar_load_choice_NO(self):
        c = Calendar()
        d = DisplayClient()
        i = InputHandler()
        assert c.handleLoadChoice("N", d, i) == "N"
    
    def test_calendar_load_choice_YES(self):
        c = Calendar()
        d = DisplayClient()
        i = InputHandler()
        module = "classes.Calendar"
        mockGetEventInfo = f"{module}.InputHandler.getFileName"
        with mock.patch(mockGetEventInfo):
            assert c.handleLoadChoice("Y", d, i) == "Y"
    
          
            
class TestDay:
    pass

class TestDisplayClient:
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






class TestInputHandler:
    def test_input_continue(self, monkeypatch):
        i = InputHandler()
        monkeypatch.setattr('builtins.input', lambda _: "C")
        test_input = i.getContinue()
        assert test_input == 1
    
    def test_input_menu_choice1(self, inputHandler, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "1")
        calendar = Calendar()
        test_input = inputHandler.getMenuChoice(calendar)
        assert test_input == "1"
    
    def test_input_menu_choice2(self, inputHandler, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "2")
        calendar = Calendar()
        test_input = inputHandler.getMenuChoice(calendar)
        assert test_input == "2"

    def test_input_menu_choice3(self, inputHandler, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "3")
        calendar = Calendar()
        test_input = inputHandler.getMenuChoice(calendar)
        assert test_input == "3"

    def test_input_menu_choice4(self, inputHandler, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "4")
        calendar = Calendar()
        test_input = inputHandler.getMenuChoice(calendar)
        assert test_input == "4"
    
    def test_input_menu_choice5(self, inputHandler, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "5")
        calendar = Calendar()
        test_input = inputHandler.getMenuChoice(calendar)
        assert test_input == "5"
    
    def test_input_menu_choice6(self, inputHandler, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "6")
        calendar = Calendar()
        test_input = inputHandler.getMenuChoice(calendar)
        assert test_input == "6"

    def test_get_save_choice1(self, inputHandler, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "Y")
        test_input = inputHandler.getSaveChoice()
        assert test_input == "Y"
    
    def test_get_save_choice2(self, inputHandler, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "N")
        test_input = inputHandler.getSaveChoice()
        assert test_input == "N"
    
    def test_load_save_choice1(self, inputHandler, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "Y")
        test_input = inputHandler.getLoadChoice()
        assert test_input == "Y"
    
    def test_get_save_choice2(self, inputHandler, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "N")
        test_input = inputHandler.getLoadChoice()
        assert test_input == "N"

    def test_get_file_name(self, inputHandler, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "test.txt")
        test_input = inputHandler.getFileName()
        assert test_input == "test.txt"

    def test_get_Week(self, inputHandler, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "2024-12-12")
        calendar = Calendar()
        test_input = inputHandler.getWeek(calendar)
        assert type(test_input) == Week

    def test_get_day_of_event_remove(self, inputHandler, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "2024-12-12")
        calendar = Calendar()
        test_input = inputHandler.getdayofEventRemove(calendar)
        assert type(test_input) == Day

    def test_get_name_of_event(self, inputHandler, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "birthday")
        calendar = Calendar()
        test_input = inputHandler.getNameofEvent()
        assert test_input == "birthday"

class TestMonth:
    pass

class TestWeek:
    pass


def greet(name):
    print(f"Hello, {name}!")
    
def test_greet(capfd):
    greet("World")
    out, err = capfd.readouterr()
    assert out == "Hello, World!\n"
    assert err == ""

class Teststuff:
    def test_something_that_involves_user_input(self):

        with mock.patch('builtins.input', return_value="yes"):
            assert input() == "yes"
            
        with mock.patch('builtins.input', return_value="no"):
            assert input() == "no"