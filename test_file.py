from datetime import date, timedelta
from classes.Calendar import Calendar
from classes.Day import Day
from classes.Display import DisplayClient
from classes.Event import Event
from classes.Month import Month
from classes.Week import Week
today = date.today()
tmrw = today + timedelta(1)
dayAftertmrw = tmrw + timedelta(1)

testEvent1 = {"title": "event1",
              "startTime": today,
              "endTime": tmrw}



class TestCalendar:
    pass

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
    def test_input_continue(self, inputHandler, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "C")
        test_input = inputHandler.getContinue()
        assert test_input == "1"
    
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