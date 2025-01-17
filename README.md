# Agenda Planner

## Team Members:
- Bhuvana Kotha - vkoth006 - https://github.com/bhuvanak04
- Mahir Patel - mpate141 - https://github.com/mahirpatel04
- Shaun Mansoor - smans029 - https://github.com/Mansoorkid
- Trisha Siva - tsiva006 - https://github.com/sivatrisha

## Project Description:

### Why is it important or interesting to you?
- Good for time management as a college student 
- Important to plan out projects
- Interesting because there are a lot of different features we can implement that are both functional and appealing to users
- Online planners allows users to access to manage their schedules from anywhere, compared to traditional written planners

### What languages/tools/technologies do you plan to use?
- C++

### What will be the input/output of your project?
- User inputs in details about upcoming events and deadlines they have
    - Start time, end time, date
    - People involved in the event
    - Description about task
    - So they can know when to plan the event/task and where it may fit best
    - User gets a clear view of their weekly tasks, events, etc
- Can get cool statistics such as:
    - XX% of your week was spent on homework
    - Completed XXX homework assignments
    - You average X hrs of sleep for the week


### What are the features that the project provides?
- Customization feature: user can select theme they like
- Allows users to input events and tasks to keep track of them
- Reminder feature
  - notifs for upcoming deadlines and events
- Event scheduling
  - Create multiple agendas for different purposes or events
- Task management
  - Allows users to add tasks or items to the agenda, set deadlines, etc
  - Suggests potential free days to schedule new events
  - Provides info and statistics on tasks completed during the 

  > ## Phase II

  ## User Interface Specification
### Navigation Diagram

 ![image](https://github.com/cs100/final-project-smans029-tsiva006-mpate141-vkoth006/assets/157240155/234196ca-56da-440d-ae35-3239d1f7b5f8)

 The user is first greeted with a simple Welcome message before proceeding to the main menu. Here, the user will be able to see and select several options of what they would like to do on their calendar application. Each option available corresponds to a different action they can perform, such as viewing the entire calendar, editing an existing event, removing an existing event, or adding a new one. The program then navigates to the appropriate page, based on the user input. From each section, the user will also be able to navigate back to the main menu page to then again choose what toher actions they would like to take int the program. 


### Screen Layouts

<img width="15000" alt="image" src="https://github.com/cs100/final-project-smans029-tsiva006-mpate141-vkoth006/assets/157240155/7ab21705-3c6a-4f03-904f-6dc87d49c778">





## Class Diagram
Version 1

![image](https://github.com/cs100/final-project-smans029-tsiva006-mpate141-vkoth006/assets/46858459/1b594a27-a24f-4f16-be7c-786680323d7e)

Version 2

![image](https://github.com/cs100/final-project-smans029-tsiva006-mpate141-vkoth006/assets/46858459/910b2141-c66e-424c-93aa-f578fe20387e)

Version 3

<img width="600" alt="image" src="https://github.com/cs100/final-project-smans029-tsiva006-mpate141-vkoth006/assets/157240155/39826a9e-7001-4c23-94f4-70fdd573c02c">




The week class contains an array of 7 day pointers, in which you can add, remove, display, or edit an event. These functions call helper functions from the Day class, which contains the events in it. It also conaints the struct of date, which contains the exact date that the user entered their data from, allowing them to plan out their week. The Day class contains the doubly linked list of events. It also contains the exact date that the day resides in after we calculate it from the time std library. The functions are almost all helper functions to those in Week. The eventNode class has all the components of the event, such as the title, start and end time, description, ID (in case 2 days have the same event), and the pointers to the events before and after it. 
 
 > ## Phase III
## SOLIDS:
The first SOLID principle we incorporated into our improved class diagram was the Single Responsibility Principle(SRP), which ensures that each class only has 1 responsibility. We implemented this by adding a new Display and InputHandler class, which only have one task each. The Display class is responsible for displaying information about each category. The InputHandler class is responsible for dealing with getting any user input. Initially, we had separate classes for these but this SOLID principle puts one class in charge of this responsibility.

Our model also incorporates Dependency Inversion Principle(DIP), of having modules dependent on interfaces. In our diagram, we can see high-level modules like Calendar and Display depend on abstractions (Month, Week, Day, EventNode) rather than concrete implementations. This allows for more flexibility.

Our classes also follow the interface segregation principle, which ensures that no subclass implements functions it doesn't absolutely need. We initially had an additional input function but later removed this in the recept scrum to simplify the program and make it more efficient. The program now takes in input through a separate InputHandler class, which we later implemented for improved efficiency. 

 
 > ## Final deliverable

 
 ## Screenshots
We are using python3 main.py to run our code and we can see our main display showing all the different menu choices in which the user can input. The user enters 1, which adds an event with the following title “Birthday Party” and further information such as the date, start time, end time, and description of event. The main menu is displayed again in which the user enters 4, in order to view our current calendar. 

<img width="425" alt="image" src="https://github.com/cs100/final-project-smans029-tsiva006-mpate141-vkoth006/assets/143913073/e2b5c1b1-7332-415e-9abe-49df9425a81d">


Now we are running the EDIT function and viewing our display’s changes. The user changed the title of the event from "Birthday Party" to "Alice's Birthday Party". The user then enters 6 to exit the edit function. 

<img width="425" alt="image" src="https://github.com/cs100/final-project-smans029-tsiva006-mpate141-vkoth006/assets/143913073/1b9e6083-b093-4cba-bb3a-9e5fc7badbf9">


**Now, the user is adding a new event and we can see the calendar with the two events that the user inputted.**

<img width="425" alt="image" src="https://github.com/cs100/final-project-smans029-tsiva006-mpate141-vkoth006/assets/143913073/3e817ccc-0b1f-46f5-8324-a301592f73a9">


**Output after choosing to add/remove an event**


<img width="425" alt="image" src="https://github.com/cs100/final-project-smans029-tsiva006-mpate141-vkoth006/assets/157240155/9cb23c71-f6fd-41e9-8fdd-64ff4f46f7b8">

**Output of an empty calander**

<img width="425" alt="image" src="https://github.com/cs100/final-project-smans029-tsiva006-mpate141-vkoth006/assets/157240155/c7e6105d-5375-457b-899f-e8e366bfa3ff">

**Example of a filled out calender output**

<img width="425" alt="image" src="https://github.com/cs100/final-project-smans029-tsiva006-mpate141-vkoth006/assets/143913073/4ab3def6-f26d-4b36-ab79-3ed0f1ed3f15">









 ## Installation/Usage
1. To install and run this calendar application, clone this repo into your local IDE.
2. Install dependencies required for the calendar and unittests, run the command: **pip install -r requirements.txt**
3. In the terminal, run the command: **python3 main.py** 
 ## Testing
 
Our project was tested and validated using a series of comprehensive test cases, which are contained in our 'test_file.py'. We wrote and executed these test cases to ensure that all our functions performed as expected. Although we did not use Continuous Integration (CI) tools, we followed a structured approach to manual testing.

**Unit testing:** We created unit tests for each function to validate their individual behaviors. These tests covered a range of inputs, including edge cases, to ensure robustness.

**Integration testing:** After unit testing, we performed integration testing to ensure that the interactions between different functions worked correctly.

**Tools used:** We used the mock library to simulate and test various functionalities and interactions within our classes. We also used pytest for testing.
 


