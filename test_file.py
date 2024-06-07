from datetime import date, time, timedelta, datetime
from classes.Calendar import Calendar
from classes.Day import Day
from classes.Display import DisplayClient
from classes.InputHandler import InputHandler
from classes.Event import Event
from classes.Month import Month
from classes.Week import Week
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
        assert c.addEvent(e)
    
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
    def test_displayClient_WelcomeMessage(self, capfd):
        d = DisplayClient()
        d.displayWelcome()
        out, err = capfd.readouterr()
        assert out == "Welcome to R'Agenda! You can plan and schedule events in this text-based planner.\n\n"
        assert err == ""
        
    def test_displayClient_Menu(self, capfd):
        d = DisplayClient()
        d.displayMenu()
        out, err = capfd.readouterr()
        assert out == f"MAIN MENU\nSelect 1 to ADD an event\nSelect 2 to REMOVE an event\nSelect 3 to EDIT an event\nSelect 4 to VIEW your calendar\nSelect 5 to SAVE your calendar\nSelect 6 to EXIT\n"
        assert err == ""
    
    def test_displayClient_ViewEmptyWeek(self, capfd):
        d = DisplayClient()
        c = Calendar()    
        week = c.months[0].weeks[0]
        d.viewWeek(week)
        out, err = capfd.readouterr()
        assert out == f"{week.days[0].date}\n--------------------\n{week.days[1].date}\n--------------------\n{week.days[2].date}\n--------------------\n{week.days[3].date}\n--------------------\n{week.days[4].date}\n--------------------\n{week.days[5].date}\n--------------------\n{week.days[6].date}\n--------------------\n"
        assert err == ""
    
    def test_displayClient_ViewEmptyWeek(self, capfd):
        d = DisplayClient()
        c = Calendar()    
        week = c.months[0].weeks[0]

        d.viewWeek(week)
        out, err = capfd.readouterr()
        assert out == f"{week.days[0].date}\n--------------------\n{week.days[1].date}\n--------------------\n{week.days[2].date}\n--------------------\n{week.days[3].date}\n--------------------\n{week.days[4].date}\n--------------------\n{week.days[5].date}\n--------------------\n{week.days[6].date}\n--------------------\n"
        assert err == ""
    
    def test_displayClient_ViewFilledWeek(self, capfd):
        d = DisplayClient()
        c = Calendar()
        currTime = time()
        oneHrLater = time(1)
        twoHrsLater = time(2)
        e = Event("title1", currTime, currTime, date.today(), "description")
        e2 = Event("title2", oneHrLater, oneHrLater, date.today(), "description")
        e3 = Event("title3", twoHrsLater, twoHrsLater, date.today(), "description")
        c.addEvent(e)
        c.addEvent(e2)
        c.addEvent(e3)
        week = c.months[0].weeks[0]
        d.viewWeek(week)
        out, err = capfd.readouterr()
        exp = "Event added successfully.\nEvent added successfully.\nEvent added successfully.\n"
        for day in week.days:
            if day.date == date.today():
                exp += f"{day.date}\n--------------------\n"
                for event in day.events:
                    exp += f"Title: {event.title}\nTiming: {event.startTime} - {event.endTime}\nDescription: {event.description}\n\n"
            else:
                exp += f"{day.date}\n--------------------\n"
        assert out == exp
        assert err == ""

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
            assert e.edit(i) == "Succesful"

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
        