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
        mockFunc = f"{module}.InputHandler.getWeek"
        with mock.patch(mockFunc, return_value=Week([Day(date.today())])):
            assert c.handleUserMenuChoice("4", d, i) == 4
    
    def test_calendar_choices_save(self):
        c = Calendar()
        d = DisplayClient()
        i = InputHandler()
        module = "classes.Calendar"
        mockFunc = f"{module}.InputHandler.getFileName"
        with mock.patch(mockFunc):
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
        mockFunc = f"{module}.InputHandler.getFileName"
        with mock.patch(mockFunc):
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
        mockFunc = f"{module}.InputHandler.getFileName"
        with mock.patch(mockFunc):
            assert c.handleLoadChoice("Y", d, i) == "Y"
    
    def test_calendar_loadFromFile(self):
        c = Calendar()
        assert (c.loadFromFile("input.txt") == "Loaded")
    
    def test_calendar_saveToFile(self):
        c = Calendar()
        e = Event("title", time(), time(), date.today(), "description")
        c.months[0].weeks[0].days[0].addEvent(e)
        assert (c.saveToFile("output.txt") == "Saved")  
            
            
    def test_calendar_addEvent(self):
        c = Calendar()
        e = Event("title", time(), time(), date.today(), "description")
        assert(c.addEvent(e), True)
    
    def test_calendar_findMonth1(self):
        c = Calendar()
        e = Event("title", time(), time(), date.today(), "description")
        c.addEvent(e)
        assert (c.findMonth(date.today()) == c.months[0])
    
    def test_calendar_findMonth2(self):
        c = Calendar()
        e = Event("title", time(), time(), date.today()+ timedelta(days=30), "description")
        c.addEvent(e)
        assert (c.findMonth(date.today() + timedelta(days=30)) == c.months[1])
    
    
    def test_calendar_findWeek1(self):
        c = Calendar()
        e = Event("title", time(), time(), date.today(), "description")
        c.addEvent(e)
        assert (c.findWeek(date.today()) == c.months[0].weeks[0])
    
    def test_calendar_findDay1(self):
        c = Calendar()
        assert ((c.findDay(date.today()).date) == date.today()) 
    
    def test_calendar_findDay2(self):
        c = Calendar()
        dateToFind = date.today() + timedelta(days=15)
        assert ((c.findDay(dateToFind)).date == dateToFind)
    
    def test_calendar_findDay3(self):
        c = Calendar()
        dateToFind = date.today() + timedelta(days=25)
        assert ((c.findDay(dateToFind)).date == dateToFind)
    
    def test_calendar_editEvent(self):
        c = Calendar()
        i = InputHandler()
        e = Event("title", time(), time(), date.today(), "description")
        c.addEvent(e)
        
        module = "classes.Calendar"
        mockFunc = f"{module}.InputHandler.getDayOfEventRemove"
        
        module2 = "classes.Day"
        mockFunc2 = f"{module2}.Day.editEvent"
        with mock.patch(mockFunc, return_value=c.findDay(e.date)):
            module2 = "classes.Day"
            mockFunc2 = f"{module2}.Day.editEvent"
            with mock.patch(mockFunc2):
                assert c.editEvent(i) == True
        
        
    def test_calendar_removeEvent(self):
        c = Calendar()
        i = InputHandler()
        e = Event("title", time(), time(), date.today(), "description")
        c.addEvent(e)
        
        module = "classes.Calendar"
        mockFunc = f"{module}.InputHandler.getDayOfEventRemove"
        
        module2 = "classes.Day"
        mockFunc2 = f"{module2}.Day.removeEvent"
        with mock.patch(mockFunc, return_value=c.findDay(e.date)):
            module2 = "classes.Day"
            mockFunc2 = f"{module2}.Day.removeEvent"
            with mock.patch(mockFunc2):
                assert c.removeEvent(i) == True
            
class TestDay:
    def test_day_constructorDate(self):
        d = Day(date.today())
        assert date.today() == d.date
        
    def test_day_constructorEventsList(self):
        d = Day(date.today())
        assert not d.events
    
    def test_day_addEvent1(self):
        d = Day(date.today())
        e = Event("title", time(), time(), date.today(), "description")
        d.addEvent(e)
        assert (len(d.events) == 1)
    
    def test_day_addEvent2(self):
        d = Day(date.today())
        e = Event("title", time(), time(), date.today(), "description")
        d.addEvent(e)
        assert (d.events[0] == e)
    
    def test_day_addEventInOrder1(self):
        d = Day(date.today())
        currTime = time()
        oneHrLater = time()
        e = Event("title1", currTime, currTime, date.today(), "description")
        e2 = Event("title2", oneHrLater, oneHrLater, date.today(), "description")
        d.addEvent(e)
        d.addEvent(e2)
        assert (len(d.events) == 2)
    
    def test_day_addEventInOrder2(self):
        d = Day(date.today())
        currTime = time()
        oneHrLater = time(1)
        e = Event("title1", currTime, currTime, date.today(), "description")
        e2 = Event("title2", oneHrLater, oneHrLater, date.today(), "description")
        d.addEvent(e)
        d.addEvent(e2)
        assert d.events[0] == e
        assert d.events[1] == e2
    
    def test_day_addEventInOrder3(self):
        d = Day(date.today())
        currTime = time()
        oneHrLater = time(1)
        twoHrsLater = time(2)
        e = Event("title1", currTime, currTime, date.today(), "description")
        e2 = Event("title2", oneHrLater, oneHrLater, date.today(), "description")
        e3 = Event("title3", twoHrsLater, twoHrsLater, date.today(), "description")
        d.addEvent(e)
        d.addEvent(e2)
        d.addEvent(e3)
        assert d.events[0] == e
        assert d.events[1] == e2
        assert d.events[2] == e3
    
    def test_day_editEvent_That_Exists(self):
        d = Day(date.today())
        e = Event("title1", time(), time(), date.today(), "description")
        d.addEvent(e)
        i = InputHandler()
        module = "classes.Day"
        mockFunc = f"{module}.InputHandler.getNameofEventEdit"
        with mock.patch(mockFunc, return_value="title1"):
            module2 = "classes.Event"
            mockFunc2 = f"{module2}.Event.edit"
            with mock.patch(mockFunc2):
                assert d.editEvent(i) == True
        
    def test_day_editEvent_That_DoesNot_Exists(self):
        d = Day(date.today())
        e = Event("title1", time(), time(), date.today(), "description")
        d.addEvent(e)
        i = InputHandler()
        module = "classes.Day"
        mockFunc = f"{module}.InputHandler.getNameofEventEdit"
        with mock.patch(mockFunc, return_value="FAIL"):
            module2 = "classes.Event"
            mockFunc2 = f"{module2}.Event.edit"
            with mock.patch(mockFunc2):
                assert d.editEvent(i) == False
            
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