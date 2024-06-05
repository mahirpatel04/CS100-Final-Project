from datetime import date, time, timedelta, datetime
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
        e = Event("title", time(), time(), date.today(), "description")
        assert e.title == "title"
        
        # START TIME AND END TIME DO NOT CONTAIN THE ACTUAL TIMES. THEY SIMPLE CONTAIN THE DATE. FIX LATER!!!
        # ---------------------------------------------------------------------
        assert e.startTime == time()
        assert e.endTime == time()
        assert e.date == date.today()
        # ---------------------------------------------------------------------
        assert e.description == "description"
    
    def test_edit_startTime(self, monkeypatch):
        i = InputHandler()
        monkeypatch.setattr('builtins.input', lambda _: "11:11")
        e = Event("title", timedelta, timedelta(), date.today(), "description")
        e.editStartTime(i)
        time = "11:11"
        time = datetime.strptime(time, "%H:%M").time()
        assert e.startTime == time

    def test_edit_EndTime(self, monkeypatch):
        i = InputHandler()
        monkeypatch.setattr('builtins.input', lambda _: "11:11")
        e = Event("title", timedelta, timedelta(), date.today(), "description")
        e.editEndTime(i)
        time = "11:11"
        time = datetime.strptime(time, "%H:%M").time()
        assert e.endTime == time

    def test_edit_description(self, monkeypatch):
        i = InputHandler()
        monkeypatch.setattr('builtins.input', lambda _: "changed")
        e = Event("title", timedelta, timedelta(), date.today(), "description")
        e.editDescription(i)
        assert e.description == "changed"
    
    def test_edit_title(self, monkeypatch):
        i = InputHandler()
        monkeypatch.setattr('builtins.input', lambda _: "changed")
        e = Event("title", timedelta, timedelta(), date.today(), "description")
        e.editTitle(i)
        assert e.title == "changed"
    
    def test_edit_choice(self, monkeypatch):
        i = InputHandler()
        monkeypatch.setattr('builtins.input', lambda _: "6")
        e = Event("title", timedelta, timedelta(), date.today(), "description")
        module = "classes.InputHandler"
        module2 = "classes.Event"
        mockEditTitle = f"{module2}.Event.editTitle"
        mockEditEvent= f"{module}.InputHandler.getTitle"
        with mock.patch(mockEditEvent) and mock.patch(mockEditTitle):
            assert e.edit(i) == None

class TestInputHandler:

    def test_input_continue(self, monkeypatch):
        i = InputHandler()
        monkeypatch.setattr('builtins.input', lambda _: "C")
        test_input = i.getContinue()
        assert test_input == 1
    
    def test_input_menu_choice1(self, monkeypatch):
        i = InputHandler()
        monkeypatch.setattr('builtins.input', lambda _: "1")
        calendar = Calendar()
        test_input = i.getMenuChoice(calendar)
        assert test_input == "1"
    
    def test_input_menu_choice2(self, monkeypatch):
        i = InputHandler()
        monkeypatch.setattr('builtins.input', lambda _: "2")
        calendar = Calendar()
        test_input = i.getMenuChoice(calendar)
        assert test_input == "2"

    def test_input_menu_choice3(self, monkeypatch):
        i = InputHandler()
        monkeypatch.setattr('builtins.input', lambda _: "3")
        calendar = Calendar()
        test_input = i.getMenuChoice(calendar)
        assert test_input == "3"

    def test_input_menu_choice4(self, monkeypatch):
        i = InputHandler()
        monkeypatch.setattr('builtins.input', lambda _: "4")
        calendar = Calendar()
        test_input = i.getMenuChoice(calendar)
        assert test_input == "4"
    
    def test_input_menu_choice5(self, monkeypatch):
        i = InputHandler()
        monkeypatch.setattr('builtins.input', lambda _: "5")
        calendar = Calendar()
        test_input = i.getMenuChoice(calendar)
        assert test_input == "5"
    
    def test_input_menu_choice6(self, monkeypatch):
        i = InputHandler()
        monkeypatch.setattr('builtins.input', lambda _: "6")
        calendar = Calendar()
        test_input = i.getMenuChoice(calendar)
        assert test_input == "6"

    def test_get_save_choice1(self, monkeypatch):
        i = InputHandler()
        monkeypatch.setattr('builtins.input', lambda _: "Y")
        test_input = i.getSaveChoice()
        assert test_input == "Y"
    
    def test_get_save_choice2(self, monkeypatch):
        i = InputHandler()
        monkeypatch.setattr('builtins.input', lambda _: "N")
        test_input = i.getSaveChoice()
        assert test_input == "N"
    
    def test_load_save_choice1(self, monkeypatch):
        i = InputHandler()
        monkeypatch.setattr('builtins.input', lambda _: "Y")
        test_input = i.getLoadChoice()
        assert test_input == "Y"
    
    def test_get_save_choice2(self, monkeypatch):
        i = InputHandler()
        monkeypatch.setattr('builtins.input', lambda _: "N")
        test_input = i.getLoadChoice()
        assert test_input == "N"

    def test_get_file_name(self, monkeypatch):
        i = InputHandler()
        monkeypatch.setattr('builtins.input', lambda _: "test.txt")
        test_input = i.getFileName()
        assert test_input == "test.txt"

    def test_get_Week(self, monkeypatch):
        i = InputHandler()
        monkeypatch.setattr('builtins.input', lambda _: "2024-12-12")
        calendar = Calendar()
        test_input = i.getWeek(calendar)
        assert type(test_input) == Week

    def test_get_day_of_event_remove(self, monkeypatch):
        i = InputHandler()
        monkeypatch.setattr('builtins.input', lambda _: "2024-12-12")
        calendar = Calendar()
        test_input = i.getDayOfEventRemove(calendar)
        assert type(test_input) == Day

    def test_get_name_of_event(self, monkeypatch):
        i = InputHandler()
        monkeypatch.setattr('builtins.input', lambda _: "birthday")
        calendar = Calendar()
        test_input = i.getNameofEvent()
        assert test_input == "birthday"

    def test_get_string_title(self, monkeypatch):
        i = InputHandler()
        monkeypatch.setattr('builtins.input', lambda _: "test title")
        test_input = i.getStringTitle()
        assert test_input == "test title"
    
    def test_get_string_date(self, monkeypatch):
        i = InputHandler()
        monkeypatch.setattr('builtins.input', lambda _: "2024-12-16")
        test_input = i.getStringDate()
        assert test_input == "2024-12-16"
    
    def test_get_start_time(self, monkeypatch):
        i = InputHandler()
        monkeypatch.setattr('builtins.input', lambda _: "11:11")
        test_input = i.getStartTime()
        assert test_input == "11:11"

    def test_get_start_time(self, monkeypatch):
        i = InputHandler()
        monkeypatch.setattr('builtins.input', lambda _: "11:11")
        test_input = i.getEndTime()
        assert test_input == "11:11"

    def test_get_edit_info(self, monkeypatch):
        i = InputHandler()
        monkeypatch.setattr('builtins.input', lambda _: "1")
        test_input = i.getEditInfo()
        assert test_input == "1"

    def test_get_description(self, monkeypatch):
        i = InputHandler()
        monkeypatch.setattr('builtins.input', lambda _: "test input")
        test_input = i.getDescription()
        assert test_input == "test input"
    
    def test_get_title(self, monkeypatch):
        i = InputHandler()
        monkeypatch.setattr('builtins.input', lambda _: "test title")
        test_input = i.getDescription()
        assert test_input == "test title"
    
    def test_get_Date(self, monkeypatch):
        i = InputHandler()
        monkeypatch.setattr('builtins.input', lambda _: "2024-12-12")
        test_input = i.getDate()
        assert type(test_input) == date

    def test_get_Time(self, monkeypatch):
        i = InputHandler()
        monkeypatch.setattr('builtins.input', lambda _: "12:12")
        test_input = i.getTime()
        assert type(test_input) == time

    def test_get_name_of_event_edit(self, monkeypatch):
        i = InputHandler()
        monkeypatch.setattr('builtins.input', lambda _: "test name")
        test_input = i.getDescription()
        assert test_input == "test name"
     

class TestMonth:
    def test_month_constructor(self):
        day = date.today()
        listofDays = [day]
        test_month = Month(listofDays, 1)
        for week in test_month.weeks:
            for day in week.days:
                assert type(day.date) == date
        
    def test_remove_event(self, monkeypatch):
        day = date.today()
        listofDays = [day]
        test_month = Month(listofDays, 1)
        monkeypatch.setattr('builtins.input', lambda _: "birthday")
        module = "classes.Week"
        mockRemoveEvent= f"{module}.Week.removeEvent"
        with mock.patch(mockRemoveEvent):
            assert test_month.removeEvent() == None

class TestWeek:
    def test_week_contructor(self):
        day = date.today()
        listofDays = [day]
        test_week = Week(listofDays)
        for day in test_week.days:
            assert type(day.date) == date
        
    def test_remove_event(self, monkeypatch):
        day = date.today()
        listofDays = [day]
        test_week = Week(listofDays)
        monkeypatch.setattr('builtins.input', lambda _: "birthday")
        module = "classes.Day"
        mockRemoveEvent= f"{module}.Day.removeEvent"
        with mock.patch(mockRemoveEvent):
            assert test_week.removeEvent() == None


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